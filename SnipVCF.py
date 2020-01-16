#!/usr/bin/python
import os
samplename ='merged'#################
f = open(samplename+".vcf", 'r')
o= open(samplename+'.VCFparse.txt','w')
contigcount=0
passcount=0
distance=0
####dont forget to change this
samplenum=4 ################
print >> o, "Contig     Pos     Distance	Ref     Alt     Qaul    Zygosity"
for lines in f:
	fields = lines.split("	")
	contig=fields[0]
	#datafile = file('Cumulative_Bait_Info.txt')
	#for line in datafile:
		#print line			
		#if contig in line:
	pos=fields[1]
	ref=fields[3]
	alt=fields[4]
	qual=fields[5]
	zyg=fields[9]
	contigcount+=1
	#hit=line.split("	")
	#hitstart=hit[1]
	#hitend=hit[2]
	if float(qual) >= 30:
		passcount +=1
		#if int(pos) < int(hitstart):
		#	dis=(int(hitstart)-int(pos))
		#	distance="-"+str(dis)
		#elif int(pos) >= int(hitstart):
		#	dis=(int(pos)-int(hitstart))
		#	distance="+"+str(dis)
		print >> o, contig,"	",pos,"	",ref,"	",alt,"	",qual,"	",
		curcount=0
		while int(curcount) < int(samplenum):
			curcount +=1
			place=(8+int(curcount))	
			zygs=fields[int(place)]
			#if zygs is not ".":
			zygsplit=zygs.split(":")
			zygs=zygsplit[0]
			#else:
			#	zygs="NOHIT"	
			#print zygs	
			if int(curcount) < int(samplenum):
				print >> o,zygs,"	",
			elif int(curcount) == int(samplenum):
				print >> o,zygs
f.close()
o.close()
print contigcount
print passcount
os.system("sed -i -e  '/^$\|0 ( 0)/d' "+samplename+".VCFparse.txt") 
