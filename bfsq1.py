from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])  
    all_paths = []

    while queue:
        current_vertex, current_path = queue.popleft()  

        if current_vertex == goal:
            all_paths.append(current_path)  
            continue  

        for neighbor in graph[current_vertex]:
            if neighbor not in current_path:  
                queue.append((neighbor, current_path + [neighbor]))  

    return all_paths  

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'C'],
    'F': ['C', 'G', 'H', 'I'],
    'G': ['D', 'F', 'J'],
    'H': ['F'],
    'I': ['F'],
    'J': ['G']
}

start_vertex = 'A'
goal_vertex = 'J'

all_paths = bfs(graph, start_vertex, goal_vertex)

if all_paths:
    print("All paths from", start_vertex, "to", goal_vertex, ":")
    for path in all_paths:
        print(path)
else:
    print("No path found from", start_vertex, "to", goal_vertex)
