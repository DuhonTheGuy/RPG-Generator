from text_reader import reader
import os
import sys

option = int(input("What do you want to do?\n1. List projects in current path\n2. Open path\n"))

# Lists projects, still a WIP
if option == 1:
	path = os.path.join(sys.path[0], "projects/")
	files = os.listdir(path)
	print(f"Current directory: {path}")
	print("---------------------------------------------------------------")
	print(", ".join(files))
# Asks for path
elif option == 2:
	path = input("Surely! What is the path?\n")
	reader.read(path)