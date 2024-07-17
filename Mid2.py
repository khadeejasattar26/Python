#graph
graph = {
    'A': [('B', 6), ('C', 9), ('E', 1)],
    'B': [('A', 6), ('D', 4), ('E', 4)],
    'C': [('A', 9), ('F', 2), ('G', 3)],
    'D': [('B', 3), ('E', 5), ('F', 7)],
    'E': [('A', 1), ('B', 4), ('D', 5), ('F', 6)],
    'F': [('C', 2), ('D', 7), ('E', 6)],
    'G': [('C', 3)]
}

#heuristic values
heuristic = {
    'A': 7,
    'B': 5,
    'C': 5,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 0
}

import heapq

def astar(graph, heuristic, start, goal):
    open_list = [(0, start)]  
    came_from = {}  
    g_score = {node: float('inf') for node in graph}  
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  
    f_score[start] = heuristic[start]
    
    while open_list:
        _, current = heapq.heappop(open_list)  
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            # Reverse path to get  and return total cost
            return path[::-1], g_score[goal]  
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score+ heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None, None  


start_node = 'A'
goal_node = 'G'

path, total_cost = astar(graph, heuristic, start_node, goal_node)
if path:
    print("Path from", start_node, "to", goal_node, "by A* algo is :", path)
    print("Total cost from:",start_node,"to",goal_node,"by A* algo is :", total_cost)
else:
    print("No path found from", start_node, "to", goal_node)