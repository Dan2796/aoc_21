# Solution for day 3

file = open("input_03.txt", "r")
lines = file.read().splitlines()

gamma_list = list()
for digit in range(0,len(lines[1])):
    digit_sum = sum([int(x[digit]) for x in lines])
    rounded_average = round(digit_sum / len(lines))
    gamma_list.append(rounded_average)

def reverse_binary(bin_list):
  new_bin_list = [0 if x == 1 else 1 for x in bin_list]
  return(new_bin_list)

epsilon_list = reverse_binary(gamma_list)

epsilon_as_bin = "".join(str(digit) for digit in epsilon_list)
gamma_as_bin = "".join(str(digit) for digit in gamma_list)

epsilon_rate = int(epsilon_as_bin,2)
gamma_rate = int(gamma_as_bin,2)

print("Solution to part 1:", int(epsilon_rate) * int(gamma_rate))

oxygen_list = lines
iterator = 0
while len(oxygen_list) > 1:
    digit_sum = sum([int(x[iterator]) for x in oxygen_list])
    if (digit_sum / len(oxygen_list)) == 0.5:
      oxygen_list = [i for i in oxygen_list if i[iterator] == "1"]
    else:
      rounded_average = round(digit_sum / len(oxygen_list))
      oxygen_list = [i for i in oxygen_list if i[iterator] == 
              str(rounded_average)]
    iterator = iterator + 1

oxygen_rate = int(oxygen_list[0], 2)

co2_list = lines
iterator = 0
while len(co2_list) > 1:
    digit_sum = sum([int(x[iterator]) for x in co2_list])
    if (digit_sum / len(co2_list)) == 0.5:
        co2_list = [i for i in co2_list if i[iterator] != "1"]
    else:
        rounded_average = round(digit_sum / len(co2_list))
        co2_list = [i for i in co2_list if i[iterator] != 
                str(rounded_average)]
    iterator = iterator + 1

co2_rate = int(co2_list[0], 2)

print("Solution to part 2:", oxygen_rate * co2_rate)

