# solution for day 14

#with open("example_input_14.txt", "r") as file:
with open("input_14.txt", "r") as file:
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
    for letter in template: letter_set.add(letter)
    for letter in rules.values(): letter_set.add(letter)

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

# start with getting the rules into a form of combo -> two new combos
combo_rules = {}
for lhs in rules.keys():
    new_combo_1 = "".join([lhs[0], rules[lhs]])
    new_combo_2 = "".join([rules[lhs], lhs[1]])
    combo_rules.update({lhs: [new_combo_1, new_combo_2]})

combo_set = set()
for lhs in combo_rules.keys():
    combo_set.add(lhs)
for rhs in combo_rules.values():
    combo_set.add(rhs[0])
    combo_set.add(rhs[1])

# blank tracker just with the possible combos counted at 0
blank_tracker = {}
for combo in combo_set:
    blank_tracker.update({combo: 0})
# tracker based on template starting values:
template_combos = []
for i in range(0, len(template) - 1):
    template_combos.append("".join([template[i], template[i + 1]]))
combo_tracker = {}
for combo in combo_set:
    combo_tracker.update({combo: template_combos.count(combo)})

# now need a function to update a polymer of combinations
import copy
def combo_tracker_update(combo_tracker, blank_tracker, combo_rules):
    new_tracker = copy.deepcopy(blank_tracker)
    for combo in combo_tracker.keys():
        current_number = combo_tracker[combo]
        #print(new_tracker[combo_tracker[combo][0]])
        new_tracker[combo_rules[combo][0]] += current_number
        new_tracker[combo_rules[combo][1]] += current_number
    
    return(new_tracker)

for i in range(0,40):
    combo_tracker = combo_tracker_update(combo_tracker, 
                                         blank_tracker, 
                                         combo_rules)

# now need to get the combo keys into a list of letter keys
# note can still rely on just raw template and rules for letter set
def count_letters_in_tracker(template, rules, combo_template):
    letter_counter = {}
    letter_set = set()
    for letter in template: letter_set.add(letter)
    for letter in rules.values(): letter_set.add(letter)
    for letter in letter_set: letter_counter.update({letter:0})
 
    # need to halve since all letters (except first and last in template) will
    # be double counted in combinations
    letter_counter[template[0]] += 0.5 # to double count the first combo
    letter_counter[template[-1]] += 0.5 # to double count the last combo
    for combo in combo_tracker.keys():
        letter_counter[combo[0]] += (combo_tracker[combo] / 2)
        letter_counter[combo[1]] += (combo_tracker[combo] / 2)
     
    return letter_counter

count = count_letters_in_tracker(template, rules, combo_tracker)

print("answer 2:", int(max(count.values()) - min(count.values())))

