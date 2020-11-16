#!/usr/bin/python
#PrintHISATStats 11-2020
#Written by Joseph Sarro
#This script prints stats from hisat2 output
#files to be opened and written.  bi needs to be changed to match your output file before running as does datafile below.  
import os
bo= open('BamStats.txt','w')
print >> bo, "Total_ Input", "	", "Discordant_alignment", "	", "Discordant_alignment_percentage", "	", "Perfect_concordant_alignment","	","Perfect_concordant_alignent_percentage", "	","Multiple_concordant_alignment","	", "Multiple_concordant_alignemnt_percentage","	","Overall_alignment_percentage"
bi = open('hisatcastellino.o1509486', 'r')
#search through all lines of output file and find matching strings
for lines in bi:
	lines = lines.replace('\n','')
	fields = lines.split(" ")
	sq=fields[0]
	#total reads
	if "reads; of these:" in lines:
		num=fields[0] 
		print >> bo, "	", num,
	#discordant alignments
	elif ") aligned concordantly 0 times" in  lines:
		num=fields[4]
		percent =fields[5]
		print >> bo, "  ", num, "	",percent,
	#concoordant perfect alignments
	elif "aligned concordantly exactly 1 time" in lines:
		num=fields[4]
		percent =fields[5]
		print >> bo, "  ", num, "       ",percent,
	#concoordant miltiple alignments
	elif "aligned concordantly >1 times" in lines:
		num=fields[4]
		percent =fields[5]
		print >> bo, "  ", num, "       ",percent,
	#total alignment
	elif "overall alignment rate" in lines:
		percent=fields[0]
		print >> bo, percent
bi.close()

bo.close()
import sys
#remove ( ) characters and trailing characters
os.system("sed -i -e  's/(//g' BamStats.txt")
os.system("sed -i -e  's/)//g' BamStats.txt")
