# myaudio.py
from os import listdir
from os.path import isfile, join
import wave

mydir = r"c:\to_be_loaded"
myfiles = [f for f in listdir(mydir) if (isfile(join(mydir, f)) and "X" in str(join(mydir, f)) and "pkf" not in str(join(mydir, f)))]
outfil = r'C:\to_be_loaded\out.txt'
i = 0
try:
	for a in myfiles:
		"""
		wav = wave.open(a, "r")
		chan = wav.getnchannels()
		samp = wav.getframerate()
		wav.close()
		print("%s has %d channels and is %s Hz\n" % (a, chan, samp))
		"""
		i += 1
	with open(outfil, mode='wt') as myfile:
		myfile.write('\n'.join(myfiles))
			
	print("done. %s files" % i)
except wave.Error as err:
	print("wave.Error: {0}".format(err))
except IOError as err:
	print("IOError: {0}".format(err))
