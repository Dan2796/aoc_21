# solution for day 15
# with help from Elliot!

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
print(risk)


