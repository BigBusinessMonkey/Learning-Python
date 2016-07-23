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

#Returns num1 to the power of num2
def power(num1, num2):
	return num1 ** num2
    
#Returns num factorial
def factorial(x):
    FACT = 1
    for i in range(x):
        i += 1
        FACT *= i
    return FACT
    

        
        
def calcUI():
	operation = input("Which operation would you like to use? (+,-,*,/,^)")
	if(operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "quit"):
		print("This is an exceedingly simple program. Please input a recognised operation.")
		calcUI()
	elif(operation == "quit"):
		print("Goodbye!")
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
		elif(operation == "^" or operation == "**"):
			print(power(var1, var2))
	

def calcAdv():
    print("Welcome to this simplistic calculator. Enter 'quit' at any time to exit the program.")
    branch = input("Would you like to perform a binary operation? (y/n)")
    if(branch == "y"):
        calcUI()
    elif(branch == "n"):
        singleOP = input("Would you like to explore functions that operate on a single value?")
        if(singleOP == "y"):
            print("Factorial currently only available operation.")
            var3 = input("Please input your number: (int only) ")
            print(factorial(var3))
            #Currently breaks if you input floats, words, etc. but if using 'type(var3) == int' things also break, because even numerical inputs are still strings.
            elif(singleOP == "n"):
            print("It is not within my power to help you. Goodbye.")
        else:
            print("Please input a valid response")
            calcAdv()
    elif(branch == "quit"):
        print("Goodbye!")
    else:
        print("Please input a valid response.")
        calcAdv()
            
calcAdv()