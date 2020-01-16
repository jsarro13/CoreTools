#!/usr/bin/python
#PrintBamStats 11-2017
#Written by Joseph Sarro
#This script prints stats from Samtools BamStats output
#files to be opened and written.  bi needs to be changed to match your output file before running as does datafile below.  
import os
bo= open('BamStats.txt','w')
print >> bo, "Name", "	", "Input Reads", "	", "Mapped Reads", "	", "Percent Mapped","	","Paired Reads", "	","Percent Paired"
SampleList=["Bob-R30-1-nob_S4_stats","Bob-R30-1-no_S3_stats","Bob-R30-1_S2_stats","Bob-WT-R_S1_stats"]
for i in SampleList:
	current=i
	#print current
	bi = open('/afs/crc.nd.edu/user/j/jsarro/genomics/yoda/morales-jan-2016/trimmed/sam/bamstats/%s.txt' % current, 'r')
	#print >> to, "Name", "	", "Input Reads", "	", "Surviving Reads", "	", "Surviving Percentage"
	print >> bo, current,
	for lines in bi:
		lines = lines.replace('\n','')
		fields = lines.split(" ")
		#print fields
		sq=fields[0]
		if "(QC-passed" in fields: 
			print >> bo, "	", sq,
		elif "mapped" in fields and "mate" not in fields:
			percent =fields[4]
			print >> bo, "  ", sq, "	",percent,
		elif "properly" in fields and "paired" in fields:
			percent=fields[5]
                        print >> bo, "  ", sq, "        ",percent
	bi.close()

bo.close()
import sys
#remove ( ) characters and trailing characters
os.system("sed -i -e  's/(//g' BamStats.txt")
os.system("sed -i -e  's/)//g' BamStats.txt")
os.system('sed -i -e  "s/:-nan%//g" BamStats.txt')
