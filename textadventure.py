"""
fragment of text adventure, created to increase fluency with simpler elements of python.

Plans to add gender choice at start, including alternative narrative depending on this.
"""
class Character(object):
    health = "Perfectly Healthy"
    def __init__(self,name,species,age,goal):
        self.name = name
        self.species = species
        self.keyTraits = []
        self.goal = goal

    def checkHealth(self):
        return(self.name + " is " + self.health)
        
        
    
protag = Character("Player","Human",20,"Self")   
ucelagon = Character("Ucelagon the Wise","Wizard","Impossibly old","The pursuit of arcane learning")    
dogName = ""
antName = ""
ambition = ""
    
def start():
    print("Welcome to Adventures in Anhedonia, an interactive text adventure programmed in Python.")
    begin = input("Type 'start' to begin, or anything else to end the program. ")
    begin = begin.lower()
    if(begin == "start"):
        print("You are the seventh prince of Anhedonia, the 45th child of King Nero the Great. As the youngest prince you have very few responsibilities, and nobody expects much of you. You have a great deal of free time, and you spend most of it reading, exploring the vast palatial grounds, and playing with your dog.\n")
        dogName = input("Do you remember your dog's name? ").lower()
        dogName = (dogName[0].upper() + dogName[1:])
        dogIntro = "He has been your loyal companion and guardian since childhood. Given as a gift to your father by ambassadors from the distant land of Zet Tsuubou, " + dogName + " is the size of a large 12 year old boy, and with his thick brown main has been mistaken, at times, for either a dire wolf, a bear, or some undiscovered species of Lion. His breed are smart, strong, loyal and have a natural life span on par with humans. " + dogName + " though the same age as you, willl likely outlive you. He likes cucumber, and chasing rabbits. He is a good dog\n"
        if(dogName == "No"):
            dogName = "Rasputin"
            print("That's fine, we've all forgotten the name of a loved one once or twice, haha. Your dog is called Rasputin. Don't beat yourself up about it.")
            protag.keyTraits.append("Hopelessly forgetful")
            print(dogIntro)
            prologue(dogName)
        elif(dogName == "Yes"):
            dogName = input("Great, what is it?").lower()
            dogName = (dogName[0].upper() + dogName[1:])
            print(dogIntro)
            prologue(dogName)
        else:
            print("\nThat's right, your dog is called " + dogName + ".")
            print(dogIntro)
            prologue(dogName)
    elif(begin == "anything else"):
        print("Witty stuff, fam.")
    else:
        print("Maybe another time then.")            
            
def prologue(dogName):
    print("Yes, " + (dogName) + " certainly is a wonderful dog, and while it's tempting to continue to expound his myriad merits, unfortunately other things must take precedence. As the seventh prince, though you admittedly have few obligations, you still have some. Most immediate among them is the obligation to wake up before midday and get out of bed.")
    decisionOne = input("Do you think you might like to get up? (yes or no)").lower 
    if(decisionOne == no):
        print("")
    elif(decisionOne == yes):
        print("")
    elif(decisionOne == maybe):
        print("")
        
def prologueA1():
    print()

def prologueA2():
    print()
    
start()