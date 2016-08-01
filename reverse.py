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
        
