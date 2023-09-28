from queue import PriorityQueue

v = 9
# v = 10
graph = [[] for i in range(v)]

# Define the heuristic values for each node
heuristic_values = [10, 7, 3, 5, 2, 4, 6, 4, 1]
# heuristic_values = [10, 8, 7, 6, 5, 4, 3, 4, 2, 0]

# Function For Implementing Best First Search
# Gives output path having the lowest cost


def best_first_search(actual_Src, destination, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((heuristic_values[actual_Src], actual_Src, 0))  # Use heuristic values as the initial priority and initialize cost
    visited[actual_Src] = True

    min_cost = float('inf')  # Initialize minimum cost as positive infinity

    while not pq.empty():
        item = pq.get()  # Dequeue the item
        u, cost_so_far = item[1], item[2]  # Get the node and cost_so_far
        # Displaying the path having the lowest cost
        print(u, end=" ")
        if u == destination:
            min_cost = cost_so_far  # Update the minimum cost if the destination is reached
            break

        for n, edge_cost in graph[u]:
            if not visited[n]:
                visited[n] = True
                # Calculate the total cost by adding the edge cost to the cost_so_far
                total_cost = cost_so_far + edge_cost
                pq.put((heuristic_values[n], n, total_cost))  # Use heuristic values for priority and update the total cost

    print("\nMinimal Cost:", min_cost)  # Output the minimal cost


# Function for adding edges to graph
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# The nodes shown in the above example (by alphabets) are
# implemented using integers addedge(x, y, cost);
addedge(0, 1, 4)
addedge(0, 7, 8)
addedge(1, 7, 11)
addedge(1, 2, 8)
addedge(2, 8, 2)
addedge(2, 3, 7)
addedge(2, 5, 4)
addedge(3, 4, 9)
addedge(3, 5, 14)
addedge(4, 5, 10)
addedge(5, 6, 2)
addedge(6, 8, 6)
addedge(6, 7, 1)
addedge(7, 8, 7)

source = 0
target = 4
best_first_search(source, target, v)

# addedge(0, 1, 6)
# addedge(0, 5, 3)
# addedge(1, 3, 2)
# addedge(1, 2, 3)
# addedge(2, 3, 1)
# addedge(2, 4, 5)
# addedge(3, 4, 8)
# addedge(4, 8, 5)
# addedge(4, 9, 5)
# addedge(5, 6, 1)
# addedge(5, 7, 7)
# addedge(6, 8, 3)
# addedge(7, 8, 2)
# addedge(8, 9, 3)
#
#
# source = 0
# target = 9
# best_first_search(source, target, v)


