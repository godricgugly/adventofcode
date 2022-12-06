puzzle= open("puzzle06").read()

#Part 1
for i, letter in enumerate(puzzle):
    if i < len(puzzle)-4:
        sub = puzzle[i]+puzzle[i+1]+puzzle[i+2]+puzzle[i+3]
    if len(set(sub)) == len(sub):
        print("Part 1: ", i+4)
        break

### Part 2
for i, letter in enumerate(puzzle):
    if i < len(puzzle)-14:
        sub=[]
        for x in range(14):
            sub.append(puzzle[i+x])
        sub = "".join([a for a in sub])
    if len(set(sub)) == len(sub):
        print("Part 1: ", i+14)
        break
