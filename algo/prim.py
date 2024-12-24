import heapq

def prim_mst(graph, start):
    
    mst = [] 
    visited = set() 
    total_weight = 0 
    pq = [] 

  
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbor))

   
    while pq and len(mst) < len(graph) - 1:
        weight, u, v = heapq.heappop(pq)  # Get the edge with the smallest weight

        if v not in visited:  # Avoid cycles
            visited.add(v)
            mst.append((u, v, weight))  # Add edge to MST
            total_weight += weight  # Add weight to total

            
            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, v, neighbor))

    return mst, total_weight


# Example Usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 3), ('D', 2)],
    'C': [('A', 4), ('B', 3), ('D', 5)],
    'D': [('B', 2), ('C', 5)]
}

start_vertex = 'A'
mst, total_weight = prim_mst(graph, start_vertex)
print("MST Edges:", mst)
print("Total Weight:", total_weight)