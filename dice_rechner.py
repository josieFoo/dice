import random
import time

def key_gen(n):
    """
    create an integer between 1 to n
    Args:
        n : an interger number
    Returns:
        _type_: an interger number
    """
    
    return random.randint(1,n)

def reg_gen(n):
    """
    create an dictionary
    Args:
        n: an interger number
    length: n
    keys: 1 to n
    initial values: 0
    """
    
    reg = {}
    for i in range(1,n+1):
        reg[i] = 0
    
    return reg

def dic(n, m):
    """
    calculates the probability of keys
    Args:
        n (int): number of keys
        m (int): how many times schould be generated?
    """
    
    reg=reg_gen(n)
    for i in range (0, m):
        k = key_gen(n)
        if k in reg:
            reg[k] += 1
        print(reg)
        
    reg_prob = {}
    for j in range(1, n+1):
        reg_prob[j]= f"{reg[j]/m*100} %"
        #print(f"{j}: {reg[j]/m*100} %")
    
    print("expected average: "+ f"{1/n*100}" + " %")
    print(reg_prob)
    
#test case
dic(2, 2**10)


