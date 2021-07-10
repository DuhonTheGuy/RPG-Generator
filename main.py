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


def menu_input(input_text:list, data_type:type) -> (str or int):
	"""
	For options selections catchs errors.
	Parameters :
	input_text (list) -- A string containing the text to display for the input prompt, or, a list displaying each input and then a line break.
	data_type (type) -- A data type to determine what kind of input to look for.
	Returns :
	option -> (int) -- The order value of the setting selected. (Only returned if data_type = 'int')
	option -> (str) -- The string the user selected. (Only returned if data_type = 'str')
	"""
	for element in input_text:
		print(element)

	while True:
		try:
			if data_type == int:
				option = int(input())
			elif data_type == str:
				option = str(input())
			else:
				raise TypeError('Invalid type must be string containing either int or str.')
			return option
		
		except ValueError:
			print('Please select a valid option.')
			continue


# Function to allow backtracking to the menu after a cancelled "from path".
def start_menu() -> None:
	"""
	The main loop of the program.
	Parameters :
	None
	Returns :
	None
	"""
	# Main loop for start menu
	while True:
		prompt = ['What do you want to do?', '1. List projects in current path', '2. Open path', '3. Exit']
		option = menu_input(prompt, int)

		reader = Reader()

		# Lists projects in current path.  (still a WIP)  # TODO : Finish this.
		if option == 1:
			path = os.path.join(sys.path[0], 'projects/')
			files = os.listdir(path)

			print(f'Current directory: {path}')
			print('---------------------------------------------------------------')

			for count, file in enumerate(files):
				print(f"{count + 1}. {file}")
			
			prompt = ['Which one do you want to access?']
			a = menu_input(prompt, int)
			print(files)

			result = path + files[a - 1]
			reader.read(result)
		
		# Opens specific file path.
		elif option == 2:
			# Asks the users for file path and checks if file path exsists.
			while True:
				prompt = ['Surely! What is the path?']
				path = menu_input(prompt, str)
			
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
						option = menu_input(['Try again? (1. No / 2. Yes)'], int)
						# If the user inputted a selection that was offered.
						if option == 1 or option == 2:
							break

						# If the user inputted a number that is not 1 or 2.
						else:
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
			return None
		
		# Loops through the program again.
		else:
			# Repeats the menu loop again.
			print("That's an invalid option!\n") # Unnecessary formatting choice.
			continue


if __name__ == '__main__':
	start_menu()