
#opens input as a integers in a list
with open ("puzzle7_crabs") as file:
    puzzle=[int(x) for line in file for x in line.split(',')]

import numpy as np
g = np.median(puzzle)

s=[]
for i in puzzle:
    if i > g:
        h = i-g
    elif i < g:
       h = g-i 
    else: h = 0
    s.append(h)
p=0
for l in s:
    p=p+l
print ("Part 1 solution:" , p)

###               part 2

print (np.mean(puzzle) , "**Needed to solve part 2")
g1=486 #this is the mean, without decimals :)

s1=[]
for i in puzzle:
    if i > g1:
        h1 = i-g1
    elif i < g1:
       h1 = g1-i 
    else: h1 = 0
    s1.append(h1)

q=[]
for m in s1:
   w=0
   for n in range(1,m+1):
        w+=n
   q.append(w)
p1=0
for l in q:
    p1=p1+l
print ("Part 2 solution:" , p1)   
        
