"""
Main file for python program.

Constants :
None

Classes :
None

Functions :
start_menu -> (None) -- Runs the start menu, which returns None.

Dependencies :
os (default) -- For managing file paths.
sys (default) -- For managing file paths.
functools.reduce (default) -- Not in use?
text_reader.Reader (local) -- For interpreting text files.
"""
# Default Dependencies
from functools import reduce	# TODO : Not sure why this is here
import os
import sys

# Exsternal Dependencies
None

# Local Dependencies
from text_reader import Reader

# Function to allow backtracking to the menu after a cancelled "from path".
def start_menu() -> None:
	"""
	Runs the start menu

	Parameters :
	None

	Returns :
	None
	"""
	# Main loop for start menu
	while True:
		# Option loop for menu selection
		while True:
			try:
				option = int(input("What do you want to do?\n1. List projects in current path\n2. Open path\n3. Exit\n"))
				break
			except ValueError:
				print('Please select a valid option')
				continue
		
		reader = Reader()

		# Lists projects in current path.  (still a WIP)  # TODO : Finish this.
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
			reader.read(result)
		
		# Opens specific file path.
		elif option == 2:
			# Asks the users for file path and checks if file path exsists.
			while True:
				try:
					path = input('Surely! What is the path?\n')
				
				except ValueError or TypeError:
					print('Please input file path in a valid format.')
					continue
				
				# If the path is real.
				if os.path.exsits(path):
					# Read the path then break out of the loop.
					reader.read(path)
					break
				
				# If no path exsists.
				else:
					print('No such path exists!')

					# Loop for asking if the user wishes to input a new file path.
					while True:
						try:
							option = int(input('Try again? (1. No / 2. Yes)\n'))
							if option == 1 or option == 2:
								break

							# If the user inputted a number that is not 1 or 2.
							else:
								print('Please enter a valid option.')
								continue
						
						# If the value is not an int.
						except ValueError:
							print('Please enter a valid option.')
							continue
					
					# Try Again?, No. break the loop.
					if option == 1:
						break
					
					# Try Again?, Yes. continue the loop.
					if option == 2:
						continue
		
		# Stops the program.
		elif option == 3:
			# returns which closes the program
			return
		
		# Loops through the program again.
		else:
			# Repeats the menu loop again.
			print("That's an invalid option!\n") # Unnecessary formatting choice.
			continue


if __name__ == '__main__':
	start_menu()