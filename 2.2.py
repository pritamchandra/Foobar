def solution(L):
    n = len(L)
    L = sorted(L) 
    # sort the list as the largest number would be beginning with the
    # largest digit of the subarray whose sum is divisible by 3
    
    D = [x % 3 for x in L] # stores the numbers reduced modulo 3
    
    T = [ [0 for m in range(3)] for i in range(n) ]
    pi = [ [(None, None) for m in range(3)] for i in range(n) ]
    # define T[i][m] as the longest subsequence ending in L[i] congruent to
    # m mod 3, and pi[i][m] stores the parent of i in that subsequence
    
    def relax(i, j, m, k):
        if T[j][k] != 0:
            if (1 + T[j][k]) >= T[i][m]:
                T[i][m] = 1 + T[j][k]
                pi[i][m] = (j, k)
                
    for i in range(n):
        T[i][D[i]] = 1 
        # implements the base cases
        
        for m in range(3):
            k = (m - D[i]) % 3 
            for j in range(i):
                relax(i, j, m, k)   
                
    # relax implements the following recurrence 
    # T[i][m] =  max_{j < i} {1 + T[j][k]}, where k + L[i] = m mod 3
    # if j particularly maximises the above recurrence then paren(i, m) = (j, k) 
                
    maxloc = 0 # stores the starting location of the largest possible digit
    for i in range(n):
        if T[i][0] >= T[maxloc][0]: maxloc = i
            
    answer = 0
    loc = (maxloc, 0)
    # this variable would recursively call the parents one by one to construct the largest number
    
    if T[maxloc][0] != 0: 
    # eliminating the case when no such number exists
        while loc != (None, None):
            answer = answer * 10 + L[loc[0]]
            loc = pi[loc[0]][loc[1]]
        
    return answer

L = [7, 4, 1, 4, 6, 8, 0, 8] 
print(solution(L))