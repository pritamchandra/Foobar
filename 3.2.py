def solution(x, y):
    # the problem is equivalent to finding the number of steps
    # required by the euclidean algorithm to calculate the gcd
    # of x and y. We can reach 1 iff 1 = gcd(x, y)

    def gcd(x, y, count):
        if y == 0:
            return (x, count - 1)
            # count - 1 as we are considering the step till reaching (a, a) and not (a, 0)
        
        else:
            q, r = divmod(x, y)
            count += q
            # if q is the quotient we'll need to do (x - y) q times until x becomes less than q
            return gcd(y, r, count)
    
    gcd, count = gcd(int(x), int(y), 0)
    
    if gcd == 1: 
        return str(count)

    else: return "impossible"
    # if gcd(x, y) != 1 then no linear combination yields the (1, 1) state
    
print(solution(65, 85))