def print_tree(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    print(" " * (height - 1) + "*")

tree_height = 100 # Высота ёлки (количество уровней)

print_tree(tree_height)