
with open ("puzzle02") as file:
    puzzle=[line.strip() for line in file]
    puzzle=[i.split(" ") for i in puzzle]
x= 1
y= 2
z= 3
draw= 3
win= 6
counter= 0

for row in puzzle:
    if row[1] == "X":
        counter+= x
    if row[1] == "Y":
        counter+= y
    if row[1] == "Z":
        counter+= z
    if row[0] == "A" and row[1] == "X" or row[0] == "B" and row[1] == "Y" or row[0] == "C" and row[1] == "Z":
        counter+= draw
    if row[0] == "C" and row[1] == "X" or row[0] == "A" and row[1] == "Y" or row[0] == "B" and row[1] == "Z":
        counter+= win
print("Part 1: ",counter)

counter2= 0
for row in puzzle:
    if row[1] == "X":
        if row[0] == "A":
            counter2+= z
        if row[0] == "B":
            counter2+= x
        if row[0] == "C":
            counter2+= y
    if row[1] == "Y":
        counter2+= draw
        if row[0] == "A":
            counter2+= x
        if row[0] == "B":
            counter2+= y
        if row[0] == "C":
            counter2+= z
    if row[1] == "Z":
        counter2+= win
        if row[0] == "A":
            counter2+= y
        if row[0] == "B":
            counter2+= z
        if row[0] == "C":
            counter2+= x
print("Part 2: ", counter2)
    
        