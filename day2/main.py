with open('day2/day2.txt') as f:
    data = f.read().split('\n')


value_dict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

total_sum = 0
for i in data:
    total_sum += value_dict[i]

print(total_sum)

value_dict_2 = {
    "A X": 3, #rock + scissors = lose (3+0)
    "A Y": 4, #rock + rock = draw  (3+1)
    "A Z": 8, #rock + paper = win (6+2)
    "B X": 1, #paper + rock = lose = 1
    "B Y": 5, # paper + paper = 3 + 2
    "B Z": 9, #paper + scissors = 6+3
    "C X": 2, #scissors + paper = 0 + 2
    "C Y": 6, #scissors + scissors = 3 + 3
    "C Z": 7 #scissors + rock = 6 + 1
}

total_sum_2 = 0
for i in data:
    total_sum_2 += value_dict_2[i]

print(total_sum_2)