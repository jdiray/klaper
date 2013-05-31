"""
Charles Murphy
murphy.charlesj@gmail.com

Takes output table from edgeR
and concatenates the Blast2GO annotation done by Purdue.

"""

#TODO TEST THIS!


import argparse
import pandas
import sys
from Bio import SeqIO
import pdb

def main():
    
    parser = argparse.ArgumentParser(description="Extract fasta file.")
    parser.add_argument('-table1',nargs=1,type=str,help="Table containing DE results.")
    parser.add_argument('-table2',nargs=1,type=str,help="Table containing Blast2GO results.")
    parser.add_argument('-fasta',nargs=1,type=str,help="Fasta file containing trinity contigs.")
    parser.add_argument('-out',nargs=1,type=str,help="Out file.")
    args = parser.parse_args()

    sequences = dict()
    
    #load fasta
    fin = open(args.fasta[0],"rU")
    for sequence in SeqIO.parse(fin,"fasta"):
        sequences[sequence.id] = sequence.seq._data
    fin.close()

    #load tables
    
    table1 = pandas.read_table(args.table1[0])
    table2 = pandas.read_table(args.table2[0])
    

    #parse data
    table2.index = table2.Contig
    table2sub = table2.ix[table1.index]
    t2 = table2sub[['Blast hit','GO terms or Genbank IDs']]
    t3 = table1.join(t2)

    #add sequence data
    sequencesSub = map(lambda x: sequences[x],t3.index)
    temp = pandas.DataFrame({'sequences':pandas.Series(sequencesSub,index=t3.index)})
    t3 = t3.join(temp)


    t3.to_csv(args.out[0],sep='\t',index=True)
    sys.exit()

if __name__=='__main__':
    main()