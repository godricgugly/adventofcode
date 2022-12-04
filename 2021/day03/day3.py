
with open ("puzzle3") as file:
    puzzle=[line.strip() for line in file]

a = '1'
w = '0'

#part 1

gamma = [0] *len(puzzle[0])
epsilon = [0] *len(puzzle[0])

for r in range(len(puzzle[0])):
    s = []
    for i in puzzle:
        s.append (i[r])
    if s.count(a) < s.count(w):
        gamma [r] = 0
        epsilon [r] = 1
    elif s.count(a) > s.count(w):
        gamma [r] = 1
        epsilon [r] = 0

binaryStringG = ''.join(str(g) for g in gamma)
binaryStringE = ''.join(str(e) for e in epsilon)

decimalG = int(binaryStringG, 2)
decimalE = int(binaryStringE, 2)

result = decimalG * decimalE

print ('Parti 1 solution:', result)

 
#part 2 

d=[]
f=[]

h= list(range(len(puzzle)))

for r in range(len(puzzle[0])): 
    z=[]
    for l in h:
       z.append (puzzle[l][r])   
    if z.count(a) > z.count(w):
        for k in h:
            if puzzle[k][r]==a:
                d.append (k)
    elif z.count(a) < z.count (w):
        for k in h:
            if puzzle[k][r]==w:
                d.append (k)
    elif z.count(a) == z.count(w):
        for k in h:
            if puzzle[k][r]==a:
                d.append(k)
    h=d
    d=[]
    if len(h)== 1:
        break



o= list(range(len(puzzle)))

for t in range(len(puzzle[0])):
    z=[]
    for b in o:
        z.append (puzzle[b][t])
    if z.count(a) > z.count(w):
        for m in o:
            if puzzle[m][t]==w:
                f.append(m)
    elif z.count(a) < z.count (w):
        for m in o:
            if puzzle[m][t]==a:
                f.append(m)
    elif z.count(a) == z.count(w):
        for m in o:
            if puzzle[m][t]==w:
                f.append(m)
    o=f
    f=[]
    if len(o)== 1:
        break
    

decimalO = int(puzzle[h[0]], 2)
decimalC = int(puzzle[o[0]], 2)
 
result1 = decimalO * decimalC
 
print ("Part 2 solution:", result1)

