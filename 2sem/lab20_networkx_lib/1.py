# -*- coding: UTF-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
while True:
    s = input().split()
    if not s:
        break
    G.add_edge(s[0], s[1], weight=s[2])

def show_spanning_tree(G):
    G = nx.minimum_spanning_tree(G)
    pos = nx.spectral_layout(G)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos)
    plt.show()

def show_graph(G):
    pos = nx.spectral_layout(G)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos)
    plt.show()
show_graph(G)
show_spanning_tree(G)