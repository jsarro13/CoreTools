#!/usr/bin/python
#PrintCountStats 11-2020
#Written by Joseph Sarro
#This script prints total number of counts, counts to genes, and percentage counts to genes in a file ouput from htseq-count
#files to be opened and written.  Samplelist contains a comma seperated list of your .out files.  
import os
co= open('CountStats.txt','w')
print >> co, "Sample", "	", "Total_Counts", "	", "Gene_Counts", "	", "%Surviving"
SampleList=["delta_srtA-log-1_S7.gtf.out","delta_srtA-log-2_S8.gtf.out","delta_srtA-log-3_S9.gtf.out","delta_srtA-stationary-1_S10.gtf.out","delta_srtA-stationary-2_S11.gtf.out","delta_srtA-stationary-3_S12.gtf.out","Splus-log-1_S1.gtf.out","Splus-log-2_S2.gtf.out","Splus-log-3_S3.gtf.out","Splus-stationary-1_S4.gtf.out","Splus-stationary-2_S5.gtf.out","Splus-stationary-3_S6.gtf.out","delta_srtA-log-1_S7.gff.out","delta_srtA-log-2_S8.gff.out","delta_srtA-log-3_S9.gff.out","delta_srtA-stationary-1_S10.gff.out","delta_srtA-stationary-2_S11.gff.out","delta_srtA-stationary-3_S12.gff.out","Splus-log-1_S1.gff.out","Splus-log-2_S2.gff.out","Splus-log-3_S3.gff.out","Splus-stationary-1_S4.gff.out","Splus-stationary-2_S5.gff.out","Splus-stationary-3_S6.gff.out"]
for i in SampleList:
	#open file an get line counts
	ci = open(i, 'r')
	linecount = len(open(i).readlines(  ))
	#print (linecount)
	totalcount=0
	genecount=0
	linenum=0
	#for each line in the file add count to total count
        for lines in ci:
                linenum +=1
                fields = lines.split("	")
                totalcount=totalcount + int(fields[1])
		#add counts to gene count up until the last 5 lines
		if (linenum <=linecount-5):
                	genecount=genecount + int(fields[1])
	#print(totalcount)
	#print(genecount)
	#print (float(int(genecount)/int(totalcount)))
	print >> co, i,"	",totalcount,"	",genecount,"	",float(float(genecount)/float(totalcount))*100	
co.close()
