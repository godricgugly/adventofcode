with open ("puzzle04") as file:
    puzzle=[[line.strip()] for line in file]

puzzle= [i.split(",") for row in puzzle for i in row]
puzzle= [[i.split("-") for i in row] for row in puzzle]
puzzle= [[[int(i)  for i in col] for col in row] for row in puzzle]

def range_subset(range1, range2):
    return range1.start >= range2.start and range1.stop <= range2.stop

def range_overlap(range1, range2):
    return range1.start >= range2.start and range1.start <= range2.stop or range1.stop <= range2.stop and range1.stop >= range2.start

counter= 0
counter2= 0
for row in puzzle:
    if range_subset(range(row[0][0], row[0][1]), range(row[1][0], row[1][1])) or range_subset(range(row[1][0], row[1][1]), range(row[0][0], row[0][1])):
        counter+= 1
    if range_overlap(range(row[0][0], row[0][1]), range(row[1][0], row[1][1])) or range_subset(range(row[1][0], row[1][1]), range(row[0][0], row[0][1])):
        counter2+= 1

print("Part 1: ", counter)
print("Part 2: ", counter2)

