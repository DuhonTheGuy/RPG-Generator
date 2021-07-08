from functools import reduce
from text_reader import Reader
import os
import sys

# Function to allow backtracking to the menu after a cancelled "from path".
def start_menu():
	while True:
		try:
			option = int(input("What do you want to do?\n1. List projects in current path\n2. Open path\n3. Exit\n"))
			break
		except ValueError:
			print('Please select a valid option')
			continue
	
	reader = Reader()

	# Lists projects in current path.  (still a WIP)
	if option == 1:
		path = os.path.join(sys.path[0], "projects\\")

		files = os.listdir(path)
		print(f"Current directory: {path}")
		print("---------------------------------------------------------------")
		for count, file in enumerate(files):
			print(f"{count + 1}. {file}")
		a = int(input("Which one do you want to access? "))
		print(files)
		result = path + files[a - 1]
		#reader.read(result)
		reader.read(result)
	
	# Opens specific file path.
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
				reader.read(path)
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
					start_menu()
	
	# Stops the program.
	elif option == 3:
		exit()
	
	# Loops through the program again.
	else:
		print("That's an invalid option!\n") # Unnecessary formatting choice.
		start_menu()	# TODO : Not the best way todo this should be looping the entire thing.


if __name__ == '__main__':
	start_menu()