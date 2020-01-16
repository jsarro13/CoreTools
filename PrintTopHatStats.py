#!/usr/bin/python
#PrintBamStats 11-2017
#Written by Joseph Sarro
#This script prints stats from TopHat output
#files to be opened and written.  bi needs to be changed to match your output file before running as does datafile below.  
import os
bo= open('BamStats.txt','w')
print >> bo, "Total Forward Input", "	", "Forward Mapped", "	", "Forward Mapped Percent", "	", "Total Reverse Input","	","Reverse Mapped", "	","Reverse Mapped Percent","	", "Overall Mapping Percent","	","Aligned Pairs","	","Concordant Pair Percent"
SampleList=["Dsuz_G_female3_S1","Dsuz_G_female4_S2", "Dsuz_G_female5_S3"]
for i in SampleList:
	current=i
	#print current
	bi = open('/afs/crc.nd.edu/user/j/jsarro/genomics/yoda/Syed-Hickner-RNASeq-Dmel-06-2017/trimmed-suz/bam/%s/align_summary.txt' % current, 'r')
	#print >> to, "Name", "	", "Input Reads", "	", "Surviving Reads", "	", "Surviving Percentage"
	print >> bo, current,
	for lines in bi:
		lines = lines.replace('\n','')
		fields = lines.split(" ")
		#print fields
		sq=fields[0]
		if "Input" in fields:
			num=fields[17] 
			print >> bo, "	", num,
		elif "Mapped" in  fields:
			num=fields[16]
			percent =fields[17]
			print >> bo, "  ", num, "	",percent,
		elif "overall" in fields and "mapping" in fields:
                        print >> bo, "  ", sq,
		elif "concordant" in fields:
                        print >> bo, "  ", sq
	bi.close()

bo.close()
import sys
#remove ( ) characters and trailing characters
os.system("sed -i -e  's/(//g' BamStats.txt")
os.system("sed -i -e  's/)//g' BamStats.txt")
