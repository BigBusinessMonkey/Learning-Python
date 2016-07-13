def pigLatinTranslator():
	print("Welcome to this Pig Latin translator. ")
	engWord = input("Please input the word you wish to translate into pig latin, or type 'q' to end program.")
	eWordLength = len(engWord)
	zero = engWord[0]
	first = engWord[1]
	if(engWord != "q"):
		if(eWordLength == 1):
			print("Please input a word consisting of more than one letter.")
			pigLatinTranslator()
		elif(eWordLength == 0):
			print("Please input a word.")
			pigLatinTranslator
		else:
			print(first.upper() + engWord[2:eWordLength] + zero.lower() + "ay")
	else:
		"Goodbye!"
	
		
		
	
	
pigLatinTranslator()