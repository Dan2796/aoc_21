# Solution for day 4

file = open("input_4.txt", "r")
lines = file.read().splitlines()

# parse out the numbers from the first row 
bingo_numbers_str = lines[0].split(",")
bingo_numbers = [int(i) for i in bingo_numbers_str]

# parse out the bingo cards - transformed into nested lists (matricies)
bingo_cards_str = lines[1:]

i = 0
cards = []
while i < len(bingo_cards_str):
    card = bingo_cards_str[i+1:i+6]
    cards.append(card)
    i = i + 6

for i in range(0,len(cards)):
    for j in range(0, 5):
        cards[i][j] = cards[i][j].split()
        for num in range(0,5):
            cards[i][j][num] = int(cards[i][j][num])

def check_row_bingo(bingo_card, bingo_numbers):
    winning = "nah"
    row = 0
    while winning == "nah" and row <= 4:
        if all(item in bingo_numbers for item in bingo_card[row]):
            winning = "yes!"
        row = row + 1
    return(winning)

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] \
            for i in range(len(matrix[0]))]

# functions for checking (or transposing) single bingo card:
def unmarked_score(bingo_winner, bingo_numbers):
    unmarked_counter = 0
    for i in range(0,5):
        for j in range(0,5):
            if bingo_winner[i][j] not in bingo_numbers:
                unmarked_counter = unmarked_counter + bingo_winner[i][j]
    return(unmarked_counter)

# while loop breaks as soon as the answer is found - works via each card
# then each transposed card, then next card etc then add bingo_number and repeat
bingo_round = 1
bingo_answer = "not yet found"
while bingo_answer == "not yet found":
    bingo_called = bingo_numbers[0:bingo_round]

    for card in cards:
        if check_row_bingo(card, bingo_called) == "yes!":
             bingo_answer = unmarked_score(card, bingo_called) * \
                 bingo_called[-1]
        elif check_row_bingo(transpose_matrix(card), bingo_called) == "yes!":
             bingo_answer = unmarked_score(card, bingo_called) * \
                 bingo_called[-1]
    
    bingo_round = bingo_round + 1

print("Solution to part 1:", bingo_answer)



