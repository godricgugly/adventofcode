import string
import numpy as np
import networkx as nx

with open("puzzle12") as file:
    puzzle = [line.strip() for line in file]

alphabet = string.ascii_lowercase
heightMap = np.zeros((len(puzzle), len(puzzle[0])))

def weights(u, v, d):
    node_u_wt = G.nodes[u].get("node_weight", heightMap[u])
    node_v_wt = G.nodes[v].get("node_weight", heightMap[v])
    edge_wt = d.get("weight", 1)
    if node_v_wt - node_u_wt < 2:
        return node_v_wt+10
    return 10000

for r, row in enumerate(puzzle):
    for i, item in enumerate(row):
        if item.islower():
            heightMap[r][i] = alphabet.index(item)
        if item == 'S':
            startNode = (r, i)
            heightMap[r][i] = 0
        if item == 'E':
            endNode = (r, i)
            heightMap[r][i] = 25

G = nx.grid_2d_graph(len(puzzle), len(puzzle[0]))
depth = {(i, j): int(heightMap[i][j]) for i, j in G.nodes}
path = nx.dijkstra_path(G, startNode, endNode, weight=weights)

print('Part 1:', len(path)-1)

### Part 2

def weights1(u, v, d):
    node_u_wt = G.nodes[u].get("node_weight", heightMap[u])
    node_v_wt = G.nodes[v].get("node_weight", heightMap[v])
    edge_wt = d.get("weight", 1)
    if node_u_wt - node_v_wt < 2:
        return node_v_wt+10
    return 10000

pathLength = nx.dijkstra_path_length(G, startNode, endNode, weight=weights)
paths1 = nx.single_source_dijkstra_path(G, endNode, cutoff=pathLength, weight=weights1)

trailLengths = []
for trail in paths1:
    if depth[trail] == 0:
        trailLengths.append(len(paths1[trail]))
print('Part 2:', min(trailLengths)-1)
