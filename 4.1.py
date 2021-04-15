# Brute force solution 

from itertools import permutations

def solution(times, time_limit):
    N = len(times)
    bunnies = [i for i in range(1, N - 1)]
    
    # All pair shortest paths using Floyd-Warshall
    
    def floyd(W):
        # deepcopy, initializing the base cases
        delta = [[W[u][v] for v in range(N)] for u in range(N)]
        
        for k in range(N):
            for u in range(N):
                for v in range(N):
                    if delta[u][v] > delta[u][k] + delta[k][v]:
                        delta[u][v] = delta[u][k] + delta[k][v]
          
        # detect negative cycles
        for u in range(N):
            if delta[u][u] < 0:
                return False
            
        return delta
        
    # Given an order (P) of traversal of a subset of bunnies
    # calculate the time time required to escape with them 
    # using the shortest distance matrix delta
    
    def calc_path_weight(P):
        s, d = P[0], P[-1]
        weight = delta[0][s] + delta[d][N - 1]
        for i in range(len(P) - 1):
            weight += delta[P[i]][P[i + 1]]
                                  
        return weight

    delta = floyd(times)
                                  
    if not delta:
        # in case there is a negative cycle it
        # is possible to escape with all the bunnies.
        return [i - 1 for i in bunnies]
    
    # check for all permutations lexicographically
    # in descending order of size
    
    for k in range(N - 2, 0, -1):
        for P in permutations(bunnies, k):
            if calc_path_weight(P) <= time_limit:
                return [i - 1 for i in sorted(P)]
            
    # if no non empty subsets of bunnies returned
    # previously, then return the empty set
    return []

print(solution([[0, 1, 1, 1, 1], 
                [1, 0, 1, 1, 1], 
                [1, 1, 0, 1, 1], 
                [1, 1, 1, 0, 1], 
                [1, 1, 1, 1, 0]], 3))