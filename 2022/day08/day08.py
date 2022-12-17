import numpy as np

with open("puzzle08") as file:
    puzzle = [[int(item) for item in line.strip()] for line in file]

puzzle = np.array(puzzle)
counter = np.zeros([len(puzzle), len(puzzle[0])])

def visibleTreeCheckerRow (index, rowOrColumn):
    for c, num in enumerate(rowOrColumn):
        if 0 < index < len(puzzle)-1 and 0 < c < len(rowOrColumn)-1:
            if np.all(rowOrColumn[:c] < num):
                counter[index][c] = 1  
    for i, item in enumerate(reversed(rowOrColumn)):
        if 0 < index < len(puzzle)-1 and 0 < i < len(rowOrColumn)-1:
            if np.all(rowOrColumn[-i:] < item):
                counter[index][-i-1] = 1

def visibleTreeCheckerColumn (index, column):
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