# solution for day 11

#with open("example_input_11.txt", "r") as file:
with open("input_11.txt", "r") as file:
    lines = file.read().splitlines()

input_map = []
for line in lines: 
    as_numbers = []
    for i in list(line):
        as_numbers.append(int(i))
    input_map.append(as_numbers) 
# make a deep copy for part 2 so can update input list in part 1
import copy
input_map_2 = copy.deepcopy(input_map)

# note it's inclusive; the inputted row and col are included in the outputted
# list of surrounding coordinates
def find_around(oct_map, row, col):
    # wasn't recognising inputs as integers for some reasons
    row = int(row)
    col = int(col)
    around = []
  
    for i in range((row - 1), (row + 2)):
        for j in range(col - 1, (col + 2)):
            around.append([i, j])
    
    # get rid of the ones 
    valid_around = []
    for point in around:
        if point[0] >= 0 and point[1] >= 0:
            if point[0] < len(oct_map) and point[1] < len(oct_map[0]): 
                valid_around.append(point)
    
    return(valid_around)

def burst(oct_map, row, col):
    row = int(row)
    col = int(col)
    
    # -9999 used for burst because it will never be added up to over zero by
    # mistake, and easier to use integer than string when doing the other 
    # additions and stuff
    for octopus in find_around(oct_map, row, col):
        if oct_map[octopus[0]][octopus[1]] != -9999:
            oct_map[octopus[0]][octopus[1]] += 1
    
    # mark has having burst
    oct_map[row][col] = -9999
    
    return(oct_map)

def add_one(oct_map):
    for row in range(0,len(oct_map)):
        for col in range(0, len(oct_map[0])):
            oct_map[row][col] += 1
    
    return oct_map

def burst_step(oct_map):
    all_bursted = False
    while all_bursted == False:
        # burst them all
        for row in range(0,len(oct_map)):
            for col in range(0, len(oct_map[0])):
                if oct_map[row][col] >= 0: # check not burst already this step
                    if oct_map[row][col] > 9: 
                        burst(oct_map,row,col)
        # check if bursted
        left_to_burst = 0
        for row in range(0,len(oct_map)):
            for col in range(0, len(oct_map[0])):
                if oct_map[row][col] > 9:
                    left_to_burst += 1
        if left_to_burst == 0:
            all_bursted = True

    return oct_map

def return_bursted_to_zero(oct_map):
    burst_this_round = 0
    for row in range(0,len(oct_map)):
        for col in range(0, len(oct_map[0])):
            if oct_map[row][col] <= 0: 
                oct_map[row][col] = 0
                burst_this_round += 1

    return [oct_map, burst_this_round]
    return oct_map

bursted_counter = 0
for step in range(0,100):
    input_map = add_one(input_map)
    input_map = burst_step(input_map)
    input_map = return_bursted_to_zero(input_map)[0]
    bursted_counter += return_bursted_to_zero(input_map)[1]

print("answer to part 1:", bursted_counter)

# Update the burst counter function to check for synchronisation
n_octopuses = len(input_map_2) * len(input_map_2[0])
def new_return_bursted_to_zero(oct_map):
    burst_this_round = 0
    for row in range(0,len(oct_map)):
        for col in range(0, len(oct_map[0])):
            if oct_map[row][col] <= 0: 
                oct_map[row][col] = 0
                burst_this_round += 1
    
    if burst_this_round == n_octopuses:
        return "it's finally happened!"
    else:
        return oct_map

step = 1

print(input_map_2)
while True:
  input_map_2 = add_one(input_map_2)
  input_map_2 = burst_step(input_map_2)
  if new_return_bursted_to_zero(input_map_2) == "it's finally happened!":
      print("answer to part 2:", step)
      break
  else:
    input_map_2 = new_return_bursted_to_zero(input_map_2)
  step += 1

