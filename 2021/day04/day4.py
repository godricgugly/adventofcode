
#opens input as a string in a list
with open ("puzzle4_bingo") as file:
    puzzle=[line.strip() for line in file]


#checks if something is in something else
def check(boardsR, Check):
    return all(x in boardsR for x in Check)
Check= [['check','check','check','check','check']]

#splits the list into "chunks".
puzzle = [i.split () for i in puzzle]

#creates and organices "bingo" input
bingo = puzzle [0]
bingo = bingo[0].split(',')


#removes all blank [] indexes
for i in range(100):
    puzzle.remove ([])

#separates input list "puzzle"  into a list of list.
#Where each sublist has 5 element (representing a bingo board).
boardsR= []
l=1
while l < len(puzzle):
    boardsR.append (puzzle[l:l+5])
    l+=5


#Creates a new list, with re-arrenged boards, to have the original Coulums in rows

boardsC=[]
for u in boardsR:
    boardsC.append([[u[0][0]]+[u[1][0]]+[u[2][0]]+[u[3][0]]+[u[4][0]]]+
    [[u[0][1]]+[u[1][1]]+[u[2][1]]+[u[3][1]]+[u[4][1]]]+
    [[u[0][2]]+[u[1][2]]+[u[2][2]]+[u[3][2]]+[u[4][2]]]+
    [[u[0][3]]+[u[1][3]]+[u[2][3]]+[u[3][3]]+[u[4][3]]]+
    [[u[0][4]]+[u[1][4]]+[u[2][4]]+[u[3][4]]+[u[4][4]]])

#Creates a flattenned copy of boardsC
w=[item for sublist in boardsC for item in sublist]


#Checks if each number (in order) of 'bingo' is in any index of 'boards',
#If the number is in the board, it marks it with 'check',
#And, identifies which board will be the first to have a row or a colum marked.

for j in bingo:
    for h in boardsR:
        for g in h:
            for f in g:
                if f == j:
                    g[g.index(f)] = 'check'
#    print (j) #needed to know the last bingo input
    if check(puzzle,Check)== True:
        break

for j in bingo:
    for h in boardsC:
        for g in h:
            for f in g:
                if f == j:
                    g[g.index(f)] = 'check'
    if check(w,Check)== True:
        break
r=[]
y=[]
for e in puzzle:
    r.append (e.count('check'))
for b in w:
    y.append (b.count('check'))
#print (sum(r)) #needed to know which board would win first
#print (sum(y)) #needed to know which board would win first

#Sums all the unmarked elements in the winning board,
#And multiplies that by the last called number in the bingo
final=[item for sublist in boardsR[11] for item in sublist]
for z in range(12):
    final.remove('check')
final = list(map(int, final))
result= 49*sum(final)

#The following line has the only purpose of being hilarious
print('you dumb human! a giant squid is gonna... well.... not eat you, but worse: beat you at bingo! unless you know this:')

#prints out the result.
print (result)



#// second part: identify which board will win last.
#(last board to get a full coulmn or row)
bCcheck=list(boardsC)
bRcheck=list(boardsR)
A=[]
H=[]
A1=[]
H1=[]
v=[]
c=[]
for j in bingo:
    for h, hR in zip(boardsC, boardsR):
        H.append(h)
        A.append(hR)
        
        for g, gR in zip(h, hR):
            for f, fR in zip(g, gR):
                if f==j:
                    
                    g[g.index(f)] = 'check'
                if fR==j:
                    gR[gR.index(fR)] = 'check'
            if gR==['check','check','check','check','check']:
                v.append (hR)
                if hR in bRcheck:
                    bRcheck.remove(hR)
                    bCcheck.remove(h)
                if h in bCcheck:
                    bCcheck.remove(h)
                    bRcheck.remove(hR)
            if g==['check','check','check','check','check']:
                c.append (h)
                if h in bCcheck:
                    bCcheck.remove(h)
                    bRcheck.remove(hR)
                if hR in bRcheck:
                    bRcheck.remove(hR)
                    bCcheck.remove(h)
                H1.append(h)
                A1.append(hR)        
#            A1.append(g) 
#    print(j)            
#    if j=='30':
#        break
    
    if len(bCcheck)==1:
        break
    if len(bRcheck)==1:
        break


bRcheck=[item for sublist in bRcheck for item in sublist]
bCcheck=[item for sublist in bCcheck for item in sublist]


for j in bingo:
    for g in bRcheck:
        for f in g:
            if f == j:
                g[g.index(f)] = 'check'
#    print (j)
    if check(bRcheck,Check)== True:
        break

for j in bingo:
    for g in bCcheck:
        for f in g:
            if f == j:
                g[g.index(f)] = 'check'
#    print (j)
    if check(bCcheck,Check)== True:
        break


final1=[item for sublist in bRcheck for item in sublist]
for z in range(20):
    final1.remove('check')
final1 = list(map(int, final1))
result1= 28*sum(final1)

#The following line has the only purpose of being hilarious
print('you dumb human! you really thought beating a giant squid at bingo is smart? it is gonna kill yout unless you know this:')

#prints out the result.
print (result1)

