
weighted_edge_list = [
    ['A', 'B', 2],
    ['A', 'C', 4],
    ['B', 'D', 1],
    ['C', 'D', 5],
]

def main():
    adjacency_list = edge_list_to_adjacency_list(weighted_edge_list)
    for vertex in adjacency_list:
        print(f"{vertex}: {adjacency_list[vertex]}")

def edge_list_to_adjacency_list(edge_list):
    adjacency_list = {}
    for edge in weighted_edge_list:
        vertex1, vertex2, weight = edge 
        if adjacency_list.get(vertex1):
           adjacency_list[vertex1].update({vertex2: weight}) 
        else:    
           adjacency_list[vertex1] = {vertex2: weight} 

        if adjacency_list.get(vertex2):
           adjacency_list[vertex2].update({vertex1: weight}) 
        else:    
           adjacency_list[vertex2] = {vertex1: weight}
    return adjacency_list
# adjacency_list is a map that its keys are basic types and values are map.
# graph = {
    # 'A': {'B': 5, 'C': 3},
    # 'B': {'A': 5, 'C': 2, 'D': 1},
    # 'C': {'A': 3, 'B': 2, 'D': 6},
    # 'D': {'B': 1, 'C': 6}
# }

if __name__ == '__main__':
    main()