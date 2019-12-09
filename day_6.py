import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv('D:/Practise/advent_of_code/day_6_input.txt',header=None)
df.columns=['original']
df['to'] = df['original'].str[:3]
df['from']=df['original'].str[4:]

# Solution to part 1
# Creating a directed graph
G = nx.DiGraph()

#Adding nodes and edges to the graph
for i,j in df.iterrows():
    G.add_edge(j[2],j[1])
    
    
# Finding the shortest path from each node to COM
sp = nx.shortest_path(G,target='COM')

# Computing total number of orbits
orbits = 0
for key in sp:
    orbits = orbits + (len(sp[key])-1)

print(orbits)
