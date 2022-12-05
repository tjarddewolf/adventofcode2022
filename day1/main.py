# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


with open('day1.txt') as f:
    data = f.read().split('\n')

count = 0
max = 0
result = []
for i in data:
    if i != "":
        i = int(i)
        count += i
        if count > max:
            max = count

        result.append(int(count))
    else:
        count = 0

result.sort(reverse=True)

print(sum(result[0:3]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
