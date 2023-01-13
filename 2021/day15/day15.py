import copy
import networkx as nx
import numpy as np

with open ("puzzle15") as file:
    puzzle=[line.strip() for line in file]
    puzzle=[[int(item) for item in line] for line in puzzle]

puzzle = np.array(puzzle)

def weights(u, v, d):
    node_u_wt = G.nodes[u].get("node_weight", 1)
    node_v_wt = G.nodes[v].get("node_weight", puzzle[v])
    edge_wt = d.get("weight", 1)
    return node_v_wt

G = nx.grid_2d_graph(len(puzzle), len(puzzle[0]))   
depth = {(i, j): int(puzzle[i][j]) for i, j in G.nodes}
path = nx.dijkstra_path(G, (0,0), (9,9), weight=weights)

riskCount = []
for i in path:
    riskCount.append(depth[i])

print("Part 1 solution:" , sum(riskCount)-1)
      
### PART 2

def weights2(u, v, d):
    node_u_wt = G2.nodes[u].get("node_weight", 1)
    node_v_wt = G2.nodes[v].get("node_weight", puzzle[v])
    edge_wt = d.get("weight", 1)
    return node_v_wt

def MapBuilder (axis, array, newPuzzle , iterations , counter):
    puzzle01 = copy.deepcopy(array) + 1
    puzzle01 = puzzle01 % 10
    puzzle01[puzzle01 < 1] = 1
    if counter < iterations:
        return np.concatenate((array, MapBuilder (axis, puzzle01, newPuzzle, iterations,  counter+1)), axis = axis)
    return np.concatenate((array, puzzle01), axis = axis)

puzzle = MapBuilder (1, puzzle, puzzle, 3, 0)
puzzle = MapBuilder (0, puzzle, puzzle, 3, 0)

G2 = nx.grid_2d_graph(len(puzzle), len(puzzle[0]))   
depth2 = {(i, j): int(puzzle[i][j]) for i, j in G2.nodes}
path2 = nx.dijkstra_path(G2, (0,0), (499,499), weight=weights2)

riskCount2 = []
for i in path2:
    riskCount2.append(depth2[i])
    
print("Part 2 solution:" , sum(riskCount2)-1)
