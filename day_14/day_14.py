# solution for day 14

with open("example_input_14.txt", "r") as file:
#with open("input_14.txt", "r") as file:
    raw_input = file.read().splitlines()

template = raw_input[0]
pair_insertion_rules = raw_input[2:]

rules = {}
for line in pair_insertion_rules:
    split = line.split(" -> ")
    rules.update({split[0]: split[1]})

def insert_polymer(template, rules):
    # add first value by default because always the same
    new_template = [template[0]]
    for i in range(1,len(template)):
        to_insert = rules["".join([template[i - 1], template[i]])]
        new_template.append(to_insert)
        new_template.append(template[i]) 
    return new_template


polymer = list(template)
for i in range(0,10):
    polymer = insert_polymer(polymer, rules)

def score_polymer(template, rules, polymer):
    # cycle through template and rules for set of possible letters 
    letter_set = set()
    for letter in template:
        letter_set.add(letter)
    for letter in rules.values():
        letter_set.add(letter)

    max_letter_count = 0
    min_letter_count = len(polymer)
    
    for letter in letter_set:
        if polymer.count(letter) > max_letter_count:
            max_letter_count = polymer.count(letter) 
        if polymer.count(letter) < min_letter_count:
            min_letter_count = polymer.count(letter) 

    return(max_letter_count - min_letter_count)

print("answer 1:", score_polymer(template, rules, polymer))

# tried just re-running it but it is way too inefficient to work
# I think we need to do what we did in the case a few days ago
# for the fish reproduction, and have a list of which
# combinations are in the polymer, with a process to see
# which combinations will be there after updating.





#print("answer 2:", score_polymer(template, rules, polymer))

