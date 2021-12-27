# day 16

with open("example_input_16.txt", "r") as file:
#with open("input_16.txt", "r") as file:
    raw_input = file.read().strip("\n")

hex_dict = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
    }

bin_input = "".join([hex_dict[i] for i in raw_input])

def parse_header(string):
    return int(string[0:3], 2), int(string[3:6], 2)

def parse_literal(string):
    i = 6
    number = ""
    last_digit = False
    while last_digit == False:
        number += string[i + 1: i + 5] 
        if string[i] == "0":
            last_digit = True
        i += 5
    # find how many zeroes needed by seeing what is left over after
    # divided by four operation
    length = i + ((i - 6) % 4)
    # also return whole length
    return (int(number, 2), length)

def get_length_zero_operator(string):
    length_subpackets = int(string[7:22], 2)
    i = 22 + length_subpackets
    #while string[i] == "0":
        #print(i)
        #i += 1
    return i

def get_length_one_operator(string):
    number_subpackets = int(string[7:18], 2)
    return number_subpackets 

#test = "8A004A801A8002F478"
test = "620080001611562C8802118E34"

tester = "".join([hex_dict[i] for i in test])
print(tester)
print(parse_header(tester))
print(get_length_one_operator(tester))
#print(parse_header(test))
#print(parse_literal(test))
#print(get_length_one_operator(test))
        


