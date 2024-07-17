def bfs(graph, start, target):
  """
  Performs BFS on a graph to find a path from start to target.

  Args:
      graph: A dictionary representing the graph.
      start: The starting node (Location A).
      target: The target node (Location F).

  Returns:
      A list representing the path from start to target if found, otherwise None.
  """
  queue = [(start, [])]  # Queue stores (node, path to that node)
  visited = set()
  while queue:
    current_node, path = queue.pop(0)
    visited.add(current_node)
    if current_node == target:
      return path + [current_node]  # Return path including current node
    for neighbor in graph[current_node]:
      if neighbor not in visited:
        queue.append((neighbor, path + [current_node]))  # Add neighbor with updated path
  return None  # Target not found

# Sample dungeon graph (replace with your actual graph data)
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


# Find path from Location A to Location F
path_to_f = bfs(graph, 'A', 'F')

if path_to_f:
  print("Path from Location A to Location F:", " -> ".join(path_to_f))
else:
  print("No path found from A to F")
