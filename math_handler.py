class Handler:

	def handle(args):
		operator_list = ["+", "-", "*", "/"]
		current_operators = []
		for i in operator_list:
			if i not in args:
				return "Error: Invalid Operator"
			else:
				current_operators.append(i)
				print(i)
			print(args)
			print(current_operators)

# =================================================================================

	# def add(self, args):
		
