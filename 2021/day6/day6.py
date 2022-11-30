
#opens input as a integers in a list
with open ("puzzle6") as file:
    puzzle=[int(x) for line in file for x in line.split(',')]

import copy
puzzle1 = copy.deepcopy(puzzle)

n=0
while n < 80:
    for k in range(len(puzzle1)):
        if puzzle1 [k] >= 0:
            puzzle1 [k]=puzzle1 [k]-1
        if puzzle1 [k]==-1:
            puzzle1 [k]=6
            puzzle1.append(8)
    n=n+1

print ("Part 1 solution:" , len(puzzle1))
 
    
###     part 2

n=0
s=[]
while n < 18:
    for k in range(len(puzzle)):
        if puzzle [k] >= 0:
            puzzle [k]=puzzle [k]-1
        if puzzle [k]==-1:
            puzzle [k]=6
            puzzle.append(8)
    s.append (len(puzzle))
    n=n+1

#Memoized approach, works but too slow when gen < 200
def lanternFish (gen, s1):
    if s1[gen] is not None:
        return s1[gen]
    else:
        result = lanternFish (gen-7, s1) + lanternFish (gen-9,s1)  
    return result

def memo (gen):
    s1= s + [None]*(gen-17)
    return lanternFish (gen, s1)

#print (memo (200))

#bottom up approach, it's awesome!
def bot (ge):
    if ge < 18:
        return s[ge]
    s2= s + [None] * (ge-17)
    for i in range(18, ge+1):
        s2[i]= s2[i-7] + s2[i-9]
    return s2[i]

print ("Part 2 solution:" , bot(255))
