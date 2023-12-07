# You can solve that using deptf-first-search algorithm (maze), 
# and you can implement maze algorithm using stack, recursion. 
def find_all_paths(adj_list, source, destination):
    paths = []
    stack = [(source, [source])]
    i = 0
    print(f"{adj_list}")
    while stack:
        i = i + 1
        current, path = stack.pop() # returns the last item and removes it from the list. 
        if current == destination:
            paths.append(path) 
        for neighbor in adj_list[current]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return paths


# Example usage
adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

source_node = 'A'
destination_node = 'F'
all_paths = find_all_paths(adj_list, source_node, destination_node)

# Print all paths
for path in all_paths:
    print(' -> '.join(path))
