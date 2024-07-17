import heapq

def a_star(graph, start, end, h):
    # Priority queue: (f-score, g-score, current_node, path)
    open_set = []
    heapq.heappush(open_set, (0 + h[start], 0, start, [start]))
    visited = set()

    # g_scores holds the cost of getting from the start node to that node, initialized with infinity.
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0

    while open_set:
        _, g, current, path = heapq.heappop(open_set)

        if current == end:
            print("A* Path:", ' '.join(path))
            return path

        visited.add(current)

        for neighbor, weight in graph[current]:
            if neighbor in visited:
                continue

            # The distance from start to a neighbor
            # the "current" is now the new parent node to the neighbor
            tentative_g_score = g + weight

            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor, path + [neighbor]))

    return []

# Example weighted graph represented as an adjacency list
graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('A', 4), ('C', 2), ('D',5)],
    'C': [('A', 3), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 2)],
    'E': [('D', 2)],
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0,
}

start_point = 'A'
end_point = 'D'
print("A* Traversal on Weighted Graph:")
a_star(graph, start_point, end_point, heuristic)