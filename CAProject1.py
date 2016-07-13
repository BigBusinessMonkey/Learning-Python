def pigLatinTranslator():
	engWord = input("Please input the word you wish to translate, or type 'q' to end program.")
	if(engWord == "q"):
		print("Goodbye!")
	elif(engWord.isalpha()):
		eWordLength = len(engWord)
		zero = engWord[0]
		first = engWord[1]
		if(eWordLength == 1):
			print("Please input a word consisting of more than one letter.")
			pigLatinTranslator()
		elif(eWordLength == 0):
			print("Please input a word.")
			pigLatinTranslator
		else:
			print(engWord + " --oink-> " + first.upper() + engWord[2:eWordLength] + zero.lower() + "ay")
	else:
		print("Word must be composed of Latin Alphabet only.")
		pigLatinTranslator()
		
	
		
		
	
print("Welcome, this is a rudimentary Pig Latin translator. ")
pigLatinTranslator()