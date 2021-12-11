# Solution for day 5

file = open("input_5.txt", "r")
#file = open("example_input.txt", "r")
lines = file.read().splitlines()

# Don't know how to use arrays, so will just have as four item lists
def array_to_list(array):
    new_array = array.replace(" -> ", ",")
    new_list = new_array.split(",")
    return(new_list)

coords = []
for array in lines:
    array = array_to_list(array)
    for i in range(0,4):
        array[i] = int(array[i])
    coords.append(array)

# Get rid of diaganol lines
horizontal = []
vertical = []
for line in coords:
    if line[0] == line[2]:
        vertical.append(line)
    if line[1] == line[3]:
        horizontal.append(line)

# Get list of points touched horizontally, then vertically
touched = []
for line in horizontal:
    for n in range(min(line[0], line[2]),max(line[0], line[2]) + 1):
        touched_coordinate = [n, line[1]]
        touched.append(touched_coordinate)
for line in vertical:
    for n in range(min(line[1], line[3]),max(line[1], line[3]) + 1):
        touched_coordinate = [n, line[1]]
        touched_coordinate = [line[0], n]
        touched.append(touched_coordinate)


# Check duplicates number
first_pass = list()
duplicated = set()
for coordinate in touched:
    if coordinate not in first_pass:
        first_pass.append(coordinate)
    else:
        duplicated.add(tuple(coordinate))
  
print("Solution to part 1:", len(duplicated))

# Now finding diaganol lines
diaganol = []
for line in coords:
    if line[0] != line[2] and line[1] != line[3]:
        diaganol.append(line)

# Mapping out points touched by the diaganol - hacky but it's part 2 and it
# works. Basically I have foure separate methods for the four distinct line
# directions. Using arrays properly would be nicer but it's a Sunday 
# and I want to go to the gym...

diaganol_touched = []
for line in diaganol:
    line_length = abs(line[0] - line[2]) + 1
    
    if line[0] < line[2] and line[1] < line[3]:
        for i in range(0,line_length):
            touched_coordinate = [line[0] + i, line[1] + i]
            diaganol_touched.append(touched_coordinate)
    elif line[0] > line[2] and line[1] < line[3]:
        for i in range(0,line_length):
            touched_coordinate = [line[0] - i, line[1] + i]
            diaganol_touched.append(touched_coordinate)
    elif line[0] < line[2] and line[1] > line[3]:
        for i in range(0,line_length):
            touched_coordinate = [line[0] + i, line[1] - i]
            diaganol_touched.append(touched_coordinate)
    elif line[0] > line[2] and line[1] > line[3]:
        for i in range(0,line_length):
            touched_coordinate = [line[0] - i, line[1] - i]
            diaganol_touched.append(touched_coordinate)

for coordinate in diaganol_touched:
    if coordinate not in first_pass:
        first_pass.append(coordinate)
    else:
        duplicated.add(tuple(coordinate))
  
print("Solution to part 2:", len(duplicated))




