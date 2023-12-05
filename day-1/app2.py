import re
f = open("input.txt", "r")
lines = f.readlines()
word_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total1 = 0
total2 = 0

def change_line(line):
    for num, name in enumerate(word_numbers):
        # print(num, name)
        line = line.replace(name, f"{name}{num}{name}")
    return line

for line in lines:
    line = line.rstrip()
    digits = [char for char in line if char.isnumeric()]
    if digits:
        print(digits)
        print(digits[0], digits[-1])
        total1 += int(digits[0]+digits[-1])

    digits = [char for char in change_line(line) if char.isnumeric()]
    total2 += int(digits[0]+digits[-1])
    

print(total1, total2)



