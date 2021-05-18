#!/usr/bin/env python

import re
import sys
import operator

x = open(sys.argv[1],'r').readlines()

for i in xrange(len(x)):
	if operator.gt(len(x),i):
		if re.search("^>",x[i]) and re.search("^\w",x[i+1]):
			print x[i],x[i+1],
