# solution for day 15
# with help from Elliot on part 1!

#with open("example_input_15.txt", "r") as file:
with open("input_15.txt", "r") as file:
    raw_input = file.read().splitlines()

# put in as dictionary coordinate -> value
cave_width = len(raw_input[0])
cave_height = len(raw_input)

cave = {}
for row in range(0, cave_height):
  for col in range(0, cave_width):
      cave[(row, col)] = int(raw_input[row][col])

def neighbours(coordinate, closed_set):
    i,j = coordinate
    around = [(i - 1,j    ),
              (i    , j - 1),
              (i + 1, j    ),
              (i    , j + 1)]
    return [(c, cave[c]) for c in around if c in cave and c not in closed_set]

import heapq # automates prioritisation
from collections import defaultdict
import sys
# astar algo for searching shortest path
# g-score cost to get to the coordinate
# f-score cost to get to the coordinate + estimate cost to end
def astar(start, goal, heuristic):
    open_set = []
    closed_set = {}
    # default dict will give back max size (infinity) if the key you asked for
    # doesn't exist
    gscore = defaultdict(lambda: sys.maxsize) 
    gscore[start] = 0 
    # element start is into the queue, with a cost of zero
    heapq.heappush(open_set, (heuristic(start), start))
    while open_set: # open_set not empty
        fscore, current = heapq.heappop(open_set)
        if current == goal:
            return total_risk(closed_set, goal)
        for n, nrisk in neighbours(current, closed_set):
            temp_gscore = gscore[current] + nrisk
            if temp_gscore < gscore[n]: 
                gscore[n] = temp_gscore 
                closed_set[n] = (current, nrisk)
            # zip changes list of tuples to tuple of lists, so we get the 
            # first thing from every single tuple
            if not any(n == k for k,v in open_set):
                heapq.heappush(open_set, (temp_gscore + heuristic(n), n))
    return None

def total_risk(closed_set, goal):
    risk = 0
    path = {}
    current = goal
    while current in closed_set:
        parent, r = closed_set[current]
        risk += r
        path[current] = r
        current = parent
    return (risk, path)

def manhattan_distance(n):
    # also known as taxi cab distance
    return cave_width - n[0] + cave_height - n[1]

# can print cave path if you want
risk, path =  astar((0,0), (cave_width - 1, cave_height - 1), manhattan_distance)
#for row in range(0, cave_height):
#    line = ""
#    for col in range(0, cave_width):
#        line += str(path[(row,col)]) if (row,col) in path else " "
#    print(line)
print("answer to part 1:", risk)


# brute forcing an input change to get out the five by five grid
def cycle_add(number, to_add):
    new_number = number + to_add 
    over = new_number - 9
    if over > 0:
        new_number = over
    return new_number

def add_to_row(row, to_add):
    return "".join([str(cycle_add(int(i), to_add)) for i in row])

def row_times_five(row):
    return row + add_to_row(row, 1) + \
               add_to_row(row, 2) + \
               add_to_row(row, 3) + \
               add_to_row(row, 4) 

new_input = []

for j in range(0,5):
    for row in raw_input:
        new_input.append(add_to_row(row, j))

part_2_input = []
for row in new_input:
    part_2_input.append(row_times_five(row))

# redraw cave with coordinates
cave_width = len(part_2_input[0])
cave_height = len(part_2_input)

cave = {}
for row in range(0, cave_height):
  for col in range(0, cave_width):
      cave[(row, col)] = int(part_2_input[row][col])

risk, path =  astar((0,0), (cave_width - 1, cave_height - 1), manhattan_distance)
print("answer to part 2:", risk)

