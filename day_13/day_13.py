# solution for day 13

# read in without splitting so can split on empty line between hash coordinates
# and fold instructions
#with open("example_input_13.txt", "r") as file:
with open("input_13.txt", "r") as file:
    raw_input = file.read()

dot_paper_raw = raw_input.split("\n\n")[0]
fold_inst_raw = raw_input.split("\n\n")[1]

dot_paper_list = dot_paper_raw.split("\n")
dot_paper = []
for i in dot_paper_list:
    split = i.split(",")
    dot_coord = []
    for j in split:
        j = int(j)
        dot_coord.append(j)
    dot_paper.append(dot_coord)
      
fold_inst_list = fold_inst_raw.split("\n")

# Get rid of extra empty line in folds
while("" in fold_inst_list ) :
    fold_inst_list.remove("")

fold_inst_list
fold_inst = []
for i in fold_inst_list:
    split = i.split("=")
    fold_in = split[0].split()
    fold_inst.append([fold_in[2], int(split[1])])

def fold_paper(paper, instruction):
    if instruction[0] == "x":
        index = 0 # will need row coords since x is vertical fold
    if instruction[0] == "y":
        index = 1
    
    for coord in paper:
        gap = coord[index] - instruction[1]
        if gap > 0:
            coord[index] = coord[index] - (2 * gap)

    return paper

# Ideally I would have the fold_paper function run everything through into a
# set and then back out into a smaller list, meaning I could just count the
# items in the folded paper list. However this was getting annoying because to 
# get the items into a set they need to be tuples, and that causes issues with 
# indexing them, so it was actually easier to just keep the full list and 
# turn it to a set only when necessary for counting. 
def count_dots(paper):
    dot_set = set()
    for dot in paper:
        dot_set.add(tuple(dot))

    return(len(dot_set))

fold_paper(dot_paper, fold_inst[0])
print("answer to part 1:", count_dots(dot_paper))

fold_inst = fold_inst[1:]
for instruction in fold_inst:
    fold_paper(dot_paper, instruction)

def show_print_out(folded_paper):
    n_row = 0
    n_col = 0
    for i in folded_paper:
        if i[0] > n_col: n_col = i[0] + 1
        if i[1] > n_row: n_row = i[1] + 1
    
    printout = []
    for i in range(0,n_row):
        row_out = []
        for j in range(0,n_col):
            if [j,i] in folded_paper:
                row_out.append("#")
            else:    
                row_out.append(".")
        printout.append("  ".join(row_out))
        #print("  ".join(row_out))

    return printout

final_printout = show_print_out(dot_paper)

print("answer to part 2:")
for i in final_printout: 
    print(i)

