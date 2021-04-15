# find maximum flow subject to limited capacity from multiple sources to multiple sinks

def solution(sources, sinks, capacity):
    N = len(capacity)
    source, sink = sources[0], sinks[0]
    # shrink the sources to a single vertex, source[0] would represent all the sources
    # similarly for sinks
    
    # transform the graph capacities according to the updated source and sinks
    def transform():
        
        # The row (columns) corresponding to the new source (sink) is the sum of all rows
        # (columns) corresponding to all the sources (sinks)
        for i in range(N):
            capacity[i][source] = sum([capacity[i][s] for s in sources])
            capacity[source][i] = sum([capacity[s][i] for s in sources])
            capacity[i][sink] = sum([capacity[i][s] for s in sinks])
            capacity[sink][i] = sum([capacity[s][i] for s in sinks])
            
        # after the updates are done the remaining source vertices are not required anymore
        # all corresponding capacities are therefore updated to 0
        for i in range(1, len(sources)):
            s = sources[i]
            for j in range(N):
                capacity[s][j], capacity[j][s] = 0, 0
        
        # Similarly for sinks
        for i in range(1, len(sinks)):
            s = sinks[i]
            for j in range(N):
                capacity[s][j], capacity[j][s] = 0, 0
    
    # Breadth fast search for source-sink paths with positive flow            
    def BFS(residue):
        # initialize single source with Queue
        visited, parent = [False for i in range(N)], [None for i in range(N)]
        visited[source] = True
        Q = [source]
        flag = False # to denote whether the sink is reached
        
        # continue as long as Q is non empty and sink is not reached
        while Q != [] and not flag:
            u = Q.pop()
            for v in range(N):
                # visit those un-visited vertices from which flow is possible
                if not visited[v] and residue[u][v] > 0:
                    Q.insert(0, v)
                    visited[v], parent[v] = True, u
                    if v == sink:
                        flag = True # sink is reached
                        break
        
        return parent if flag else False
    
    # Ford Fulkerson Edmonds Karp Algorithm
    def maxflow():
        residue = [c for c in capacity] # initial residue
        paths = [] # store all paths here
        maxflow = 0 # initial flow
        
        # keep finding source sink paths and add their flow to the maxflow
        while True:
            parent = BFS(residue)
            # if no source sinks paths found
            if not parent: break 
        
            # construct path using parent list
            path, v = [source], sink
            while v != source:
                path.insert(1, v)
                u = parent[v]
                v = u
                
            # the flow of a path is the the minimum flow of all edges    
            flow =  min( [residue[path[i]][path[i + 1]] for i in range(len(path) - 1)] )
                
            # update the residues after the flow of the current path is determined
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                residue[u][v] -= flow
                residue[v][u] += flow
            
            paths.append(path)
            maxflow += flow
        
        return maxflow
        
    
    transform()
    return maxflow()


solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], 
                          [0, 0, 5, 2, 0, 0], 
                          [0, 0, 0, 0, 4, 4], 
                          [0, 0, 0, 0, 6, 6], 
                          [0, 0, 0, 0, 0, 0], 
                          [0, 0, 0, 0, 0, 0]])