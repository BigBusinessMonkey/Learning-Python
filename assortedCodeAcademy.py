#Assorted independent exercises produced as part of "Practice makes perfect" section of Code Academy Python course

#function that returns reverse of input
def reverse(text):
    length = len(text)
    repeats = 1
    mirror = ""
    for letter in text:
        letter = str(text[length - repeats])
        repeats += 1
        mirror += letter
    return(mirror)
    
    
#function thhat returns input with vowels removed
def anti_vowel(text):
    voweless = ""
    vowels = ["A", "a", "e", "E", "i", "I", "o", "O", "u", "U"]
    for letter in text:
        if(letter in vowels):
            continue
        else:
            voweless += letter
    return voweless
    
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
#function that returns scrabble score of input
def scrabble_score(word):
    SCORE = 0
    word = word.lower()
    for letter in word:
        SCORE += score[letter]
    return SCORE
        

