import re
f = open("input.txt", "r")
lines = f.readlines()

total = 0

for line in lines:
    line = line.rstrip()
    digits = [char for char in line if char.isnumeric()]
    # print(digits)
    # print(digits[0], digits[-1])
    total += int(digits[0]+digits[-1])

print(total)