
#opens the input file as a list strings
with open ("puzzle5_vents") as file:
    vent_input=[line.strip() for line in file]
#takes out the arrows and creates nested list
vent_input = [i.replace ('->',',') for i in vent_input]
vent_input = [i.split (',') for i in vent_input]
#turns strings into integers
vent_input_int = [int(j) for i in vent_input for j in i]
#re-organizes into a nested list
vents = list([vent_input_int[i:i+2] for i in range(0, len(vent_input_int), 2)])
#turns nested list into tuples
ventsT = list([tuple(l) for l in vents])
ventsT = list([ventsT[i:i+2] for i in range(0, len(ventsT), 2)])
#creates list from ventsT, where x1==x2 or y1==y2
#(so only vertical and horizontal lines, no diagonals)
s=[]
for i in ventsT:
    for l in range(len(i)):
        for m in range(len(i[0])):
            if i in s:
                continue
            if i[l][m]==i[l-1][m]:
                s.append(i)
#creates arrays
import numpy as np
u= np.array(s)
x= np.array (u[:,:,0])
x1=np.array (x[:,0])
x2=np.array (x[:,1])
y= np.array (u[:,:,1])
y1=np.array (y[:,0])
y2=np.array (y[:,1])
#creates a grid of "0"s
ñ = np.zeros((1000,1000))
#adds 1 to each position on the grid contained in the arrays (x,y)
#and to all positions between (x1,x2 and y1,y2) 
for q in range(len(s)):
        np.add.at(ñ, (range(y1[q],y2[q]+1),range(x1[q],x2[q]+1)), +1)
        np.add.at(ñ, (range(y2[q],y1[q]+1),range(x2[q],x1[q]+1)), +1)
#locates and prints the solution
solution = np.where(ñ>1)
print ('Part 1 solution:', len(solution[0]))

###       part 2

#creates list with the diagonals from ventsT
h=[]
for i in ventsT:
    if i in ventsT and i not in s:
        h.append (i)
#creates arrays with the coords of the diagonals
v= np.array(h)
w= np.array (v[:,:,0])
w1=np.array (w[:,0])
w2=np.array (w[:,1])
z= np.array (v[:,:,1])
z1=np.array (z[:,0])
z2=np.array (z[:,1])
#creates sub-array with the coords of the each diagonal,
#adds 1 to the diagonal or anti-diagonal of sub-array.
for l in range(len(h)):
        subñ=ñ[z1[l]:z2[l]+1,w1[l]:w2[l]+1]
        np.add.at(np.diagonal(subñ),range(len(np.diagonal(subñ))), +1)
        subñ=ñ[z2[l]:z1[l]+1,w2[l]:w1[l]+1]
        np.add.at(np.diagonal(subñ),range(len(np.diagonal(subñ))), +1)
        subñ=ñ[z2[l]:z1[l]+1,w1[l]:w2[l]+1]
        np.add.at(np.diagonal(np.fliplr(subñ)),range(len(np.diagonal(subñ))), +1)
        subñ=ñ[z1[l]:z2[l]+1,w2[l]:w1[l]+1]
        np.add.at(np.diagonal(np.flipud(subñ)),range(len(np.diagonal(subñ))), +1)
#locates and prints solution to part 2
solution2 = np.where(ñ>1)
print('Part 2 solution:',len(solution2[0]))
