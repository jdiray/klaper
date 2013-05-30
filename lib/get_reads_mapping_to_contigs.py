from Bio import SeqIO
import argparse
import sys
import random
import pandas
import pysam
import subprocess
import os

def __main__():

    parser = argparse.ArgumentParser(description="Given a FASTA file containing contigs and FASTQ file(s)."
                                                 " Select a few")

    parser.add_argument('-fasta',nargs=1,type=str,help='FASTA file containing contigs.')
    parser.add_argument('-selected_sequences',nargs=1,type=str,help='FASTA file containing selected contigs.')
    parser.add_argument('-bam',nargs='+',action='append',type=str,help='Space delimited list of BAM files.')
    parser.add_argument('-fastq',nargs='+',action='append',type=str,help='Space delimited list of FASTQ files.')
    parser.add_argument('-N',type=int,help='Number of contigs to select.')
    parser.add_argument('-output',nargs=1,type=str,help='FASTA file to save the selected contigs.')
    parser.add_argument('-fastq_out',nargs=1,type=str,help='FASTQ file to save the retrieved reads.')


    args = parser.parse_args()

    #read sequence file
    if not args.selected_sequences:
        sequences = load_sequences(args.fasta[0])

        print 'Binning sequences...'
        binned_sequences = bin_sequences(sequences,args.N)

        print 'Selecting sequences...'
        selected_sequences = select_sequences(binned_sequences)

        print_sequences(selected_sequences,args.output[0])
    else:
        selected_sequences = load_sequences(args.selected_sequences[0])

    #iterate over BAM file
    sequence_ids = get_contig_sequence_ids(selected_sequences)
    print sequence_ids
    query_sequence_ids = iterate_over_bam_files(sequence_ids,args.bam[0])
    print query_sequence_ids

    query_sequences = get_sequence_reads(query_sequence_ids,args.fastq[0],args.fastq_out[0])
    #print query_sequences

    sys.exit()

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = dict()
    last = 0.0
    N=1

    while last < len(seq):
        out[N] = seq[int(last):int(last + avg)]
        last += avg
        N += 1

    return out

def load_sequences(file):

    sequences = []

    fin = open(file,"rU")

    for sequence in SeqIO.parse(fin,"fasta"):
        sequences.append(sequence)

    fin.close()

    return sequences

def bin_sequences(sequences,N):

    sequence_lengths = map(lambda x: len(x),sequences)
    sequence_max = max(sequence_lengths)
    sequence_min = min(sequence_lengths)

    bins = chunkIt(range(sequence_min,sequence_max+1),N)

    binned_sequences = dict.fromkeys(bins.keys(),[])

    for i in bins:
        temp = pandas.DataFrame({'lengths':sequence_lengths,'sequences':sequences})
        temp1 = temp['lengths'] >= bins[i][0]
        temp1 = temp1.tolist()
        temp2 = temp['lengths'] <= bins[i][len(bins[i])-1]
        temp2 = temp2.tolist()

        temp1 = zip(temp1,temp2)
        temp1 = map(lambda x: x[0] and x[1],temp1)

        temp['lengths'] = temp['lengths'][temp1]
        temp = temp.dropna()
        binned_sequences[i] = temp['sequences'].tolist()


    return binned_sequences

def select_sequences(binned_sequences):

    selected_sequences = []

    for i in binned_sequences:
        number = random.randint(0,len(binned_sequences[i]))
        selected_sequences.append(binned_sequences[i][number])

    return selected_sequences

def print_sequences(selected_sequences,out_file):

    fout = open(out_file,'w')
    SeqIO.write(selected_sequences,fout,"fasta")
    fout.close()

def get_contig_sequence_ids(sequences):
    sequence_ids = []

    for i in sequences:
        sequence_ids.append(i.id)

    return sequence_ids

def iterate_over_bam_files(sequence_ids,bam_files):
    query_sequence_ids = []

    for bam_file in bam_files:
        fin = pysam.Samfile(bam_file)
        for read in fin.fetch():

            if fin.getrname(read.tid) in sequence_ids:
                query_sequence_ids.append(read.qname)
        fin.close()

    return query_sequence_ids

def worker(fastq,N):
    os.system('cat '+fastq+' | python parse.py lids.txt > filtered.fastq')

def get_sequence_reads(query_sequence_ids,fastq_files,output):

    fout = open("tmp.out",'w')
    for i in query_sequence_ids:
        fout.write(i+'\n')
    fout.close()
    processes = set()
    max_processes = 4

    for i in fastq_files:
        print i
        command = 'cat '+i+' | python parse.py lids.txt > filtered.fastq'

        processes.add(subprocess.Popen([command],shell=True))


    #query_sequences = []

    #for i in fastq_files:
    #    print i[0]
    #    fin = open(i[0],"rU")

    #    for sequence in SeqIO.parse(fin,"fastq"):
    #        if sequence.id in query_sequence_ids:
    #            query_sequences.append(sequence)

    #    fin.close()

    #return query_sequences


if __name__=='__main__':
    __main__()