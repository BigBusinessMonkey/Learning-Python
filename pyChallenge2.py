"""
Mastermind
From http://usingpython.com/python-programming-challenges/
"""

import random
number = random.randint(1000,9999)
guesses = 0
print(number)
print("----MASTERMIND----\n\nGuess the 4 numbers in as few tries as possible.")
while True:
    guess = input(str(guesses + 1) + ") ")
    guesses += 1
    feedback = 0
    if(int(guess) == number):
        print("Congratulations, you found the number in " + str(guesses) + " guesses.")
        break
    elif(int(guess) > 9999 or len(list(guess)) != 4):
        print("Number has four digits.")
        guesses -= 1
        continue
    else:
        for x in range(4):
            numList = list(str(number))
            guessList = (str(guess))
            if(numList[x] == guessList[x]):
                feedback += 1
                continue
            else:
                continue
              
        print(feedback * "*")
        if(feedback == 0):
            print("No numbers correct.")
        continue
        
    

