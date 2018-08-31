# dc.py

import os
import math
from os import listdir
from os.path import isfile, join

#with open(fil) as f1:
#	read_data = f1.read()
#	f1.closed
#True

#print('The value of PI is approximately {0:5.20f}.'.format(math.pi))

#fil = "647640797.txt"
#print('output of file {0}'.format(fil))

cwd = os.getcwd()
print('Current Working Directory: {0}'.format(cwd))

mp3dir = r'c:\to_be_loaded'
outfil = r'C:\to_be_loaded\out.txt'
onlyfiles = [f for f in listdir(mp3dir) if isfile(join(mp3dir, f))]

with open(outfil, mode='wt', encoding='utf-8') as myfile:
	myfile.write('\n'.join(onlyfiles))


print('Files done')

input("press any key to exit")