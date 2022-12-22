import numpy as np
with open ("puzzle09") as file:
    puzzle=[tuple(line.strip().split(' ')) for line in file]

headX = 499
headY = 499

tailX = 499
tailY = 499

path = np.zeros((1000, 1000))

def moveHead(direction, positionX, positionY):
    if direction == 'U':
        positionY -= 1
    if direction == 'D':
        positionY += 1
    if direction == 'R':
        positionX += 1
    if direction == 'L':
        positionX -= 1
    return positionX, positionY

def checkDistance(postitionTailX, positionTailY, positionHeadX, positionHeadY):
    if abs(positionHeadX-postitionTailX) > 1:
        return True
    if abs(positionHeadY-positionTailY) > 1:
        return True

def tailFollow(direction, positionTailX, positionTailY, positionHeadX, positionHeadY):
    if checkDistance(positionTailX, positionTailY, positionHeadX, positionHeadY):
        if direction == 'U':
            positionTailX = positionHeadX
            positionTailY = positionHeadY+1
        if direction == 'D':
            positionTailX = positionHeadX
            positionTailY = positionHeadY-1
        if direction == 'R':
            positionTailX = positionHeadX-1
            positionTailY = positionHeadY
        if direction == 'L':
            positionTailX = positionHeadX+1
            positionTailY = positionHeadY
    return positionTailX, positionTailY

for row in puzzle:
    for step in range(int(row[1])):
        path[tailY][tailX] = 1
        headX, headY = moveHead(row[0], headX, headY)
        tailX, tailY = tailFollow(row[0], tailX, tailY, headX, headY)
        
print('Part 1:', np.count_nonzero(path))