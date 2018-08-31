# hoff wedding files

from os import listdir
from os.path import isfile, join

dir = r"R:\Alan Wedding"
out = r"c:\users\david\documents\hoff.txt"
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

with open(out, "a") as myfile:
	myfile.write('\nhttps://www.onholdwizard.com/Hoff/'.join(onlyfiles))

print("done")