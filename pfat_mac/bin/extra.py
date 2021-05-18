#!/usr/bin/env python

import re
import sys

inputfile_1 = sys.argv[1]

def dictionary (inputfile):

	genes = {}

	last_gene = ""

	for line in open(inputfile, "r"):
		if not re.search("^$",line) and not re.search("\#",line):
			l = line.rstrip()

			if not re.search("^Query\:",l): #and not re.search("!",l):
#				print l
				genes[last_gene].append(l)
		#	if re.search("^Query\:",l):
			elif re.search("^Query\:",l):
#				print l
				sub = re.search("^Query:\s+(.*)\s+\[.*$",l)
				c = sub.group(1)
				#print c
				last_gene = c
#				print last_gene

				if not genes.has_key(c):
					genes[c] = []
			else:
				continue

	return genes

if __name__=='__main__': 

	for element in dictionary(inputfile_1).iterkeys():	
		#print element
		for r in dictionary(inputfile_1)[element]:
		
		#	print r
			if re.search("^\>\>",r):
				print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
				print element		
				for r in dictionary(inputfile_1)[element]:
					print r
				break
