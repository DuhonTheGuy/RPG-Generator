import time

class reader:
	def read(path):
		with open(str(path), "r") as f:
			load = f.readlines()
		variables = {}
		for line in load:
			if line.startswith("-"):
				line = line[1:].replace("\n", "")
				print(line)
			elif line.startswith("#-"):
				line = line[2:].replace("\n", "")
				if str(line) not in variables:
					print(f"Error: Variable not found, '{line}'")
				else:
					print(f"{variables[str(line)]}")
			elif line.startswith("#"):
				line = line[1:].replace("\n", "")
				var = line.split("=")
				if var[1].startswith("+"):
					var[1] = input(var[1].replace("+", ""))
					variables[str(var[0])] = var[1]
				elif var[1].startswith("math."):
					var[1] = var[1].replace("math.", "")
					if "+" in var[1]:
						numbers = var[1].split("+")
						numbers = [int(i) for i in numbers]
						variables[str(var[0])] = sum(numbers)
			elif line.startswith("/"):
				line = line[1:].replace("\n", "")
				input(line)
