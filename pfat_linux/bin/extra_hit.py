#!/usr/bin/env python




import os
import re
import sys
import operator

x = open("../result/outfile",'r').readlines()

primary_match = "bla"

for i in xrange(len(x)):

	if re.search("^\s+\d+\s+QUERY_SEQ\s+\d+\.\d+", x[i]):

		sub = re.search("^\s+(\d+)\s+QUERY_SEQ\s+\d+\.\d+", x[i])

		node = sub.group(1)

		for j in xrange(len(x)):		


			if re.search("^\s+\d+\s+\S+\s+\d+\.\d+", x[j]) and not re.search("^\s+\d+\s+\d+\s+\d+\.\d+", x[j]) :		
				sub_j = re.search("^\s+(\d+)\s+(\S+)\s+\d+\.\d+", x[j])

				if operator.eq (node, sub_j.group(1)) and operator.ne ("QUERY_SEQ", sub_j.group(2)):
						
					primary_match = sub_j.group(2)

					print "##################"

					break

	if re.search("^\s+\d+\s+QUERY_SEQ\s+\d+\.\d+", x[i]):

		for j in xrange(i-1,0 ,-1):

			if re.search("^\s+\d+\s+\S+\s+\d+\.\d+", x[j]) and not re.search("^\s+\d+\s+\d+\s+\d+\.\d+", x[j]):		

#				print x[j]		

				sub_j = re.search("^\s+(\d+)\s+(\S+)\s+\d+\.\d+", x[j])
			
				primary_match = sub_j.group(2)

				break

				#if operator.eq (node, sub_j.group(1)) and operator.ne ("QUERY_SEQ", sub_j.group(2)):


					#primary_match = sub_j.group(2)

#				elif operator.eq (int(node)-1, int(sub_j.group(1))) and operator.ne ("QUERY_SEQ", sub_j.group(2)):

#					primary_match = sub_j.group(2)	


			


print primary_match+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"		

y = open("../source/protein_title_lib.txt",'r')


for line_y in y:

        if re.search(primary_match,line_y):


                sub = re.search("^\S+\t+(\S+)",line_y)

                os.system("curl 'http://www.genome.jp/dbget-bin/www_bget?uniprot:%s' > ../source/hit.html" %(sub.group(1)))

#                os.system("open ../source/hit.html")

z = open("../source/hit.html",'r').readlines()

out  =  open("../result/description.txt",'w')

group = []

for i in xrange(len(z)):
	print z[i]

        if re.search("\<\!\-\- bget\:db\:default \-\-\>\<\!\-\- uniprot\:", z[i]):

                group.append(i)

        if re.search("\<a href\=\"\/dbget-bin\/www_bget\?\-f\+uniprot", z[i]):

                group.append(i)



print group

if operator.eq(len(group),0):

	print >> out, "%s is the closest protein with the query protein sequence, howeverm its function is NOT fully documented!" %(primary_match)

else:


	print >> out, "%s is the closest protein with the query protein sequence, the function description about %s are listed as below:" %(primary_match, primary_match)

	for j in xrange(group[0], group[1]):

        	if re.search("\<a href\=.*\>.*\<\/a\>", z[j]):

                	sub = re.search("(.*)\<a href\=.*\>(.*)\<\/a\>(.*)", z[j])

                	print >> out, sub.group(1) + sub.group(2) + sub.group(3)

        	else:

                	print >> out, z[j],

out.close()



