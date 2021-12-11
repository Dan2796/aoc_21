# solution to day 2

file = open("input_02.txt", "r")
lines = file.read().splitlines()
instructions = list(map(lambda x: x.split(), lines))

forward_counter = 0
depth_counter = 0

for move in range(0,len(instructions)):
    if instructions[move][0] == "forward":
        forward_counter = forward_counter + int(instructions[move][1])
    if instructions[move][0] == "down":
        depth_counter = depth_counter + int(instructions[move][1])
    if instructions[move][0] == "up":
        depth_counter = depth_counter - int(instructions[move][1])

print("Solution to part 1:", depth_counter * forward_counter)

forward_counter = 0
depth_counter = 0
aim_counter = 0

for move in range(0,len(instructions)):
    if instructions[move][0] == "forward":
        forward_counter = forward_counter + int(instructions[move][1])
        depth_counter = depth_counter + aim_counter * int(instructions[move][1])
    if instructions[move][0] == "down":
        aim_counter = aim_counter + int(instructions[move][1])
    if instructions[move][0] == "up":
        aim_counter = aim_counter - int(instructions[move][1])

print("Solution to part 2:", depth_counter * forward_counter)


