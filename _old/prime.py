# prime numbers

running = True

while running == True:
	uI = raw_input("Please enter a number or type q to quit\n")
	if uI.isdigit():
		file1 = open("prime.txt", "w")
		for n in range(2, int(uI)):
			for x in range(2, n):
				if n % x == 0:
					print n, 'equals', x, '*', n/x
					break
			else:
				print n, ' is a prime number'
				file1.write("%d is a prime number\n" % n)
		file1.close()
				
	elif uI.lower() == "q" or uI.lower() == "quit":
		running = False
	else:
		print "invalid input"