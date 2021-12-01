import os
from pprint import pprint

numbers = []


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/day1.txt')
with open(filename, "r") as f:   
    for line in f:
        numbers.append(int(line))


increase = 0
decrease = 0
same = 0

three_sum = []

for i in range(0,len(numbers)):
    try:
        three_sum.append(numbers[i] + numbers[i+1] + numbers[i+2])
    except IndexError:
        print("done with reading")

last_number = three_sum[0]

for number in three_sum[1:]:
    if number == last_number:
        print(str(number) + "(same)")
        same += 1
    elif number > last_number:
        print(str(number) + "(increased)")
        increase += 1
    elif number < last_number:
        print(str(number) + "(decreased)")
        decrease += 1
    else:
        print("error")
    last_number = number

print("Increased: " + str(increase))
print("decreased: " + str(decrease))
print("Stayed the same: " + str(same))


