import string
import copy

with open ("puzzle03") as file:
    puzzle=[[line.strip()] for line in file]
    
puzzle2= sum(copy.deepcopy(puzzle), [])

alphabet= string.ascii_lowercase + string.ascii_uppercase

counter= 0
for row in puzzle:
    firstpart, secondpart = row[0][:len(row[0])//2], row[0][len(row[0])//2:]
    row[0]= firstpart
    row.append(secondpart)
    repeated=[]
    for letter in row[1]:
        if letter in row[0] and letter not in repeated:
            counter+= alphabet.index(letter) +1
            repeated.append(letter)

print ("Part 1: ", counter)

counter2= 0
for i in range(0, len(puzzle2), 3):
    repeated=[]
    for letter in puzzle2[i]:
        if letter in puzzle2[i+1] and letter in puzzle2[i+2] and letter not in repeated:
            counter2+= alphabet.index(letter) +1
            repeated.append(letter)
            
print ("Part 2: ", counter2)