from collections import deque
import math


def can_measure_water(jug1capacity, jug2capacity, jug1initial, jug2initial, jug1final, jug2final):
    print(f"GCD: {math.gcd(jug1capacity, jug2capacity)}")
    if math.gcd(jug1capacity, jug2capacity) == 1:
        print("GCD is 1, Solution only exists if one of two final jug capacities is zero.")
    visited = set()
    que = deque([(jug1initial, jug2initial, [])])  # Adding the current state path to the queue
    while len(que):
        a, b, path = que.popleft()
        if (a == jug1final and b == jug2final) or (a == jug2final and b == jug1final):
            print("It is possible to reach the final state.")
            if a == jug2final and b == jug1final:
                print("But in Vice versa form.")
            return path + [(a, b)]
        if a and b < jug2capacity:
            c = min(a, jug2capacity - b)
            if (a - c, c + b) not in visited:
                visited.add((a - c, c + b))
                que.append((a - c, c + b, path + [(a, b)]))
        if b and a < jug1capacity:
            c = min(b, jug1capacity - a)
            if (a + c, b - c) not in visited:
                visited.add((a + c, b - c))
                que.append((a + c, b - c, path + [(a, b)]))
        if a and (0, b) not in visited:
            visited.add((0, b))
            que.append((0, b, path + [(a, b)]))
        if b and (a, 0) not in visited:
            visited.add((a, 0))
            que.append((a, 0, path + [(a, b)]))
        if a != jug1capacity and (jug1capacity, b) not in visited:
            visited.add((jug1capacity, b))
            que.append((jug1capacity, b, path + [(a, b)]))
        if b != jug2capacity and (a, jug2capacity) not in visited:
            visited.add((a, jug2capacity))
            que.append((a, jug2capacity, path + [(a, b)]))
    return []


def print_states(states_1):
    print("Sequence of states:")
    for state in states_1:
        print(state)


# Taking inputs from the user
jug1_Capacity = int(input("Enter the capacity of jug 1: "))
jug2_Capacity = int(input("Enter the capacity of jug 2: "))
jug1_Initial = int(input("Enter the initial amount in jug 1: "))
jug2_Initial = int(input("Enter the initial amount in jug 2: "))
jug1_Final = int(input("Enter the final amount in jug 1: "))
jug2_Final = int(input("Enter the final amount in jug 2: "))

states = can_measure_water(jug1_Capacity, jug2_Capacity, jug1_Initial, jug2_Initial, jug1_Final, jug2_Final)
if states:
    print_states(states)
else:
    print("It is not possible to reach the final state.")

# HERE IT IS PRINTING VICE VERSA IS POSSIBLE AND STATES ALSO , BUT IF (2, 0) THEN (0, 2) IS SHOWING WITH THE STATEMENT VICE VERSA IS POSSIBLE