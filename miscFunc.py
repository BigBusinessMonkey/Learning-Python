def digit_sum(n):
    sm = 0
    n = str(n)
    for x in range(len(n)):
        sm += float(n[x])
    return int(sm)
        
 
def factorial(x):
    FACT = 1
    for i in range(x):
        i += 1
        FACT *= i
    return FACT
    
def is_prime(x):
    if(x < 2):
        return False
    else:
        for n in (range(2, x)):
            if(x % n != 0):
                continue
            else:
                return False
                break
        else:
            return True
                