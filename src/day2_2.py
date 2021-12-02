import os
from pprint import pprint


instructions = []


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/day2.txt')
with open(filename, "r") as f:   
    for line in f:
        instructions.append(line.split())

depth = 0
horizontal = 0
aim = 0

for instruction in instructions:
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
        depth += (int(instruction[1])*aim)
    elif instruction[0] == "up":
        aim -= int(instruction[1])
    elif instruction[0] == "down":
        aim += int(instruction[1])

print("Depth: " + str(depth)) 
print("Horizontal: " + str(horizontal))
print("Multiply: " + str(depth * horizontal))