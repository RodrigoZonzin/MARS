import networkx as nx
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import community as community_louvain 
import matplotlib.cm as cm

grafo = nx.read_gml('grafo.gml')

centralidades = nx.closeness_centrality(grafo)
nx.set_node_attributes(grafo, centralidades, 'centrality')
centrality = nx.degree_centrality(grafo)
node_values = [centrality[n]*5000 for n in grafo.nodes()]


# +
grafo = nx.Graph(grafo)
partition = community_louvain.best_partition(grafo)

print(partition)

values = [partition[node] for node in grafo.nodes()]
cmap = cm.get_cmap('viridis', max(values)+1)

plt.figure(figsize=((12, 12)), dpi = 500)
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, node_size = node_values, node_color=values, with_labels=True, cmap=cmap)
plt.savefig('resultsLouvain.png')
#plt.show()
