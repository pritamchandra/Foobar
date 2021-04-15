from math import sqrt, floor, log
def solution(n):
    n = int(n)
    # define a = sqrt(2) - 1 = r/t, use 100 digits for the required precision
    r = 41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206
    t = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    
    # Use the following recurrence. Define m = floor(a * n)
    # Let S(n) be the required beatty sum up to n terms, then S(0) = 0
    # S(n) = mn + n(n+1)/2 - m(m+1)/2 + S(m)
    # The is obtained using Rayleigh Theorem
    
    def S(n):
        if n == 0: return 0
        else:
            m = int((r * n)/t)
            M = int(m * (m + 1) / 2)
            N = int(n * (n + 1) / 2)
            return m * n + N - M - S(m)
    
    return(str(S(n)))

solution(10**100)