#!/bin/sh
#this script requires the number of samples as an input parameter 
#Joe Sarro
#echo "$1"
#print column names
#echo -e Sample_Name'\t'Barcode'\t'Total_Num_Reads'\t'Percent_of_Lane'\t'Percent_Perfect_Barcode'\t'Percent_One_Missmatch_Barcode'\t'Yield'\('mbases'\)''\t'PF_Clusters'\t'Q30_Bases'\t'Mean_Quality_Score
#echo -e Sample'\t'Barcode Sequence'\t'PF Clusters'\t'% Of The Lane'\t'% Perfect Barcode'\t'Yield'('mbases')''\t''% >= 'Q30'\t'Mean_Quality_Score
samples=$(($1+1))
#echo $samples
#c=40
#parse the html file
cat laneBarcode.html | tr "\n" "|" | grep -o '<td>.*</td>' | sed 's/\(<td>\|<\/td>\)//g' | sed 's/\(<p align="right">\|<\/p>\)//g' | sed 's/\(<a href="..\/..\/..\/..\/\|\/all\/all\/all\/lane.html">hide barcodes<\/a>\)//g'  | sed 's/|/\n/g' > NEWFILE
cat NEWFILE | tr "\n" "|" | grep -o '.*,.*' | sed 's/,//g' | sed 's/|/\n/g' > NEWFILE2
cat NEWFILE2 | tr "\n" "|" | grep -o '.*' | sed 's/<td style="font-style:italic">unknown/NA/g' | sed 's/|/\n/g' > NEWFILE3
#print flowcell ID flowcell summary stats and header
echo -e Flow Cell ID
more NEWFILE3 |awk 'FNR=='5' {print $0}'
echo -e Clusters'('Raw')''\t'Clusters'('PF')''\t'Yield'('MBases')'
clustraw=$(more NEWFILE3 |awk 'FNR=='15' {print $0}')
clustpf=$(more NEWFILE3 |awk 'FNR=='16' {print $0}')
yieldmb=$(more NEWFILE3 |awk 'FNR=='17' {print $0}')
echo -e $clustraw'\t'$clustpf'\t'$yieldmb
echo -e Sample'\t'Barcode Sequence'\t'PF Clusters'\t'% Of The Lane'\t'% Perfect Barcode'\t'Yield'('mbases')''\t''% >= 'Q30'\t'Mean_Quality_Score
#starting line for each field
startline=39
seqline=40
readline=41
laneperline=42
perfectbcperline=43
missmatchperline=44
yieldline=45
pfperline=46
q30perline=47
meanqualityline=48
#for each sample
for (( i=1; i <= $samples; ++i ))
do
readnum=0
lanepernum=0
perfectbcpernum=0
missmatchpernum=0
yieldnum=0
pfpernum=0
q30pernum=0
meanqualitynum=0
#echo $i 
name=$(more NEWFILE3 |awk 'FNR=='$startline' {print $0}')
seq=$(more NEWFILE3 |awk 'FNR=='$seqline' {print $0}')
#echo -e  $test'\t'$test
#for each lane
for  (( j=1; j <= 4; ++j ))
do
#echo $readnum
#echo $readline2
if [ $j == "1" ]
then
#set line for first value
readline2=$readline
laneperline2=$laneperline
perfectbcperline2=$perfectbcperline
#missmatchperline2=$missmatchperline
yieldline2=$yieldline
pfperline2=$pfperline
q30perline2=$q30perline
meanqualityline2=$meanqualityline
else
#set lines for all other values
readline2=$(($readline2 + (14*($1+1))))
laneperline2=$(($laneperline2 + (14*($1+1))))
perfectbcperline2=$(($perfectbcperline2 + (14*($1+1))))
#missmatchperline2=$(($missmatchperline2 + (14*($1+1))))
yieldline2=$(($yieldline2 + (14*($1+1))))
pfperline2=$(($pfperline2 + (14*($1+1))))
q30perline2=$(($q30perline2 + (14*($1+1))))
meanqualityline2=$(($meanqualityline2 + (14*($1+1))))
fi
# read numbers of values in file
curreadnum=$(more NEWFILE3 |awk 'FNR=='$readline2' {print $0}')
readnum=$(($readnum+$curreadnum))
curlanepernum=$(more NEWFILE3 |awk 'FNR=='$laneperline2' {print $0}')
curperfectbcpernum=$(more NEWFILE3 |awk 'FNR=='$perfectbcperline2' {print $0}')
#curmissmatchpernum=$(more NEWFILE3 |awk 'FNR=='$missmatchperline2' {print $0}')
curyieldnum=$(more NEWFILE3 |awk 'FNR=='$yieldline2' {print $0}')
curpfpernum=$(more NEWFILE3 |awk 'FNR=='$pfperline2' {print $0}')
curq30pernum=$(more NEWFILE3 |awk 'FNR=='$q30perline2' {print $0}')
curmeanqualitynum=$(more NEWFILE3 |awk 'FNR=='$meanqualityline2' {print $0}')
lanepernum=`echo "scale = 20; $lanepernum + $curlanepernum" | bc`
perfectbcpernum=`echo "scale = 20; $perfectbcpernum+$curperfectbcpernum" | bc`
#missmatchpernum=`echo "scale = 20; $missmatchpernum+$curmissmatchpernum" | bc`
yieldnum=`echo "scale = 20; $yieldnum+$curyieldnum" | bc`
pfpernum=`echo "scale = 20; $pfpernum+$curpfpernum" | bc`
q30pernum=`echo "scale = 20; $q30pernum+$curq30pernum" | bc`
meanqualitynum=`echo "scale = 20; $meanqualitynum+$curmeanqualitynum" | bc`
#echo $curreadnum
#echo $readnum
#echo "$currentline"
c=$(($c + 1))
#echo $c
done
#generate averages by four lanes and print results
lanepernum=`echo " scale = 4; $lanepernum / 4" | bc`
perfectbcpernum=`echo " scale = 4; $perfectbcpernum / 4" | bc` 
#missmatchpernum=`echo " scale = 4; $missmatchpernum / 4" | bc`
yieldnum=`echo " scale = 4; $yieldnum / 4" | bc`
pfpernum=`echo " scale = 4; $pfpernum / 4" | bc`
q30pernum=`echo " scale = 4; $q30pernum / 4" | bc`
meanqualitynum=`echo " scale = 4; $meanqualitynum / 4" | bc`
#echo -e $name'\t'$seq'\t'$readnum'\t'$lanepernum'\t'$perfectbcpernum'\t'$missmatchpernum'\t'$yieldnum'\t'$pfpernum'\t'$q30pernum'\t'$meanqualitynum
echo -e $name'\t'$seq'\t'$readnum'\t'$lanepernum'\t'$perfectbcpernum'\t'$yieldnum'\t'$q30pernum'\t'$meanqualitynum
#echo $startline
startline=$(($startline+14))
seqline=$(($seqline+14))
readline=$(($readline+14))
laneperline=$(($laneperline+14))
perfectbcperline=$(($perfectbcperline+14))
#missmatchperline=$(($missmatchperline+14))
yieldline=$(($yieldline+14))
pfperline=$(($pfperline+14))
q30perline=$(($q30perline+14))
meanqualityline=$(($meanqualityline+14))
done
#remove parsed htmlfiles
rm NEWFILE
rm NEWFILE2
rm NEWFILE3
