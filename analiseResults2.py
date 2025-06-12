import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from apify_client import ApifyClient
import networkx as nx
import sys 
import matplotlib.colors as mcolors

df = pd.read_json(sys.argv[1])


nomes_usuarios = []

for it in df['latestComments'].items():
    for comments in it[1]:
        #print(comments['ownerUsername'])
        nomes_usuarios.append(comments['ownerUsername'])


arestas = []
for usuario in nomes_usuarios: 
    arestas.append((usuario, sys.argv[2]))

try: 
    grafo = nx.read_gml('grafo.gml')
    print(grafo)
except Exception:
    print('entrei no except')
    grafo = nx.DiGraph()

grafo.add_edges_from(arestas)
print(grafo)

nx.write_gml(grafo, path = 'grafo.gml')

#nx.draw(grafo, with_labels = True)
#plt.savefig(f'grafo_{sys.argv[2]}.png')

#nx.write_gml(grafo, path = f'grafo.gml')

# Cores aleatórias para nós (usando uma paleta do matplotlib)
cores = list(mcolors.TABLEAU_COLORS.values())
cores_nos = [cores[i % len(cores)] for i, n in enumerate(grafo.nodes())]

# Desenha o grafo com estilo
nx.draw(
    grafo,
    with_labels=True,
    node_size=10,
    node_color=cores_nos,
    edge_color='gray',
    font_size=8,
    font_color='black',
    alpha=0.9,
    linewidths=0.5
)

# Salva como imagem
plt.title(f"Rede baseada em Comentários")
plt.axis('off')
plt.tight_layout()
plt.savefig(f'grafo_{sys.argv[2]}.png', dpi=300)

