# fancier solution to day 1 that is at least a bit extensible

file = open("input_1a.txt", "r")
num_list_as_string = file.read().splitlines()
while("" in num_list_as_string ) :
    num_list_as_string.remove("")

num_list = [int(i) for i in num_list_as_string]

def window_check(window_length, num_list, jump_number):
    increasing_counter = 0
    for i in range(0,len(num_list) - 1 - window_length):
        this_window = sum(num_list[i : (i + window_length)])
        next_window = sum(num_list[(i + jump_number) : 
                              (i + window_length + jump_number)])
        if this_window < next_window:
            increasing_counter = increasing_counter + 1
    return(increasing_counter)         

print("Solution to part 1:", window_check(1, num_list, 1))
print("Solution to part 2:", window_check(3, num_list, 1))
