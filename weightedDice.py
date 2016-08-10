import random
"""
Rigged random number generator, based on an initial misunderstanding of a programming challenge. Provides x weighted random numberers, where x is a quantity determined by user, when given upper 
and lower bounds (also by user). Takes arguments "high" or "low" or "unweighted", 
which determines whether generated numbers are weighted towards high end or low end. Attempts to bias results subtly.

Work in progress
"""
def weightnum(weighting):
    print("This is a totally unweighted randon integer generator that allows use to define lower and upper bounds, and specificy quantity of numbers generated. (All boundaries are inclusive.) \n")
    lower = int(input("Input lower boundary: "))
    upper = int(input("\nInput upper boundary: "))
    quant = int(input("\nHow many numbers do you wish to generate? "))
    median = int(lower + upper / 2)
    if(upper <= lower):
        print("Upper bound must exceed lower bound, please try again.\n")
        weightnum()
    else:
         for x in range(1, (quant + 1)):
            flip = random.randint(0,2)
            if(flip >= 1 or weighting == "unweighted"):
                print(random.randint(lower,upper))
            else:
                if(weighting == "high"):
                    print(random.randint(int(median + lower / 2),upper))
                elif(weighting == "low"):
                    print(random.randint(lower, int(median + upper / 2)))
                    
weightnum("high")