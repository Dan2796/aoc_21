# solution for day 6

# parse first as csv to avoid /n at end
# then put into list of numbers as integers
import csv
with open('input_06.txt', mode ='r')as file:
#with open('example_input_06.txt', mode ='r') as file:
    csv_file = csv.reader(file)

    numbers = []
    for line in csv_file:
        for number in line:
            numbers.append(int(number))

# there's definitely a clever way to do this with maths since it's a sequence
# but it's a while since I had to do maths, so ima brute force it...

state = numbers[:] 
day = 1
fish_eggs = 0
while day <= 80:
    for i in range(0,len(state)):
        if state[i] == 0:
           state[i] = 6
           fish_eggs = fish_eggs + 1
        else:
            state[i] = state[i] - 1
    day = day + 1
    for egg in range(0,fish_eggs): 
        state.append(8)
    fish_eggs = 0

print("Answer to part 1:", len(state))

# Ok so that worked for short days, but my computer is taking too long for p2
# Have to be a little bit cleverer (though I'm sure there's still a maths
# trick I'm missing here).

# Can represent the number of fish more abstractly than a literal list of fish:
state = [0,0,0,0,0,0,0]
for fish_age in numbers:
    state[fish_age] = state[fish_age] + 1

day = 1
fish_babies = [0,0]
while day <= 256:
    # storing a value so the cycles can work without needing to be simultaneous
    babies_coming_of_age = fish_babies[0]
    fish_babies[0] = fish_babies[1]
    fish_babies[1] = state[0]
    # fish babies sorted, can rotate and add on the coming of age
    state = state[1:] + state[:1]
    state[6] = state[6] + babies_coming_of_age
    day = day + 1

print("Answer to part 2:", sum(state) + sum(fish_babies))


