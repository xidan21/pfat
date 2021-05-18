#!/usr/bin/env python

# NOTE: the motif sequence are the part of protein seqeunce

import re
import operator
import sys

def creating (x,para_1,para_2,para_3):	# creating a dictionary where key is the protein id and values are the motif sequences coordinate. 
    
    protein = {}
    last_protein = ""
    
    for i in xrange(len(x)):
    
        x[i]=x[i].rstrip()
    
        if re.search(para_1,x[i]):
	    sub = re.search ("(\d+)\s+(\d+)\s+[\[\.][\.\]]\s+\d+\s+\d+\s+[\[\.][\.\]]\s+\d+\.\d+$", x[i])

	    bla = []; bla.append(int(sub.group(1))-1); bla.append(int(sub.group(2))-1)
            protein[last_protein].append(bla)	 # get the line descibing the motif seqeunces coordinate
        elif x[i].startswith(para_2):	# detect the line describing the protein id

            sub = re.search("(\S+_\S+)\s+\(",x[i][para_3:])
	    protein_title = sub.group(1)	 # delete ">> " and get protein id
            last_protein = protein_title	 # get protein id

            if not protein.has_key(protein_title):
                protein[protein_title] = []            
            else:
                continue    
    return protein


def creating_seq (x,para_1,para_2):

	seq = {}
	last_seq = ""

	for i in xrange(len(x)):

		x[i]=x[i].rstrip()











		if re.search(para_1, x[i]):

			seq[last_seq].append(x[i].rstrip())
			
		elif x[i].startswith(para_2):
			sub = re.search("^>(\S+)\s+\(",x[i])
			seq_title = sub.group(1)
			last_seq = seq_title

			if not seq.has_key(seq_title):
				seq[seq_title] = []
			else:

				continue
	return seq



if __name__=='__main__':

	inputfile_1 = sys.argv[1] #"/Users/xidanli/Desktop/phylogeny_project/ppr.txt"
	inputfile_2 = sys.argv[2] #"/Users/xidanli/Desktop/phylogeny_project/ppr_formatted_uniq.fasta"

	x = open (inputfile_1,'r').readlines()
	y = open (inputfile_2,'r').readlines()

	start = 0
	end = 0 


	out = open("../source/protein_title_lib.txt",'w')

	#print creating(x,"^\s+\d+\s+[!?]",">>",3)        
	#print creating_seq(y, "^\w+", ">")

	
	#for protein_id in creating(x,"^\s+\d+\s+[!?]",">>",3).iterkeys(): 	# creating a dictionary where key is the protein id and values 
	protein = creating(x,"^\s+\d+\s+[!?]",">>",3)	
	seq = creating_seq(y,"^\w+",">")
	for protein_id in seq.iterkeys(): 	# creating a dictionary where key is the protein id and values 
		
		#print seq.get(protein_id)
		#print protein_id
		
		#print protein.get(protein_id)

		result = list(''.join(seq.get(protein_id)))
		#print ''.join(seq.get(protein_id))
		for start,end in protein.get(protein_id):
			result[start:end] = ["N"]*(end-start)

		result = ''.join(result)
		print ">"+protein_id
		print result







