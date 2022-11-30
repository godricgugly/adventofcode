
#opens the input file as a list strings
with open ("puzzle8") as file:
    puzzle=[line.strip() for line in file]
    
#organices list
puzzle = [i.split ('|') for i in puzzle]
puzzle = [i.split () for j in puzzle for i in j]

#creates 2 lists, one for the output numbers, one for the signalt patterns
n=0
numbers = []
signalPatterns = []
while n < len(puzzle):
    numbers.append (puzzle[n+1])
    signalPatterns.append (puzzle[n])
    n += 2

#selects the numbers that have the desired properties
selected = []
for i in numbers:
    for j in range(len(i)):
        if len(i[j]) in {2, 4, 3, 7}:
            selected.append(i[j])

print ("Part 1 solution:", len(selected))

###             part 2

#check if a unorganized sequence contains another unorganized sequence.
def containsAll(a, b):
    return 0 not in [c in a for c in b]

#Searches input letter string in the local database, and identifies what number it is
def find690 (o , p):
    for i in signalPatterns[p]:
        if len(i) == 2:
            k = i
        elif len(i) == 4:
            ñ = i
        else: continue
    
    if containsAll(o , k and ñ) == True:
        return 9
    if containsAll(o , k) == True and containsAll(o , ñ) == False:
        return 0
    else: return 6

#Searches input letter string in the local database, and identifies what number it is
def find235 (o , p):
    for i in signalPatterns[p]:
        if len(i) == 2:
            k = i
        elif len(i) == 6:
            if find690 (i , p) == 9:
                m = i
        else: continue

    if containsAll(o , k) == True:
        return 3
    if containsAll(m , o) == False:
        return 2
    if containsAll(m , o) == True:
        return 5

#Identifies and substitutes each letter string whith the correct number it represents.
for i in enumerate(numbers):
    for j in range(len(i[1])):
        if len(i[1][j]) == 2:
            i[1][j]= 1
        elif len(i[1][j]) == 4:
            i[1][j]= 4
        elif len(i[1][j]) == 3:
            i[1][j]= 7
        elif len(i[1][j]) == 7:
            i[1][j]= 8
        elif len(i[1][j]) == 5:           
            i[1][j]= find235 (i[1][j] , i[0])
        elif len(i[1][j]) == 6:
            i[1][j]= find690 (i[1][j] , i[0])
#concadetanes the numbers into 4 digit numbers
s = []
for j in numbers:
    res = int("".join([str(i) for i in j]))
    s.append (res)
#Adds all the numbers
print ("Part 2 solution:" , sum(s))

