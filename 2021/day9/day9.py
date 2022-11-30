
#with open ("test9.1") as file:
#    potatoe=[line.strip() for line in file]

##opens the input file as a list strings
with open ("puzzle9") as file:
    potatoe=[line.strip() for line in file]

h=[]
for s in potatoe:
    s= [s[i] for i in range(0, len(s), 1)]
    h.append(s)
t=[]
for s in h:
    s= [int(x) for line in s for x in line.split(',')]
    t.append(s)

import numpy as np
t1 = np.array(t)


res=[]
for i in range(len(t)):
    for j in range(len(t)):
        if i == 0 and j <= len(t)-2:
            if t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res.append(t1[i][j])
        if j == 0 and i <= len(t)-2:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res.append(t1[i][j])
        if 0 < j <= len(t)-2 and 0 < i <= len(t)-2:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res.append(t1[i][j])
        if j == len(t)-1:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j]:
                res.append(t1[i][j])
        if i == len(t)-1:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i][j+1] :
                res.append(t1[i][j])
result=[]  

for i in res:
    i += 1
    result.append(i)
print(sum(result))


# =============================================================================
#                                     part 2
# =============================================================================
    
    
def find_cave (a,b):
    a1=a
    a2=a
    b1=b
    b2=b
    for i in range(len(t)-a):
        if t1[a1][b1] < 9:
            for j in range(len(t)-b):
                if t1[a1][b1] < 9:
                    res1.append(t1[a1][b1])
                    t1[a1][b1] = 0
                    b1+=1
                elif b2 < 0:
                    continue
                elif t1[a1][b2]< 9:
                    if b2 != b:
                        res1.append(t1[a1][b2])
                        t1[a1][b2] = 0
                    b2-=1
            a1+=1
            b1 = b
            b2 = b
        elif a2 < 0:
            continue
        elif t1[a2][b1]< 9:
            if a2 != a:
                for j in range(len(t)-b):
                    if t1[a2][b1] < 9:
                        res1.append(t1[a2][b1])
                        t1[a2][b1] = 0
                        b1+=1
                    elif b2 < 0:
                        continue
                    elif t1[a2][b2]< 9:
                        if b2 != b:
                            res1.append(t1[a2][b2])
                            t1[a2][b2] = 0
                        b2-=1
            b1 = b
            b2 = b
            a2-=1


def edges (a , b):
    a1=a
    b1=b
    for i in range(len(t)-a):
        if t1[a1][b1] != 0 and t1[a1][b1] < 9:
            res1.append (t1[a1][b1])
            t1[a1][b1] = 0
        elif t1[a1+1][b1] > 9 and t1[a1+1][b1] != 0:
            res1.append(t1[a1+1][b1])
            t1[a1+1][b1] = 0
        elif t1[a1][b1+1] > 9 and t1[a1][b1+1] != 0:
            res1.append(t1[a1][b1+1])
            t1[a1][b1+1] = 0
        elif t1[a1-1][b1] > 9 and t1[a1-1][b1] != 0:
            res1.append (t1[a1-1][b1])
            t1[a1-1][b1] = 0
        elif t1[a1][b1-1] > 9 and t1[a1][b1-1] != 0:
            res1.append ([a1][b1-1])
            [a1][b1-1] = 0
        elif t1[a1][b1] == 0 and t1[a1-1][b1] != 9 and t1[a1][b1+1] != 9 and t1[a1+1][b1] != 9:
                a1 -= 1
        elif t1[a1-1][b1] == 9:
            b1 +=1
        elif t1[a1][b1+1] == 9 and t1[a1+1][b1] != 9:
            a1 += 1
        elif t1[a1+1][b1] == 9:
            b1 -= 1
        


  
res1=[]
for i in range(len(t)):
    for j in range(len(t)):
        if i == 0 and j <= len(t)-2:
            if t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res1.append(find_cave (i,j))
        if j == 0 and i <= len(t)-2:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res1.append(find_cave (i,j))
        if 0 < j <= len(t)-2 and 0 < i <= len(t)-2:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j] and t1[i][j] < t1[i][j+1] :
                res1.append(find_cave (i,j))
        if j == len(t)-1:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i+1][j]:
                res1.append(find_cave (i,j))
        if i == len(t)-1:
            if t1[i][j] < t1[i-1][j] and t1[i][j] < t1[i][j-1] and t1[i][j] < t1[i][j+1] :
                res1.append(find_cave (i,j))
        
#    if i == 64: #to check where is each of the big caves in the t1 array
#        break
#    

    
res2 = [str(i) for i in res1]

def split(sequence, sep):
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk

res3 = [i for i in split(res2 , 'None')]


check=[]
for i in res3:
    if len(i) > 70:
        check.append(i)

    


# t1[29][63] = cave length 96 + 8 (counted by hand!!!) = 104
# t1[63][30] = cave length 88 + 6 (counted by hand!!!) = 94
# t1[53][8] = cave length 78 + 14 (counted by hand!!!) = 92
            ###
# t1[33][34] = cave length 71 + 6 (counted by hand!!!) = 
# t1[15][27] = cave length 73 + 16 (counted by hand!!!) = 89 
# t1[24][2] = cave length 74 + 8 (counted by hand!!!) =  82
# t1[51][77] = cave length 75 + 9 (counted by hand!!!) = 84
# t1[10][80] = cave length 81 + 5 (counted by hand!!!) = 86
# t1[19][87] = cave length 81 + 4 (counted by hand!!!)

print ('answer 2 = ', 104*94*92)

