#!/usr/bin/python
#PrintTrimData 11-2017
#Written by Joseph Sarro
#This script prints stats from timmomatic output
#files to be opened and written.  ti needs to be changed to match your output file before running as does datafile below.  
import os
ti = open('/afs/crc.nd.edu/user/j/jsarro/genomics/yoda/morales-jan-2016/trimandcutmorales.o742023', 'r')
to= open('Stats.txt','w')
print >> to, "Name", "	", "Input Reads", "	", "Surviving Reads", "	", "Surviving Percentage"
for lines in ti:
	lines = lines.replace('\n','')
	fields = lines.split(" ")
	sq=fields[0]
	if sq != "TrimmomaticPE:" and sq != "Multiple" and sq != "Using" and sq != "ILLUMINACLIP:" and sq !="Input":
		print >> to, sq, "	",
	elif sq == "Input":
		inputr = fields[3]
		surv = fields[6]
		survp=fields[7]
		print >> to, inputr, "	",surv, "	",survp
	#else:
	#	print >> to, "NOPE"
ti.close()
to.close()
import sys
os.system("sed -i -e  's/(//g' Stats.txt")
os.system("sed -i -e  's/)//g' Stats.txt")
