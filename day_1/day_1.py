# solution to day 1

file = open("input_1.txt", "r")
lines = file.readlines()

increasing_counter = 0
for i in range(0,len(lines) - 2):
    if int(lines[i]) < int(lines[i+1]):
        increasing_counter = increasing_counter + 1

print("Solution to part 1:", increasing_counter)

three_window_counter = 0
for i in range(0,(len(lines) - 4)):
    if (int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) < 
          int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])):
        three_window_counter = three_window_counter + 1

print("Solution to part 2:", three_window_counter)

