# dc2.py

username = "dave"
uInput = raw_input("Please enter username ")
if str(uInput) == username:
	print "Welcome %s" % username
else:
	print "Incorrect username"

input("Press any key to continue")