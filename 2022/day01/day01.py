from itertools import groupby

with open ("puzzle01") as file:
    puzzle=[line.strip() for line in file]   
puzzle= (list(g) for _, g in groupby(puzzle, key=''.__eq__))
puzzle= [i+j for i, j in zip(puzzle, puzzle)]
puzzle= [[int(item) for item in row if item != ""] for row in puzzle]
puzzle= [sum(i) for i in puzzle]
puzzle.sort()
print("Part 1: ", puzzle[-1])
print("Part 2: ", puzzle[-1]+puzzle[-2]+puzzle[-3])
