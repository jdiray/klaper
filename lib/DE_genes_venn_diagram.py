"""
Charles Murphy
murphy.charlesj@gmail.com

Takes in three tables (output from $TRINITY_HOME/util/RSEM_util/merge_RSEM_frag_counts_single_table.pl)
    and finds intersection/unions of the gene lists.

"""


import argparse
import pandas
import sys
import pdb
import sets

def main():
    
    parser = argparse.ArgumentParser(description="Extract fasta file.")
    parser.add_argument('-table1',nargs=1,type=str,help="First table.")
    parser.add_argument('-table2',nargs=1,type=str,help="Second table.")
    parser.add_argument('-table3',nargs=1,type=str,help="Third table.")
    args = parser.parse_args()

    
    
    #load tables
    
    table1 = pandas.read_table(args.table1[0])
    table2 = pandas.read_table(args.table2[0])
    table3 = pandas.read_table(args.table3[0])
    #pdb.set_trace()
    
    
    print '\n' + args.table1[0] + '\n'
    print 'Number p-value <= 0.05: '+str(len(table1))
    print 'Number FDR <= 0.05: '+str(sum(table1.FDR<=0.05))+'\n'

    print '\n' + args.table2[0] + '\n'
    print 'Number p-value <= 0.05: '+str(len(table2))
    print 'Number FDR <= 0.05: '+str(sum(table2.FDR<=0.05))+'\n'
    
    print '\n' + args.table3[0] + '\n'
    print 'Number p-value <= 0.05: '+str(len(table3))
    print 'Number FDR <= 0.05: '+str(sum(table3.FDR<=0.05))+'\n'
    
    
    set1 = sets.Set(table1.index)
    set2 = sets.Set(table2.index)
    set3 = sets.Set(table3.index)
    
    print 'Overlapping statistics'+'\n'
    print 'Intersection (p-value<=0.05)'
    print args.table1[0] + ' and ' + args.table2[0] + ': \n' + str(len(set1.intersection(set2)))
    print args.table1[0] + ' and ' + args.table3[0] + ': \n' + str(len(set1.intersection(set3)))
    print args.table3[0] + ' and ' + args.table2[0] + ': \n' + str(len(set3.intersection(set2)))
    print args.table1[0] + ' and ' + args.table2[0] + ' and ' + args.table3[0] + ': \n' + str(len(set1.intersection(set3.intersection(set2))))
    
    table1sub = table1[table1.FDR<=0.05]
    table2sub = table2[table2.FDR<=0.05]
    table3sub = table3[table3.FDR<=0.05]
    
    set1 = sets.Set(table1sub.index)
    set2 = sets.Set(table2sub.index)
    set3 = sets.Set(table3sub.index)
    
    print '\n\nIntersection (FDR<=0.05)'
    print args.table1[0] + ' and ' + args.table2[0] + ': \n' + str(len(set1.intersection(set2)))
    print args.table1[0] + ' and ' + args.table3[0] + ': \n' + str(len(set1.intersection(set3)))
    print args.table3[0] + ' and ' + args.table2[0] + ': \n' + str(len(set3.intersection(set2)))
    print args.table1[0] + ' and ' + args.table2[0] + ' and ' + args.table3[0] + ': \n' + str(len(set1.intersection(set3.intersection(set2))))

    sys.exit()

if __name__=='__main__':
    main()