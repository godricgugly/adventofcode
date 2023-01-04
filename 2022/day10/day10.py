with open("puzzle10") as file:
    puzzle = [line.strip().split(' ') for line in file]

x = 1
cycle = 1
h = {}

for i in puzzle:
    if i[0] == 'noop':
        cycle += 1
        h[cycle] = x
    else:
        h[cycle+1] = x
        cycle += 2
        x += int(i[1])
        h[cycle] = x
result = sum([h[20]*20, h[60]*60, h[100]*100, h[140]*140, h[180]*180, h[220]*220])

print("Part 1:", result)
