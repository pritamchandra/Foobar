
def solution(m):
    # initialize memo table T with 0s
    T = [[0 for i in range(m + 1)] for j in range(m + 1)]
    T[1][1] = 1 # base case
    
    # define T(n, i): number of distinct partitions of n
    # such that no term is smaller than i
    
    # Recurrence used,
    # T(n, i) = 1 + sum T(n - j, j + 1) over i <= j <= floor {(n - 1)/2}
    
    for n in range(2, m + 1):
        for i in range(1, m + 1):
            result = 1
            lim = int((n - 1)/2)
            
            for j in range(i, lim + 1):
                result += T[n - j][j + 1]
                
            T[n][i] = result
            
            if (n, i) == (m, 1): break
    
    # Clearly the solution is T(m, 1), however we substract 1 as the number
    # itself is not asked (in the specific question) to be considered as a partition
    
    return(T[m][1] - 1)
            
print(solution(200))