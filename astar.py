graph = {
    "S": {"G": 10, "A": 1},
    "A": {"B": 2, "C": 1},
    "B": {"D": 3},
    "C": {"D": 3, "G": 4},
    "D": {"G": 2},
    "G": {}
}

heuristic = {
    "S": 5,
    "A": 3,
    "B": 4,
    "C": 2,
    "D": 6,
    "G": 0
}

start, goal = "S", "G"
visited, total_cost = [start], 0

while start != goal:
    next_node = graph[start]
    fn_values = {cost + heuristic[next_node]: next_node for next_node, cost in next_node.items()}
    selected_cost = min(fn_values.keys())
    start = fn_values[selected_cost]
    total_cost += selected_cost
    visited.append(start)
    
print("Path is:", " -> ".join(visited))
print("Total path cost:", total_cost)


