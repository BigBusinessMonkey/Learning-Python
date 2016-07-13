def userNameLang():
	print("Welcome. This is the first program, please remember to correctly capitalise when answering the following questions.")
	userName = input("Please enter your name: ")
	userLang = input("What is your preferred interface language?")

	if(userLang == "English"):
		greeting = "Hello "
	elif(userLang == "French"):
		greeting = "Bonjour "
	elif(userLang == "German"):
		greeting = "Guten Tag "
	else:
		greeting = "Welcome "

		
	if(userName == "Samuel" or userName == "Sam"):
		print("Welcome, Master!")
	else:
		print(greeting + userName + ".")

	if(greeting == "Welcome " and (userName != "Samuel" or userName != "Sam")):
		print("Sorry, but your chosen language was not recognised.")
		
userNameLang()