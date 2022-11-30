
#opens input as integers in a list
with open ("puzzle13") as file:    
    puzzle=[int(x) for line in file for x in line.split(',')]
#opens and organises the folding instructions
with open ("folds13") as file:
    folds=[line.strip() for line in file]
folds = [i.replace('fold along ', '') for i in folds]
folds = [i.split('=') for i in folds]
folds = [[l,  int(i)] for l, i in folds]

import numpy as np
#transforms and organises input as an array
puzzle = np.array(puzzle).reshape(-1, 2)
#creates empty matrix, with dimensions from input
grid = np.zeros(np.amax(puzzle +1, 0))
grid = np.rot90(grid)
#fills the empty matrix 
for y , x in puzzle:
    grid [x , y] += 1

#function to perform the folds on the matrix
bends=[]
def bender (matrix, axis):  
    if axis == 'x':
        k , m = np.array_split(matrix, 2, axis = 1)
        k = np.delete(k , -1, 1)
        m = np.fliplr(m)
        result = k + m
        bends.append(result)
        count = np.count_nonzero(result)
        return count
        
    if axis == 'y':
        k , m = np.array_split(matrix, 2, axis = 0)
        k = np.delete(k , -1, 0)
        m = np.flipud(m)
        result = k + m
        bends.append(result)
        count = np.count_nonzero(result)
        return count
        
#part 1
print ('part 1:', bender (grid, folds[0][0]))
        
#part 2
for row, i in enumerate(folds):
    bender (bends[row], folds[row+1][0])
    if row == 10:
        break

#For easier readibility;
#replaces any value over 0 with a 1, in the last folded matrix.
solution = np.where(bends[11]>0, 1,0)
print('part 2: read the letters in the "solution" array: RLBCJGLU')
