from atproto import Client
import networkx as nx
import time

client = Client()
client.login('tpmars.bsky.social', 'ViniVini@123')

# Função para pegar quem um usuário segue
def pega_following(handle):
    try:
        did = client.com.atproto.identity.resolve_handle({'handle': handle})['did']
        resposta = client.app.bsky.graph.get_follows({'actor': did})
        return [user['handle'] for user in resposta['follows']]
    except Exception as e:
        print(f"Erro ao buscar seguidores de {handle}: {e}")
        return []

# Criar grafo
G = nx.DiGraph()

# Inicializar com você
nivel_1 = pega_following('pif45.bsky.social')
G.add_node('pif45.bsky.social')

# Conecta você aos primeiros
for usuario in nivel_1:
    G.add_edge('pif45.bsky.social', usuario)

# Coletar o segundo nível (quem os seus seguidores seguem)
for usuario in nivel_1:
    nivel_2 = pega_following(usuario)
    for u in nivel_2:
        G.add_edge(usuario, u)
    time.sleep(1)  # respeitar limite de requisições

# Salvar ou visualizar a rede
nx.write_gexf(G, "rede_bluesky.gexf")
print("Rede salva como rede_bluesky.gexf")