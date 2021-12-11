# Solution for day 7

# parse first as csv to avoid /n at end 
# then put into list of numbers as integers - as with day 6
import csv
with open('input_07.txt', mode ='r')as file:
#with open('example_input_07.txt', mode ='r') as file:
    csv_file = csv.reader(file)

    numbers = []
    for line in csv_file:
        for number in line:
            numbers.append(int(number))

# Slowly move from outside in, keeping track of how many moves required
# Always move from the furthest value with the fewest crabs
cform = numbers[:] # cform for crab formation
# Run until all in same position, tracking movements made
fuel_counter = 0
while not all(pos == cform[0] for pos in cform):

    lowest_pos = min(cform)
    highest_pos = max(cform)
    n_at_min = len([pos for pos in cform if lowest_pos == pos])
    n_at_max = len([pos for pos in cform if highest_pos == pos])

    # or equal to for cases of tie where it doesn't matter
    if n_at_min <= n_at_max: 
        for pos in range(0, len(cform)):
            if cform[pos] == lowest_pos:
                cform[pos] = cform[pos] + 1
                fuel_counter = fuel_counter + 1
    else:
        for pos in range(0, len(cform)):
            if cform[pos] == highest_pos:
                cform[pos] = cform[pos] - 1
                fuel_counter = fuel_counter + 1

print("Answer 1:", fuel_counter)

# Need to track extra fuel consumption from top and from bottom
cform = numbers[:] 
fuel_counter = 0
top_fuel_extra = 0
bottom_fuel_extra = 0
while not all(pos == cform[0] for pos in cform):

    lowest_pos = min(cform)
    highest_pos = max(cform)
    cost_bot = len([pos for pos in cform if lowest_pos == pos]) + \
                    bottom_fuel_extra

    cost_top = len([pos for pos in cform if highest_pos == pos]) + \
                    top_fuel_extra

    if cost_bot <= cost_top:
        fuel_counter = fuel_counter + bottom_fuel_extra # for extra price
        for pos in range(0, len(cform)):
            if cform[pos] == lowest_pos:
                cform[pos] = cform[pos] + 1
                fuel_counter = fuel_counter + 1
                bottom_fuel_extra = bottom_fuel_extra + 1
    else:
        fuel_counter = fuel_counter + top_fuel_extra # for extra price
        for pos in range(0, len(cform)):
            if cform[pos] == highest_pos:
                cform[pos] = cform[pos] - 1
                fuel_counter = fuel_counter + 1 
                top_fuel_extra = top_fuel_extra + 1 

print("Answer 2:", fuel_counter)

