import re
from itertools import groupby

with open("puzzle11") as file:
    puzzle = [line.strip().replace('Operation: new = ', '') for line in file]
    puzzle = [list(sub) for ele, sub in groupby(puzzle, key=bool) if ele]

for row, monkey in enumerate(puzzle):
    puzzle[row][1] = [int(s) for s in re.findall(r'\b\d+\b', monkey[1])]
    puzzle[row][2] = monkey[2].split()
    puzzle[row][3] = int(''.join(filter(str.isdigit, monkey[3])))
    puzzle[row][4] = int(''.join(filter(str.isdigit, monkey[4])))
    puzzle[row][5] = int(''.join(filter(str.isdigit, monkey[5])))

def monkeyOperation(currentItem, action1, operation, action2):
    op = {'+': lambda x, y: x + y,
          '*': lambda x, y: x * y}
    if action1 == 'old':
        action1 = currentItem
    if action2 == 'old':
        action2 = currentItem
    return op[operation](int(action1), int(action2))

counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

shenanigans = 0
while shenanigans < 20:
    for ID, monk in enumerate(puzzle):
        for position, item in enumerate(monk[1]):
            item = monkeyOperation(item, monk[2][0], monk[2][1], monk[2][2])//3
            counter[ID] += 1
            if item % monk[3] == 0:
                puzzle[monk[4]][1].append(item)
            else: puzzle[monk[5]][1].append(item)
        del puzzle[ID][1][:]
    shenanigans += 1

monkeyBusiness = sorted(list(counter.values()))
print('Part 1:', monkeyBusiness[-2]*monkeyBusiness[-1])
