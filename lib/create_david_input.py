"""
Charles Murphy
murphy.charlesj@gmail.com

Creates the input list of UniProt IDS that are needed for IPA and DAVID
from the results of running Trinotate and the edgeR wrapper in Trinity.

Input:
Trinotate output table from running:
Trinotate.pl report [opts] > trinotate_annotation_report.xls

DE results from running:
$TRINITY_HOME/Analysis/DifferentialExpression/run_DE_analysis.pl

Outputs:
File containing uniprot ids

"""

import argparse
import pandas
import sys
from Bio import SeqIO
import pdb

def main():

    parser = argparse.ArgumentParser(description="Extract fasta file.")
    parser.add_argument('-DE',nargs=1,type=str,help="Table containing DE results.")
    parser.add_argument('-trinity',nargs=1,type=str,help="Trinity results.")
    parser.add_argument('-out',nargs=1,type=str,help="Out file.")
    args = parser.parse_args()


    #load tables

    DEResults = pandas.read_table(args.DE[0])
    trinityResults = pandas.read_table(args.trinity[0])


    #parse data

    temp = list(trinityResults['trans_derived'])
    temp = map(lambda x: x.split(':')[0],temp)
    trinityResults.index = temp


    filtered_trinityResults = trinityResults.ix[DEResults.index]
    topBlastHit = list(filtered_trinityResults['TopBlastHit'])

    uniprotID=[]

    for i in topBlastHit:
        if i is not '.':
            uniprotID.append(i.split('|')[1])

    uniprotID = pandas.DataFrame(uniprotID)
    uniprotID.to_csv(args.out[0],sep='\n',header=False,index=False)

    sys.exit(0)

if __name__=='__main__':
    main()
