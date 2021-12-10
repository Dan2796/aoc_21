# solution for day 10

#with open("example_input_10.txt", "r") as file:
with open("input_10.txt", "r") as file:
    lines = file.read().splitlines()

syntax = []
for line in lines: syntax.append(list(line)) 

openers = ["{", "(", "[", "<"]
closers = ["}", ")", "]", ">"]

def reverse_bracket(bracket):
    if bracket == "(":
        return(")")
    if bracket == "[":
        return("]")
    if bracket == "{":
        return("}")
    if bracket == "<":
        return(">")

def score_wrong_bracket(bracket):
    if bracket == ")":
        score = 3
    if bracket == "]":
        score = 57
    if bracket == "}":
        score = 1197
        return(1197)
    if bracket == ">":
        score = 25137
    return score

def find_syntax_mismatch_score(line):
    to_close = []
    score = 0
    for bracket in line:
            if bracket in openers:
                to_close.append(bracket)
            if bracket in closers:
                if bracket == reverse_bracket(to_close[-1]):
                    del to_close[-1]
                else:
                    return score_wrong_bracket(bracket)
                    break

                    #score = score_wrong_bracket(bracket)
    return score

score_counter = 0
for line in syntax:
    score_counter += find_syntax_mismatch_score(line)

print("answer 1:", score_counter)

not_corrupt = []
for line in syntax:
    if find_syntax_mismatch_score(line) == 0:
        not_corrupt.append(line)

def find_complete_line_string(line):
    to_close = []
    for bracket in line:
            if bracket in openers:
                to_close.append(bracket)
            if bracket in closers:
                if bracket == reverse_bracket(to_close[-1]):
                    del to_close[-1]
    
    closing_string = []
    for bracket in to_close:
        # prepend to get right order, and reverse for closing bracket
        closing_string.insert(0, reverse_bracket(bracket)) 
    return closing_string

def score_completed_string(closing_string):
    score = 0
    for bracket in closing_string:
        score = score * 5
        if bracket == ")":
            score += 1
        if bracket == "]":
            score += 2
        if bracket == "}":
            score += 3
        if bracket == ">":
            score += 4
    return score

score_list = []
for line in not_corrupt:
    score_for_line = score_completed_string(find_complete_line_string(line))
    score_list.append(score_for_line)
    score_list.sort()

list_length = int(len(score_list) / 2)
print("answer to part 2:", score_list[list_length])

