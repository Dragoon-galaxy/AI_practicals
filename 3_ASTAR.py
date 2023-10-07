import heapq

# Define the graph_node as a dictionary with nodes as keys and their neighbors and edge costs as values
graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('S', 4), ('F', 5), ('E', 12)],
    'C': [('S', 3), ('D', 7), ('E', 10)],
    'D': [('C', 7), ('E', 2)],
    'E': [('D', 2), ('G', 5), ('B', 12), ('C', 10)],
    'F': [('G', 16), ('B', 5)],
    'G': [('F', 16), ('E', 5)]
}

# Define the heuristic function (h(n)) as a dictionary
heuristic = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}


# # Describe your graph here
# graph = {
#     'S' : [('B', 2), ('E', 3)],
#     'B' : [('C', 1), ('G', 9), ('S', 2)],
#     'C' : ['B', 1],
#     'E' : [('D', 6), ('S', 3)],
#     'D' : [('G', 1), ('E', 6)],
#     'G' : [('D', 1), ('B', 9)]
# }
#
# heuristic = {
#     'S' : 11,
#     'B' : 6,
#     'C' : 99,
#     'D' : 1,
#     'E' : 7,
#     'G' : 0,
#
# }

def astar(graph_node, start, goal):
    open_set = [(0, start)]  # Priority queue (cost, node)
    came_from = {}  # Dictionary to store the path
    g_score = {node: float('inf') for node in graph_node}  # Initialize g(n) scores to infinity
    g_score[start] = 0  # g(n) score for the start node
    f_score = {node: float('inf') for node in graph_node}  # Initialize f(n) scores to infinity
    f_score[start] = heuristic[start]  # f(n) score for the start node

    while open_set:
        _, current = heapq.heappop(open_set)  # Get the node with the lowest f(n) score
        if current == goal:
            return reconstruct_path(came_from, current), g_score[goal]  # Return the path and its cost

        for neighbor, cost in graph_node[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float('inf')  # No path found, return cost as infinity


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.insert(0, current)
        current = came_from[current]
    path.insert(0, current)  # Add the start node
    return path


# Perform A* search
start_node = 'S'
goal_node = 'G'
path, cost = astar(graph, start_node, goal_node)

# Print the result
if path:
    print("Optimal path:", ' --> '.join(path))
    print("Cost:", cost)
else:
    print("No path found.")































# graph = {
#     'S': [('A', 1), ('G', 10)],
#     'A': [('S', 1), ('B', 2), ('C', 1)],
#     'B': [('A', 2), ('D', 5)],
#     'C': [('A', 1), ('D', 3), ('G', 4)],
#     'D': [('C', 3), ('B', 5), ('G', 2)],
#     'G': [('S', 10), ('C', 4), ('D', 2)]
# }
#
# # Define the heuristic function (h(n)) as a dictionary
# heuristic = {
#     'S': 5,
#     'A': 3,
#     'B': 4,
#     'C': 2,
#     'D': 6,
#     'G': 0
# }

