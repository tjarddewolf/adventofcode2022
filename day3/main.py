from collections import OrderedDict
import string

with open('day3/day3.txt') as f:
    data = f.read().split('\n')

#create ordered dict with 52 values
value_dict = dict(zip(string.ascii_letters, range(1,53)))


#determine first and second half, calculate the intersect (i.e. what is in both) then run it through the above dict
count = 0
for string in data:
    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
    intersect = ''.join(set(firstpart).intersection(secondpart))

    for i in intersect:
        count += value_dict[i]

print(count)

#part 2
count2 = 0
for i in range(0, len(data), 3):
    intersect = ''.join(set(data[i]).intersection(data[i+1]).intersection(data[i+2]))

    for i in intersect:
        count2 += value_dict[i]

print(count2)


