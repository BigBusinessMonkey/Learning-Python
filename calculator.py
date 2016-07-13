#Returns product of num2 added to num1
def add(num1, num2):
	return num1 + num2

#Returns product of num2 subracted from num1
def subtract(num1, num2):
	return num1 - num2

#Returns product of num1 multiplied by num2
def multiply(num1, num2):
	return num1 * num2
	
#Returns product of num1 divided by num2
def divide(num1, num2):
	return num1 / num2

	
def calcUI():
	operation = input("Which operation would you like to use? (+,-,*,/, or type 'quit' to end program.)")
	if(operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "quit"):
		print("This is an exceedingly simple program. Please input a recognised operation.")
		calcUI()
	elif(operation == "quit"):
		print("Ending program.")
	else:
		var1 = int(input("Please input first number:"))
		var2 = int(input("Please input second number:"))
		if(operation == "+"):
			print(add(var1, var2))
		elif(operation == "-"):
			print(subtract(var1, var2))
		elif(operation == "*"):
			print(multiply(var1, var2))
		elif(operation == "/"):
			print(divide(var1, var2))
	

	
	
calcUI()