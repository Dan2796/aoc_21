# solution for day 9

#with open("example_input_09.txt", "r") as file:
with open("input_09.txt", "r") as file:
    lines = file.read().splitlines()

cave_map = []
for line in lines: cave_map.append(list(line)) 

# turn into integers:
for row in range(0, len(cave_map)):
    for num in range(0, len(cave_map[row])):
        cave_map[row][num] = int(cave_map[row][num])

# using if conditions to avoid dropping of edge of the map
def find_around(map_matrix, row, column):
    around = set()
    
    if column > 0: # left
        around.add(map_matrix[row][column - 1])
    if column < (len(map_matrix[row]) - 1): # right
        around.add(map_matrix[row][column + 1])
    if row > 0: 
        around.add(map_matrix[row - 1 ][column]) # above
    if row < (len(map_matrix) - 1): # below
        around.add(map_matrix[row + 1][column])
    # set used to avoid unnecessary duplicates, converted to list for easier
    # iteration when checking whether one number bigger than all the list 
    return(list(around)) 

def check_is_low_point(map_matrix, row, column):
    check_num = map_matrix[row][column]
    around = find_around(map_matrix, row, column)
    if(all(check_num < num for num in around)):
        return(True)
    else:
        return(False)

risk = 0
for row in range(0, len(cave_map)):
    for column in range(0, len(cave_map[row])):
        if check_is_low_point(cave_map, row, column): 
            risk = risk + 1 + cave_map[row][column]

print("answer to part 1:", risk)

def check_from_point(map_matrix, row, col):
    checked = [] # by definition all checked will be in the basin
    nines = []
    to_check = [[row, col]] # starting point of basin bottom  
    n_row = len(map_matrix)
    n_col = len(map_matrix[0])
    
    while len(to_check) > 0: # cycle through to_check list from 0
        left_coords = [to_check[0][0], to_check[0][1] - 1]
        right_coords = [to_check[0][0], to_check[0][1] + 1]
        above_coords = [to_check[0][0] - 1, to_check[0][1]]
        below_coords = [to_check[0][0] + 1, to_check[0][1]]
        
        if left_coords not in to_check and left_coords not in checked:
            if left_coords[1] >= 0: # check not left beyond matrix
                if map_matrix[left_coords[0]][left_coords[1]] == 9:
                    nines.append(left_coords)
                else:
                    to_check.append(left_coords)
        # check right if not already to be checked or been checked
        if right_coords not in to_check and right_coords not in checked:
            if right_coords[1] < n_col: # check not right beyond matrix
                if map_matrix[right_coords[0]][right_coords[1]] == 9:
                    nines.append(right_coords)
                else:
                    to_check.append(right_coords)
        # check above if not already to be checked or been checked
        if above_coords not in to_check and above_coords not in checked:
            if above_coords[0] >= 0: # check not above top row
                if map_matrix[above_coords[0]][above_coords[1]] == 9:
                    nines.append(above_coords)
                else:
                    to_check.append(above_coords)
        # check below if not already to be checked or been checked
        if below_coords not in to_check and below_coords not in checked:
            if below_coords[0] < n_row: # check not below bottom row
                if map_matrix[below_coords[0]][below_coords[1]] == 9:
                    nines.append(below_coords)
                else:
                    to_check.append(below_coords)
        
        checked.append(to_check[0])
        del to_check[0] # remove it now it's checked
    
    return(len(checked))

basin_sizes = []
# note - need to re-find all low points since didn't bother for part 1
for row in range(0, len(cave_map)): 
    for column in range(0, len(cave_map[row])):
        if check_is_low_point(cave_map, row, column): 
            basin_sizes.append(check_from_point(cave_map, row, column))

basin_sizes.sort()

print("answer to part 2:", basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
