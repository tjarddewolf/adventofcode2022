from collections import OrderedDict
import string
import re
import numpy as np

with open('day4/day4.txt') as f:
    data = f.read().split('\n')

count_2 = 1000
count_individual = 0
for i in data:
    numbers = re.findall(r'\d+', i)
    numbers_int = [int(x) for x in numbers]

    #part 1
    numbers = numbers_int
    if numbers[0] >= numbers[2] and numbers[1] <= numbers[3]:
        count_individual += 1
    elif numbers[0] <= numbers[2] and numbers[1] >= numbers[3]:
        count_individual += 1

    #part 2

    if numbers[0] < numbers[2] and numbers[1] < numbers[2]:
        print(numbers)
        count_2 -= 1
    elif numbers[0] > numbers[3] and numbers[1] > numbers[3]:
        print(numbers)
        count_2 -= 1

print(count_individual, count_2)
