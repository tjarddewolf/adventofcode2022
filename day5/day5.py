import re


#parsing data solten from https://github.com/BastiaanRudolf/adventofcode22/blob/main/day5/solution.py
with open('day5/day5.txt') as f:
    lines = f.readlines()


def clean_crate(lst):
    return [re.findall('[A-Z]', s)[0] for s in lst if len(re.findall('[A-Z]', s)) > 0]

def get_starting_stack(lines):
    return [list(reversed(lst)) for lst in [clean_crate([line[i:i+4] for line in lines for i in range(0, len(line), 4)][x::9]) for x in range(9)]]

start_stack = get_starting_stack(lines[:8])

move_stack = lines[10:]
# print(move_stack)

# should have made this cleaner, but i'm updating the original lists rather than creating a new one so... It's messy
# #step 1
# def run_create():
#     global i
#
#     for i in move_stack:
#         numbers = re.findall(r'\d+', i)
#         numbers_int = [int(x) for x in numbers]
#
#         # determine items to move
#         to_move = start_stack[numbers_int[1] - 1][-numbers_int[0]:][::-1]
#
#         # add to correct line
#         start_stack[numbers_int[2] - 1] = start_stack[numbers_int[2] - 1] + to_move
#
#         # remove from line
#         start_stack[numbers_int[1] - 1] = start_stack[numbers_int[1] - 1][
#                                           :len(start_stack[numbers_int[1] - 1]) - numbers_int[0]]
#
#
# run_create()

#step 2
def question_2():
    global i

    for i in move_stack:
        numbers = re.findall(r'\d+', i)
        numbers_int = [int(x) for x in numbers]

        # determine items to move --> remove the last part comparedf to run-create from step 1
        to_move = start_stack[numbers_int[1] - 1][-numbers_int[0]:]

        # add to correct line
        start_stack[numbers_int[2] - 1] = start_stack[numbers_int[2] - 1] + to_move

        # remove from line
        start_stack[numbers_int[1] - 1] = start_stack[numbers_int[1] - 1][:len(start_stack[numbers_int[1] - 1]) - numbers_int[0]]


question_2()

for i in start_stack:
    print(i[-1])

