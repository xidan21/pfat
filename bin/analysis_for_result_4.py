#!/usr/bin/env python

import re
import operator
import sys
#import for_result_5 as f2py # for calculating the evolutionary distance between two genes

index = 0
def inputting (file_name): # read and convert result_4.txt to a two-dimension array

    x = open (file_name,'r').readlines()# reading result_4.txt which is a matrix-like file
    array = []
    global index
    for i in xrange(len(x)):
        x_array =  x[i].split() # split the each line to become an array 
#        print x_array[0],">>>>>>>>>>>>>>>>>>>>>>"
 #       print len(x_array)
	if not operator.eq (len(x_array),1):
            index += 1
            array.append (x_array) # convert the whole to a two-dimension array
    return array

def calculating(r1,r2,r3):
	distance = 0
	if operator.eq(r1,0) and operator.eq(r2,0) and operator.eq(r3,0):
            distance = 0
        else:
            distance = 1- (r3/((r1+r2)/2))

	return distance
	
def cal(array):
    print index
    for i in xrange(len(array)):
        print array[i][0].lstrip(">>"),
        for k in xrange(len(array)):
            count = 0
            for j in xrange(1,len(array[i])):# remove the gene_title
                      
                for l in xrange(1,len(array[k])):
           
                    if operator.eq(array[i][j],array[k][l]):
               
                        count += 1 # count the shared hits between two genes
                       
            length_1 = float(len(array[i])-1) # count the number of hits of each gene
            length_2 = float(len(array[k])-1)
            
            result = calculating(length_1,length_2,count) # calculating the distance between two genes
            print "%f" %(result),
        print

if __name__=='__main__':
    cal(inputting(sys.argv[1]))
