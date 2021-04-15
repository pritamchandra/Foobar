def solution(start, length):
    
    # calculate the XOR in the range [1, n] and observe that the value has period 4
    def xortill(n):
        if n % 4 == 1: return 1
        elif n % 4 == 2: return (n + 1)
        elif n % 4 == 3: return 0
        else: return n
    
    answer = 0
    
    for j in range(length):
        # XOR[x, y] = XOR[1, x - 1] ^ XOR[1, y]
        # Calculate the boundaries for each line
        a = xortill( start + (j * length) - 1 )
        b = xortill( start + ((j + 1) * length) - (j + 1) )
        answer = answer ^ (a ^ b)
        
    return answer
    
print(solution(17, 4))