import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os, sys
import atproto as bsk
import networkx as nx
#from senha import senha


#logando no Bsk 
client = bsk.Client()
client.login('tpmars.bsky.social', 'ViniVini@123')


termos_interesse = ['DefendaOBrasil', 'LulaLadrao', 'BrasilSoberano']
search = client.app.bsky.feed.search_posts({'q': termos_interesse[0]})

