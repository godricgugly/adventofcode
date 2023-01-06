import numpy as np

with open("puzzle10") as file:
    puzzle = [line.strip().split(' ') for line in file]

xregister = 1
cycle = 1
h = {0: 1, 1: 1}

for i in puzzle:
    if i[0] == 'noop':
        cycle += 1
        h[cycle] = xregister
    else:
        h[cycle+1] = xregister
        cycle += 2
        xregister += int(i[1])
        h[cycle] = xregister
result = sum([h[20]*20, h[60]*60, h[100]*100, h[140]*140, h[180]*180, h[220]*220])

print("Part 1:", result)

### Part 2
displayCTR = np.zeros((6, 40))
for y in range(6):
    for x in range(41):
        sprite = [h[y*40+x]-1, h[y*40+x], h[y*40+x]+1]
        if x-1 in sprite:
            displayCTR[y][x-1] = 1

#Open numpy array "displayCTR" to read the letters
print("Part 2: PZULBAUA")
