#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:44:16 2022

@author: vant
"""
#opens input as stings in a list
with open ("puzzle11") as file:
    potatoe=[line.strip() for line in file]
#converts into list of units
p=[]
for i in potatoe:
    p1=[]
    for j in i:
        p1.append (int(j))
    p.append (p1)

import numpy as np
mat= np.array(p)

#def neighbors ( a , b):
#    n = [mat[i][j] for i in range(a-1, a+2) for j in range(b-1, b+2) if i > -1 and j > -1 and j < len(mat[0]) and i < len(mat)]
#    np.add.at (n,1)
#    return n

def neighborsI ( a , b):
    a1 = a
    b1 = b
    ñ=[]
    for i in range(a-1, a+2):
        for j in range(b-1, b+2):
            if i == a1 and j == b1:
                continue
            if i > -1 and j > -1 and j < len(mat[0]) and i < len(mat):
               ñ.append((i,j))
    return ñ

#test=[]
c = []
f=0
sol=0
while f < 315:
    mat += 1
    while np.any(mat > 9): 
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val > 9:
                    mat[i][j] = -273
                    for x,y in neighborsI (i,j):
                        mat[x][y] += 1      
    mat = np.where(mat < 0 , 0 , mat)
#    test.append(mat)
    c.append(np.count_nonzero(mat==0))
    if np.all(mat == 0):
        sol = f
    f += 1

print(sum(c))
print(sol+1)

