# Solution for day 7

# Pretty poorly written for part 2, but it does work...

#with open("example_input_7.txt", "r") as file:
with open("input_7.txt", "r") as file:
    lines = file.read().splitlines()

second_segments = []
for line in lines:
    second_half = line.split("| ")[1].split(" ")
    for code in second_half:
        second_segments.append(code)

unique_num_counter = 0
unique_len_values = [2, 4, 3, 7]
for code in second_segments:
    if len(code) in unique_len_values:
        unique_num_counter = unique_num_counter + 1

print("Answer 1:", unique_num_counter)

# Get a dictionary of unique numbers out of the whole line - letters are 
# stored as a set to avoid order issues, so that it's easy later to check
# whether a given letter code includes a letter found in one of the four
# unique numbers
def decode_uniques(full_line):
    unique_letter_sets = {}
    for i in range(0, len(full_line)):
        if len(full_line[i]) == 2:
            unique_letter_sets["one"] = set(full_line[i])
        if len(full_line[i]) == 4:
            unique_letter_sets["four"] = set(full_line[i])
        if len(full_line[i]) == 3:
            unique_letter_sets["seven"] = set(full_line[i])
        if len(full_line[i]) == 7:
            unique_letter_sets["eight"] = set(full_line[i])
    return(unique_letter_sets)

# Check whether every line has all four unique numbers to make sure
# I can do a set of simple rules - they do!
for line in lines:
    line = line.split(" ")
    if len(decode_uniques(line)) != 4:
        print("Missing a number")

# Decode codes of lengths five, based on the letters they share in common with
# the unique numbers
def decode_twofivethree(uniques, letter_code):
    decoded = ""
    while decoded == "":
        # If contains all numbers in 1, then it's a 3
        if all(letter in letter_code for letter in uniques["one"]):
            return(3)
            decoded = "done"
        # check if it contains three letters from the four code
        how_many_in_four = 0
        for letter in letter_code:
            if letter in uniques["four"]:
                how_many_in_four = how_many_in_four + 1
        if how_many_in_four == 2:
            return(2)
            decoded = "done"
        return(5) # back up if other two conditions not satisfied
        decoded = "done"
    return(decoded)

# Decode codes of lengths six based on the letters they share in common with 
# the unique numbers
def decode_zerosixnine(uniques, letter_code):
    decoded = ""
    while decoded == "":
        # If does not contain all numbers in 1, then it's a 6
        if not all(letter in letter_code for letter in uniques["one"]):
           return(6)
           decoded = "done"
        # Check if it's 9 based on how many letters in four code
        how_many_in_four = 0
        for letter in letter_code:
            if letter in uniques["four"]:
                how_many_in_four = how_many_in_four + 1
        if how_many_in_four == 4:
           return(9)
           decoded = "done"
        return(0) # back up if other two conditions not satisfied
        decoded = "done"

# Take a line and spit out the digit for each letter code, based on the length
# and then either directly translating it from the length, or applying
# the functions above in the cases of ambiguous five and six letter length
# codes
def decode_output(full_line):
    output = full_line.split("| ")[1].split(" ")
    full_line = full_line.split(" ") # leaves in "|", just gets ignored
    uniques = decode_uniques(full_line)
    
    output_as_digits = []
    for i in output:
        if len(i) == 2: 
            output_as_digits.append(1)
        elif len(i) == 4: 
            output_as_digits.append(4)
        elif len(i) == 3: 
            output_as_digits.append(7)
        elif len(i) == 7: 
            output_as_digits.append(8)
        elif len(i) == 5: # could be 2, 3 or 5
            output_as_digits.append(decode_twofivethree(uniques, i))
        elif len(i) == 6: # could be 0, 6 or 9
            output_as_digits.append(decode_zerosixnine(uniques, i))
        else:
            output_as_digits.append("???")
    return(output_as_digits)

# Go through the full text input and get an integer from each decoded output 
# list. Score is just kept with count of with a counter because it's easy.
total = 0
for line in lines:
    total = total + int(''.join(map(str, decode_output(line))))

print("Answer 2:", total)
