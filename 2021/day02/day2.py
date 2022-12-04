
with open ("puzzle2_submarie_directions") as file:
    puzzle=[line.strip() for line in file]
puzzle = [i.split() for i in puzzle]

forwardCounter = 0
depthCounter = 0
aimCounter = 0
for o in puzzle:
    if "forward" in o:
        forwardCounter = forwardCounter + (int (o[1]))
        aimCounter = (int (o[1])) * depthCounter + aimCounter
    if "down" in o:
        depthCounter = depthCounter + (int (o[1]))
    if "up" in o:
        depthCounter = depthCounter - (int (o[1]))   

result1 = depthCounter * forwardCounter
print ("Part1 solution:", result1)

result2 = aimCounter * forwardCounter
print ("Part2 solution:", result2)
        
