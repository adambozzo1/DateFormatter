
#!/usr/bin/python

import sys

fileName = sys.argv
file = open(str(fileName[1]), "w+")
file.write("heyyy")
file.close()