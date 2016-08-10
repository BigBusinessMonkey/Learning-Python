import random
"""
Rigged random number generator, based on an initial misunderstanding of a programming challenge. Takes arguments "high" or "low" or "unweighted", 
which determines whether generated numbers are weighted towards high end or low end.

Work in progress
"""
def weightnum(weighting):
    print("This is a totally unweighted randon integer generator that allows use to define lower and upper bounds, and specificy quantity of numbers generated. (All boundaries are inclusive.) \n")
    lower = int(input("Input lower boundary: "))
    upper = int(input("\nInput upper boundary: "))
    quant = int(input("\nHow many numbers do you wish to generate? "))
    median = lower + upper / 2
    if(upper <= lower):
        print("Upper bound must exceed lower bound, please try again.\n")
        weightnum()
    else:
         for x in range(1, (quant + 1)):
            flip = random.randint(0,1)
            if(flip == 1 or weighting == "unweighted"):
                print(random.randint(lower,upper))
            else:
                if(weighting == "high"):
                    print(random.randint(median + lower / 2,upper))
                elif(weighting == "low"):
                    print(random.randint(lower, median + upper / 2))
                    
weightnum("high")