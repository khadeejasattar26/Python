def dfs(graph, start, end=None):
    visited = set()
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == end:
                return path
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'E', 'C'],
    'B': ['A', 'E', 'D'],
    'C': ['G', 'A', 'F'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

start_point = 'D'
end_point = 'C'

print(f"Path from {start_point} to {end_point}:")
path = dfs(graph, start_point, end_point)
if path:
    print(" -> ".join(path))
else:
    print("No path found.")
