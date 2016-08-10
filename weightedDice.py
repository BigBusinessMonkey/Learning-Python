
"""
Rigged random number generator, based on an initial misunderstanding of a programming challenge. Provides x weighted random numbers, where x is a quantity determined by user, when given upper 
and lower bounds (also by user). Takes arguments "high" or "low" or "unweighted", 
that determines whether generated numbers are weighted towards high end or low end. Skews result in favour of given argument.

Work in progress
"""
import random
import statistics
def weightnum(weighting,showAverage):
    print("This is a totally unweighted randon integer generator that allows the user to define lower and upper bounds, and specificy quantity of numbers generated. (All boundaries are inclusive.) \n")
    lower = int(input("Input lower boundary: "))
    upper = int(input("\nInput upper boundary: "))
    quant = int(input("\nHow many numbers do you wish to generate? "))
    median = int(lower + upper / 2)
    if(upper <= lower):
        print("Upper bound must exceed lower bound, please try again.\n")
        weightnum()
    else:
        sum = []
        for x in range(1, (quant + 1)):
            flip = random.randint(0,2)
            if(flip >= 1 or weighting == "unweighted"):
                print(random.randint(lower,upper))
            else:
                if(weighting == "high"):
                    num = (random.randint(int(median + lower / 2),upper))
                    print(num)
                    sum.append(num)
                elif(weighting == "low"):
                    num = (random.randint(lower, int(median + upper / 2)))
                    print(num)
                    sum.append(num)
        print(sum)
        average = statistics.mean(sum)
    if(showAverage == True):
        print(average)
        
        

weightnum("high", True)