import re
import copy

### Organice input data

initialLayout= list(re.split("    |] |  ",i ) for i in open("initialLayout").readlines())
initialLayout= [[i.replace("[", "").replace("]", "").strip() for i in row] for row in initialLayout]
layout= copy.deepcopy(initialLayout)
for e in range(0, len(layout)):
    for i in range(0, len(layout)):
        layout[i][e]= initialLayout[-e][i]
layout=[[i for i in row if i.isalpha()] for row in layout]

movementInstruction= list([int(e) for e in re.split("move | from | to ", i) if e != ""] 
                    for i in list(open("instructions").read().split("\n")) if i)

layout2= copy.deepcopy(layout)

### Part 1

for r, row in enumerate(movementInstruction):
    for i in range(row[0]):
        layout[row[2]-1].append(layout[row[1]-1][-1])
        layout[row[1]-1].pop()

print("Part 1:", "".join([a[-1] for a in layout]))

### Part 2

for r, row in enumerate(movementInstruction):
    tranferCrates= layout2[row[1]-1][-row[0]:]
    for i in tranferCrates:
        layout2[row[2]-1].append(i)
    del layout2[row[1]-1][-row[0]:]

print("Part 2:", "".join([a[-1] for a in layout2]))