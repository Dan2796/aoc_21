# Solution for day 4

file = open("input_4.txt", "r")
lines = file.read().splitlines()
bingo_numbers_str = lines[0].split(",")
bingo_numbers = [int(i) for i in bingo_numbers_str]

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

#for i in cards:
    #print(i)


