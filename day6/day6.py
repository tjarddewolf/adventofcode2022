import string

with open('day6/day6.txt') as f:
    data =[]
    data[:0] = f.read()

# print(data)

#create ordered dict with 52 values
# value_dict = dict(zip(string.ascii_lowercase, range(1,27)))
#
# for i in range(3, len(data)):
#     compare_data = data[i-3:i+1]
#     if len(compare_data) == len(set(compare_data)):
#         print(i+1, compare_data)
#

# #test data
# data[:0] = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# print(data)
def compare_info(data, match_number):
    for i in range(match_number-1, len(data)):
        compare_data = data[i-match_number+1:i+1]
        if len(compare_data) == len(set(compare_data)):
            return(i+1, compare_data)

p1 = compare_info(data, 4)
p2 = compare_info(data, 14)

print(p1, p2)
