tree = {
    'A': {
        'B': {
            'E': 3,
            'F': 5
        },
        'C': {
            'G': 6,
            'H': 9
        },
        'D': {
            'I': 1,
            'J': 2
        }
    }
}

def minimax(node, depth, is_maximizing_player):
    if type(node) is int:
        return node, str(node)
    if is_maximizing_player:
        best_value = -float('inf')
        path = ""
        for key, subtree in node.items():
            value, subpath = minimax(subtree, depth + 1, False)
            if value > best_value:
                best_value = value
                path = key + " -> " + subpath
        return best_value, path
    else:
        best_value = float('inf')
        path = ""
        for key, subtree in node.items():
            value, subpath = minimax(subtree, depth + 1, True)
            if value < best_value:
                best_value = value
                path = key + " -> " + subpath
        return best_value, path

optimal_cost, optimal_path = minimax(tree, 0, True)
print(f"Optimal Cost: {optimal_cost}")
print(f"Optimal Path: {optimal_path}")
