# Refer to 4.1 extended discussion
def solution(times, time_limit):
    N = len(times)
    
    # Bellman-Ford to calculate single source shortest paths, detect
    # negative cycles, and transform all weights into non-negative
    # weights using Johnson's method
    
    def bellmanford(times, s): 
        delta = [inf for i in range(N)]
        delta[s] = 0
        
        for i in range(N - 1):
            for u in range(N):
                for v in range(N):
                    delta[v] = min(delta[v], delta[u] + times[u][v])
        
        for u in range(N):
            for v in range(N):
                if delta[v] > delta[u] + times[u][v]:
                    return False
                
        return delta
    
    # Recurrence, T(v, t): maximum set of vertices that can be spanned by any 
    # source (0) to "v" walk that has total weight smaller than t
    # Relate, T(v, t) = {v}  union  { largest over u in Adj[v] [T(u, t - W(u, v))] }
    
    def T(v, t):
        # base cases, T(0, 0) = [0]
        # T(v, t) = [], if t < _delta[v], minimum distance from 0 to 
        
        if (v, t) == (0, 0): return [0]
        elif t < _delta[v]: return []
        
        else:
            M = []
            for u in range(N):
                if u != v:
                    S = T(u, t - _times[u][v])
                    if len(S) > len(M):
                        M = S
                        
            M.append(v)
            return list(set(M))
    
    # any random source other than 0 can be used if 0 is used then all source destination 
    # shortest paths after the transformation have 0 weight, which is undesirable
    delta = bellmanford(times, 2)
    
    if not delta:
        # in case there is a negative cycle it
        # is possible to escape with all the bunnies.
        return [i - 1 for i in range(1, N - 1)]
    
    # Otherwise transform the graph using Johnson's algorithm to contain non-negative 
    # weights only, where h(u) = delta(s, u). Update the new quantities accordingly.
    _times = [[(times[i][j] + delta[i] - delta[j]) for j in range(N)] for i in range(N)]
    _delta = bellmanford(_times, 0)
    _time_limit = time_limit + delta[0] - delta[N - 1]
    
    # Call the recursion
    T = T(N - 1, _time_limit)
    return [T[i] - 1 for i in range(1, len(T) - 1)]

print(solution([[0, 1, 1, 1, 1], 
                [1, 0, 1, 1, 1], 
                [1, 1, 0, 1, 1], 
                [1, 1, 1, 0, 1], 
                [1, 1, 1, 1, 0]], 3))
