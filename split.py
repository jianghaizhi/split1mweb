import csv
import os

nowdir = '/Users/tao/Desktop/jschrome'

csvFile = open("/Users/tao/Desktop/jschrome/20170920.csv", "r")
lines = csv.reader(csvFile)



urlnum = 1
filenum = 0
dirnum = 1

i = 1
while(i<11):
    commond = 'mkdir /Users/tao/Desktop/jschrome/site/' + str(i)
    i += 1
    os.system(commond)

for line in lines:

    if (urlnum % 1000 == 1 ):
        filenum += 1
        dirnum = 1 + ((filenum-1)/100)
        filedir = nowdir + '/site/' + str(dirnum) + '/' + str(filenum) + '.txt'
        f = open(filedir, 'w')


    #print line[0], line[1]
    f.write(line[0] + '    ' + line[1] + '\n')
    urlnum += 1

f.close()