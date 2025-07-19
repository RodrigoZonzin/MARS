import networkx as nx
import matplotlib.pyplot as plt 

g = nx.read_gexf('rede_bluesky.gexf')


plt.figure(figsize=(10, 8))
nx.draw(g)
plt.savefig('grafo.png')