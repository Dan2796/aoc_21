# solution for day 12

#with open("example_input_12.txt", "r") as file:
with open("input_12.txt", "r") as file:
    lines = file.read().splitlines()

input_list = []
for line in lines: 
    input_list.append(line.split("-"))

nodes = []
for i in input_list:
    if i[0] not in nodes:
        nodes.append(i[0])
    if i[1] not in nodes:
        nodes.append(i[1])

tree = {}
for i in nodes:
    connected_to = []
    for j in input_list:
        if j[0] == i: connected_to.append(j[1])
    for j in input_list:
        if j[1] == i: connected_to.append(j[0])
    tree.update({i:connected_to}) 

def add_path_item(current_state, dictionary):
    new_state = []
    for path in current_state:
        for node in dictionary[path[-1]]:
            if path[-1] == "end": new = path
            else: new = path + [node]
            new_state.append(new)
    return new_state

def check_ended(path):
    result = "not ended"
    for node in path:
        if node == "end":
            result = "ended"
    return result

def check_all_ended(state):
    unended = 0
    for path in state:
        if check_ended(path) == "not ended": 
            unended += 1
    if unended == 0:
        ended = True
    if unended > 0:
        ended = False
    return ended

def check_valid(path):
    already_in_path = set()
    for node in path:
        if node in already_in_path:
            if node.islower():
                return "invalid"
        already_in_path.add(node)
    return "valid"

def keep_only_valid(state):
    new_state = []
    for path in state:
        if check_valid(path) == "valid": 
            new_state.append(path)
    return new_state

def remove_duplicates(state):
    new_list = []
    state_set = set()
    for path in state:
        if tuple(path) in state_set:
            new_list.append(path)
        state_set.add(tuple(path))
    return new_list

paths = [["start"]]
while True:
    paths = add_path_item(paths, tree)
    paths = keep_only_valid(paths)
    # quickly get rid of duplicates - tried doing this with a function and
    # for some reason just could not get it to work
    extra_set = set()
    extra_list = []
    for i in paths:
        extra_set.add(tuple(i))
    for i in extra_set:
        extra_list.append(list(i))
    paths = extra_list
    if check_all_ended(paths) == True:
        break

print("answer to part 1:", len(paths))

# update check valid function for small caves twice
def check_valid(path):
    used_up_small_cave_revisit = "no"
    already_in_path = set()
    for node in path:
        if node in already_in_path:
            if node == "start" or node == "end":
                return "invalid"
            if node.islower():
                if used_up_small_cave_revisit == "yes":
                    return "invalid"
                used_up_small_cave_revisit = "yes"
        already_in_path.add(node)
    return "valid"

paths = [["start"]]
while True:
    paths = add_path_item(paths, tree)
    paths = keep_only_valid(paths)
    # quickly get rid of duplicates - tried doing this with a function and
    # for some reason just could not get it to work
    extra_set = set()
    extra_list = []
    for i in paths:
        extra_set.add(tuple(i))
    for i in extra_set:
        extra_list.append(list(i))
    paths = extra_list
    if check_all_ended(paths) == True:
        break

print("answer to part 2:", len(paths))

