from math import inf

def solution(xs):
    n = len(xs)
    
    if n == 1:
        return str(xs[0])  #in case there is just one panel
    
    max_neg, neg_c, zero_c = - 1001, 0, 0
    # stores the maximum negative power, the number of negative power
    # and the number of zero powers respectively
    
    prod = 1
    #for storing the product of non-zero panel powers
    
    for i in xs:
        if i == 0: 
            zero_c += 1
        
        else:
            prod = prod * i
            
            if i < 0: 
                neg_c += 1
                if i >= max_neg:
                    max_neg = i
    
    if (zero_c == n - 1 and neg_c == 1) or (zero_c == n):
        return "0"
        # corner cases
    
    elif neg_c % 2 == 0: return str(int(prod))
    # if there are even number of negative powers then the maximum
    # product comprises of all the non zero powers
    
    else: return str(int(prod / max_neg))
    # if there are an odd number of them, we take out from the product
    # of non-zero powers the negative power with least absolute value
    
    
L = [-2, -3, 4, -5]
print(solution(L))
        