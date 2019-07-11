
#program to correct date format for json files in order to import into robo3t

import sys
import re 

fileName = sys.argv
fileR = open(str(fileName[1]), "r")
newlines = ""
for line in fileR:
    newlines += re.sub("(\+0000+)", "", line)

fileR.close()
fileW = open("results.txt", "w+")
fileW.write(newlines)
fileW.close()
