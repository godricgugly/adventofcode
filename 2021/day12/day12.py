
import networkx as nx

#opens input as stings in a list
with open ("puzzle12") as file:
    puzzle=[line.strip() for line in file]
puzzle = [i.split('-') for i in puzzle]

#creates graph from list
G = nx.Graph()
for i in puzzle:
    G.add_nodes_from (i)  

for l, j in puzzle:
    G.add_edge (l , j)

#               PART 1 (DFS SOLUTION):
#creates list to keep thack of the number of paths
paths=[0,0]

#function to find the number of paths between 2 nodes. 
#(allowing infinite revisits of "big cave" nodes)
def depthFirst1(graph, currentVertex, target, visited, path):
    path.append(currentVertex)
#builds visited list with only "small caves"
    if currentVertex.islower():
        visited.append(currentVertex)
#keeps track of the number of paths
    if currentVertex == target and path not in paths:
#        paths.append(path) #to see what's going on while building up the function
        paths[0] +=1
#iterates through the graph nodes and calls function again if it's not in a "small cave"
    for vertex in graph[currentVertex]:
       if vertex not in visited:
            depthFirst1(graph, vertex, target, visited.copy(), path.copy())

#calls function and prints result
depthFirst1(G, 'start', 'end', [], [])
print ("Part 1 solution:" , paths[0])


#            PART 2 (DFS SOLUTION)
    
#probably super stupid way of making a dictionary with the nodes
d1=[]
for k in G:
    d1.append(k)
d2 = [False]*len(d1)
d = dict(zip(d1,d2))
reD = d.copy()

#function to find the number of paths between 2 nodes. 
#(allowing infinite revisits of "big cave" nodes 
#and 1 revisit of a "small cave" per path)
def depthFirst2(graph, currentVertex, target, visited, path, revisited):
    path.append(currentVertex)
#dictionary keeps track of which "small caves" have been revisited.
    revisited['start'] = True
    revisited['end'] = True
    if currentVertex.islower() and visited[currentVertex] == True:
        revisited[currentVertex] = True  
#builds visited list with only "small caves"
    if currentVertex.islower():
        visited[currentVertex] = True
#keeps track of the number of paths
    if currentVertex == target:
#        paths.append(path) #to see what's going on while building up the function
        paths[1] +=1
#iterates through the graph nodes and calls function again if it's not in a "small cave"
    for vertex in graph[currentVertex]:
       if visited[vertex] == False:
            depthFirst2(graph, vertex, target, visited.copy(), path.copy(), revisited.copy() )
#iterates through the graph nodes and calls function again
# if a "small cave" has not been revisited
    for vertex in graph[currentVertex]:
        if revisited[vertex] == False and visited[vertex] == True and sum(revisited.values()) < 3:
            depthFirst2(graph, vertex, target, visited.copy(), path.copy(), revisited.copy())

#calls function and prints result
depthFirst2(G, 'start', 'end', d, [], reD)
print ("Part 2 solution:" , paths[1])


# =============================================================================
#               INITIAL SLOW SOLUTION TO PROBLEM 1
# =============================================================================




#
#ll = list(itertools.chain.from_iterable((e , e) for e in puzzle for e1 in e if e1.isupper()))
#
##ll = list(itertools.chain.from_iterable((e, e, e) for e in puzzle for e1 in e if e1.isupper()))
#
##test=[]
##t=0
##while t < 3:
##    for k , row in enumerate(ll):
##        pp=[] 
###        if row == ll[k-1]:
##            
##        #        test.append(ll)
##        for k1 , val in enumerate(row):
###                if ll[k] == ll[k-1]:# and row == ll[k-2] :
###            if t ==1:
##            if val.isupper and row in puzzle and t==1:
##                    val+='1'
##                    ll[k][k1]= val
##            pp.append(ll[k][k1])
###            pp.append(ll[k][k1-1])
###                        puzzle.append(list(ll[k][k1],ll[k][k1-1]))
##            puzzle.append(pp)
##    t+=1
#
#
#            
#                
#
##hh=puzzle
##t1=0
##while  t1 < 3:
##    for e , row in enumerate(puzzle):
##        for e1 , val in enumerate(row):
##            if val.isupper():
##              
##                hh.append(row)  
##        if len(puzzle) > 30:
##            break
##    t1+=1
#
#
##lll = copy.deepcopy(ll)
#test=[]
#t=0
#while t < 4:
#    lll = copy.deepcopy(ll)
#    for k , row in enumerate(lll):
#        if row == ll[k-1]:
#            for k1 , val in enumerate(row):
#                if t ==0 and val.isupper():
#                    val += '1'
#                    lll[k][k1] = val
##                    test.append(lll)
#                    puzzle.append(row)
#                if t ==1 and val.isupper():
#                    val += '2'
#                    lll[k][k1] = val
##                    test.append(lll)
#                    puzzle.append(row)
#                if t ==2 and val.isupper():
#                    val += '3'
#                    lll[k][k1] = val
##                    test.append(lll)
#                    puzzle.append(row)
##                if t ==3 and val.isupper():
##                    val += '4'
##                    lll[k][k1] = val
###                    test.append(row)
##                    puzzle.append(row)
#    t+=1
#
##for m , row in enumerate(puzzle):
##    for m1 , val in enumerate(row):
##        if val.isupper():
##            ll = list(itertools.chain.from_iterable((e, e, e) for e in puzzle))
#
##y=0
##while y < 2:
##    for m , row in enumerate(puzzle):
##        for m1 , val in enumerate(row):
##            if val.isupper():
##                puzzle.append(row)
##    y+=1
#    
#G = nx.Graph()
#for i in puzzle:
#    G.add_nodes_from (i)
#
#for l, j in puzzle:
#    G.add_edge (l , j)
#
#paths = []
#for p in nx.all_simple_paths(G, source='start', target='end'):
#    paths.append(p)
#    
#for k , row in enumerate(paths):
#    for k1 , val in enumerate(row):
#        if val == 'QR1' or val == 'QR2' or val == 'QR3':
#            paths[k][k1] = 'QR'
#        if val == 'PF1' or val == 'PF2' or val == 'PF3':
#            paths[k][k1] = 'PF'
#        if val == 'HR1' or val == 'HR2' or val == 'HR3':
#            paths[k][k1] = 'HR'
#        if val == 'LY1' or val == 'LY2' or val == 'LY3':
#            paths[k][k1] = 'LY'
#
#
#paths1 = paths
#paths1.sort()
#paths1 = list(paths1 for paths1,_ in itertools.groupby(paths1))
#
#print (len(paths1))
#
