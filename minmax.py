def minimax(node, depth, maximizing_player):
    if depth == 0 or game_over(node):
        return evaluate(node)
    
    return max(
        [minimax(child, depth - 1, False) for child in get_children(node)]
    ) if maximizing_player else \
        min(
        [minimax(child, depth - 1, True) for child in get_children(node)]
    )

# Example usage:
def game_over(node):
    return node == 0

def evaluate(node):
    return node

def get_children(node):
    return [node - 1, node - 2, node - 3]

print(minimax(10, 3, True))
