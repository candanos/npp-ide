# adjacency_list = {
# 1: [2, 3],
# 2: [1, 3, 4],
# 3: [1, 2, 4],
# 4: [2, 3, 5],
# 5: [4]
# }

def convert_to_adjacency_list(edge_list):
    adjacency_list = {}

    # Iterate over each edge in the edge list
    for edge in edge_list:
        vertex1, vertex2 = edge

        # Add vertex2 to the adjacency list of vertex1
        if vertex1 in adjacency_list:
            adjacency_list[vertex1].append(vertex2)
        else:
            adjacency_list[vertex1] = [vertex2]

        # Add vertex1 to the adjacency list of vertex2 (if the graph is undirected)
        if vertex2 in adjacency_list:
            adjacency_list[vertex2].append(vertex1)
        else:
            adjacency_list[vertex2] = [vertex1]

    return adjacency_list

# Example usage
edge_list = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]]
adjacency_list = convert_to_adjacency_list(edge_list)

# Print the adjacency list
for vertex in adjacency_list:
    neighbors = adjacency_list[vertex]
    print(f"{vertex}: {neighbors}")
