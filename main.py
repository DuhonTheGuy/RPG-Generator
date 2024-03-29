from functools import reduce
from text_reader import reader
import os
import sys

# Function to allow backtracking to the menu after a cancelled "from path".
def startMenu():
	option = int(input("What do you want to do?\n1. List projects in current path\n2. Open path\n3. Exit\n"))
	Reader = reader()

	if option == 1:
		path = os.path.join(sys.path[0], "projects\\")

		files = os.listdir(path)
		print(f"Current directory: {path}")
		print("---------------------------------------------------------------")
		for count, file in enumerate(files):
			ext = file.split(".")[1]
			if ext == "start":
				pass
			print(f"{count + 1}. {file}")
		a = int(input("Which one do you want to access? "))
		result = path + files[a - 1]
		startFile = result[:-3:] + "start"
		Reader.read(result, startFile)
	# Asks for path
	elif option == 2:
		# Check if specified path exists.
		pathChecking = True
		# While a valid path is not provided, ask until one is or the user cancels the operation.
		while pathChecking:
			path = input("Surely! What is the path?\n")
			if os.path.exists(path):
				#reader.read(path)
				# End the checking loop.
				pathChecking = False
				Reader.read(path)
			else:
				print("No such path exists!")
				option = input("Try again? (1. No / 2. Yes)\n")
				try:
					option = int(option)
				except:
					option = 1
				if option == 1:
					# End the checking loop.
					pathChecking = False
					print("\n") # Unnecessary formatting choice.
					startMenu()
	# Exits.
	elif option == 3:
		exit()
	else:
		print("That's an invalid option!\n") # Unnecessary formatting choice.
		startMenu()

startMenu()