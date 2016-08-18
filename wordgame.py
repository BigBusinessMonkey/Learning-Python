"""
Word game:
Play has limited number of guesses
Player guesses letter
Returns word with letters filled in
Repeat
Player can guess word at any time, but uses up two guesses if incorrect
"""
import random



raw = open("words.txt", "r")
list = (raw.read()).split()
raw.close()
randomNum = random.randint(1,len(list))

word = (list[randomNum - 1])

chances = len(word) * 3
if(chances > 16):
    chances = 16
    
print("This is a word game. A word has been generated, and it is up to you to guess what it is.")
print("This round the word has " + str(len(word)) + " characters.")
print("You may guess letters, or you may guess words. Letters utilise one guess, words two. You have " + chances + "guesses.")
def guessing():
    solved = ""
    for x in chances:
        guess = input("Begin:")
        try(int(guess)):
            print("Please try again, ensuring your input is either a letter or a word.")
            guessing()
        except ValueError:
            continue
        if
        for y in word:
    
        
