#Codingbat.com/python practices

"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"."
"""

def string_bits(str):
    length = len(str)
    new = ""
    for a, b in enumerate(str):
        if(a % 2 == 0):
            new += b
        else:
            continue
    return(new)
        
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

def string_explosion(str):
    final = []
    lust = str.split()
    for a in range(len(str)):
        final.append(str[0:(a + 1)])
    return("".join(final))
    
