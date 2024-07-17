import heapq

def a_star(graphA, heuristic, start, goal):
    
    open_list = [(0 + heuristic[start], start)]  
    came_from = {}  
    g_score = {node: float('inf') for node in graph}  
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph} 
    f_score[start] = heuristic[start]
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            return reconstruct_path(came_from, current), g_score[goal]
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                if not any(neighbor == n for _, n in open_list):
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
                    
    return None, None

def reconstruct_path(came_from, current):
   
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


graph = {
    'A': [('B', 6), ('C', 9), ('E', 1)],
    'B': [('A', 6), ('D', 4), ('E', 4)],
    'C': [('A', 9), ('F', 2), ('G', 3)],
    'D': [('B', 4), ('E', 5), ('F', 7)],  
    'E': [('A', 1), ('B', 4), ('D', 5), ('F', 6)],
    'F': [('C', 2), ('D', 7), ('E', 6)],
    'G': [('C', 3)]
}

heuristic_values = {
    'A': 7,
    'B': 5,
    'C': 5,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 0
}


start_node = 'A'
goal_node = 'G'


if start_node in graph and goal_node in graph:
    path, total_cost = a_star(graph, heuristic_values, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to reach {goal_node} using A* algorithm is: {path}")
        print(f"Total cost from {start_node} to {goal_node} by A* algorithm is: {total_cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
else:
    print("Invalid start or goal node.")
