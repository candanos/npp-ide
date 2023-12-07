# Implementing maze algorithm via a stack. 

def main():
    nodes = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0} #basicaly a dict that has a single boolean value.
        
    adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': []
    } #adjaceny_list is basically a map/dictionary whose values is a list
    
 #   adj_list = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D", "E"], "D": ["B", "C", "E"], "E": ["C", "D"] }
    
    nodes = {"A":"open", "B":"open", "C":"open", "D":"open", "E":"open", "F":"open"}    
    start = 'A'  #source_node
    target = 'F'  #target_node
    paths = []
    stack = [start] #stack is basicaly a list and a list is python has the stack functions.
    nodes[start] = "done"    
    i = 1
    while stack:
        # if i == 30:
            # break
        current = stack[-1]
        adjacents = adj_list.get(current)
        if check_if_you_can_go_deeper(current, adjacents, nodes, target):
            stack = go_deeper(adjacents, nodes, stack, target)
        else:
            if current == start:
                print("you can not step back from start.")
                stack.pop() 
            else:    
                nodes, stack, paths = step_back(nodes, stack, paths, target)
                print("hello." +str(i) + str(nodes))
        i = i + 1    
        
    for path in paths:
        print(' -> '.join(path))

    print(str(paths))
    
    # checking_if_you_can_go_deeper() = "look at the adjacencies of your current node and check is there any unvisited node or your current node is the destination node."
    
    # go_deeper() = "push to the stack which means append the next unvisited node in the adjacencies to the last element of the stack"
    
    # do_when_you_came_to_an_end() = "you must tag that node as visited, you must copy the stack to somewhere else, you must pop the stack, you must check is there any unvisited alternative. If there is an alternative node you must go deeper."
    
    
    
    
def check_if_you_can_go_deeper(current, adjacents, nodes, target):
    # "look at the adjacencies of your current node and check is there any unvisited node."

    if current == target: # zaten target isem daha ileri gidemem.
        return False

    current_state = nodes.get(current)
    for element in adjacents: 
        next_state = nodes.get(element)
        if element == target and current_state == "target": 
            pass
        elif next_state == "done":
            pass
        elif next_state == "open":   
           return True

    return False
    
def go_deeper(adjacents, nodes, stack, target):
    current = stack[-1]
    current_state = nodes.get(current)
    for element in adjacents: 
        next_state = nodes.get(element)
        if element == target and current_state == "target":
            pass
        elif next_state == "done":
            pass
        elif next_state == "open": 
           stack.extend(element)
           break 
    return stack 
    
def step_back(nodes, stack, paths, target):

# copy:if the previous node is open, you must copy the stack to somewhere else
# tag: if current node is not the target, you must tag the current node as done. 
# tag: if current node is the target, you must tag the previous node as target. 
# step_back: you must pop the stack
# copy 
    current = stack[-1]
    previous = stack[-2]

    
# tag         
    if current != target: 
        nodes[current] = "done"
    
    if current == target:     
        nodes[previous] = "target"

# we are step back from a tip point, so we shoulp copy the stack. 
# how to understand we are currently on a tip. the current is target or current state is done. 
    if current == target: 
       paths.append(stack.copy()) # we want to add stacks current state to paths but not the stacks itself.
   

# step_back
    stack.pop()  
    return nodes, stack, paths
    
    

# def find_all_paths(adj_list, source, destination):
    # paths = []
    # stack = [(source, [source])]
    # i = 0
    # print(f"{adj_list}")
    # while stack:
        # i = i + 1
        # current, path = stack.pop() # returns the last item and removes it from the list. 
        # if current == destination:
            # paths.append(path) 
        # for neighbor in adj_list[current]:
            # if neighbor not in path:
                # stack.append((neighbor, path + [neighbor]))

    # return paths




# all_paths = find_all_paths(adj_list, source_node, destination_node)

# Print all paths
# for path in all_paths:
    # print(' -> '.join(path))

if __name__ == "__main__":
    main()
