import numpy as np

with open("puzzle08") as file:
    puzzle = [[int(item) for item in line.strip()] for line in file]

puzzle = np.array(puzzle)
counter = np.zeros([len(puzzle), len(puzzle[0])])

def visibleTreeCheckerRow(index, row1):
    for c, num in enumerate(row1):
        if 0 < index < len(puzzle)-1 and 0 < c < len(row1)-1:
            if np.all(row1[:c] < num):
                counter[index][c] = 1
    for i, item in enumerate(reversed(row1)):
        if 0 < index < len(puzzle)-1 and 0 < i < len(row1)-1:
            if np.all(row1[-i:] < item):
                counter[index][-i-1] = 1

def visibleTreeCheckerColumn(index, column):
    for c, num in enumerate(column):
        if 0 < index < len(puzzle)-1 and 0 < c < len(column)-1:
            if np.all(column[:c] < num):
                counter[c][index] = 1
    for i, item in enumerate(reversed(column)):
        if 0 < index < len(puzzle)-1 and 0 < i < len(column)-1:
            if np.all(column[-i:] < item):
                counter[-i-1][index] = 1

for r, row in enumerate(puzzle):
    visibleTreeCheckerRow(r, row)
    visibleTreeCheckerColumn(r, puzzle[:, r])

print('Part 1:', np.count_nonzero(counter == 1)+len(puzzle[0])*4 - 4)

# Part 2

scenicScore = 0

def scenicScoreColumn(column, index, item):
    score = 0
    view = []
    view1 = []
    for i in reversed(column[:index]):
        if i <= item:
            view.append(i)
        if i >= item:
            break
    for l in column[index+1:]:
        if l <= item:
            view1.append(l)
        if l >= item:
            break
    if score < len(view)*len(view1):
        score = len(view)*len(view1)
    return score

def scenicScoreRow(row2, index):
    score = 0
    view = []
    view1 = []
    for y, item in enumerate(row2):
        view = []
        view1 = []
        for i in reversed(row2[:y]):
            if i <= item:
                view.append(i)
            if i >= item:
                break
        for l in row2[y+1:]:
            if l <= item:
                view1.append(l)
            if l >= item:
                break
        if score < len(view)*len(view1)*scenicScoreColumn(puzzle[:, y], index, item):
            score = len(view)*len(view1)*scenicScoreColumn(puzzle[:, y], index, item)
    return score

for x, line in enumerate(puzzle):
    if scenicScoreRow(line, x) > scenicScore:
        scenicScore = scenicScoreRow(line, x)

print('Part 2:', scenicScore)
