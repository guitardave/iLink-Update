# bookkeeper.py

class book(object):
	def __init__(self, title, author):
		self.title = title
		self.author = author
		
def addBook(bookList):
	title = raw_input("What is the name of the book? ")
	author = raw_input("What is the author's name? ")
	bookList.append(book(title.upper(), author.title()))
	
def listBook(bookList):
	for i in bookList:
		print "\"%s\", by %s\n" % (i.title, i.author)
		
def readBooks(bookList):
	bList = []
	f = open(raw_input(" Enter the filename. "))
	for line in f:
		comma = line.find(",")
		title = line[0:comma].rstrip(',') # get book title preceding comma
		author = line[comma+1:].strip() # get author name after comma
		
		bList.append(book(title.upper(), author.title()))
		print "%s, %s" % (title.upper(), author.title())
		
	userInput = raw_input("Would you like to add these items to your temp list? ")
	if userInput == "yes":
		for i in bList:
			bookList.append(i)
			print "Saved"
	else:
		print "Not saved"
	f.close()
		
def writeToNew(bookList):
	userInput = raw_input(" Enter the filename you'd like to export to ")
	f = open(userInput, 'w')
	for i in bookList:
		f.write("%s, %s\n" % (i.title.upper(), i.author.title()))
		
def writeToExisting(bookList):
	userInput = raw_input("Enter the filename you'd like to add to. ")
	f = open(userInput, 'a')
	for i in bookList:
		f.write("%s, %s\n" % (i.title.upper(), i.author.title()))
	f.close()
	
def banner():
	print "*** Welcome to BOOKKEEPER ***. Type:"
	print "\t\"ADD\" to add a book to your temp list"
	print "\t\"LIST\" to read out of your temp list"
	print "\t\"READ\" to read an existing file"
	print "\t\"SAVE\" to save to a new file"
	print "\t\"SAVE EXISTING\" to save an existing file"
	print "\t\"CLEAR\" to clear your temp list"
	print "\t\"EXIT\" to exit"
	
		
bookList = []
running = True

while running == True:
	banner() # display list of commands
	userInput = raw_input()
	
	if userInput.lower() == "add":
		addBook(bookList)
	elif userInput.lower() == "list":
		listBook(bookList)
	elif userInput.lower() == "read":
		readBooks(bookList)
	elif userInput.lower() == "save":
		writeToNew(bookList)
	elif userInput.lower() == "save existing":
		writeToExisting(bookList)
	elif userInput.lower() == "clear":
		bookList = []
	elif userInput.lower() == "exit":
		running = False
	else:
		print "Invalid command\n\n"
	
	