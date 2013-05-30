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

def main():
    
    parser = argparse.ArgumentParser(description="Extract fasta file.")
    parser.add_argument('-table1',nargs=1,type=str,help="Table containing DE results.")
    parser.add_argument('-table2',nargs=1,type=str,help="Table containing Blast2GO results.")
    parser.add_argument('-out',nargs=1,type=str,help="Out file.")
    args = parser.parse_args()

    
    
    #load tables
    
    table1 = pandas.read_table(args.table1[0])
    table2 = pandas.read_table(args.table2[0])
    
    
    table2.index = table2.Contig
    table2sub = table2.ix[table1.index]
    t2 = table2sub[['Blast hit','GO terms or Genbank IDs']]
    t3 = table1.join(t2)
    
    t3.to_csv(args.out[0],sep='\t',index=True)
    sys.exit()

if __name__=='__main__':
    main()