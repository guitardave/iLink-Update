# list.py
# 2/26 v1.2 DC added write list to file aka WriteToFile()
# 2/23 v1.1 DC added functions for AddBook(), ListBook() and Booklist() main
# 2/22 v1.0 DC created initial program (book database)

def AddBook(bList):
	uInput = raw_input("Enter the name of the book: \n")
	bList.append(uInput) # add the list item
	
def ListBook(bList):
	if not bList: # empty list
		print "The list is empty\n"
	else:
		for i in bList:
			print "%s\n" % i # prints the list

def WriteToFile(bList, f):
	file1 = open(f, "w")
	for b in bList:
		file1.write(b + "\n")
	file1.close()
	
	print "The list was saved\n"
	
def Booklist():
	booklist = []
	running = True

	while running == True: # run as long as this is True
		uInput = raw_input("Book List v1.2\nType\"add\" to add a book, \"list\" to list the books, \"clear\" to clear the list, \"save\" to save, or \"exit\" to exit the program\n")
		
		if uInput.lower() == "add":
			AddBook(booklist)
		
		elif uInput.lower() == "list":
			ListBook(booklist)
		
		elif uInput.lower() == "clear":
			booklist = []
		
		elif uInput.lower() == "save":
			# save the list to a file here
			outfil = "booklist.txt"
			WriteToFile(booklist, outfil)
			
		elif uInput.lower() == "exit":
			running = False
		
		else:
			print "The command was invalid\n"

# start main Booklist() program here
Booklist()