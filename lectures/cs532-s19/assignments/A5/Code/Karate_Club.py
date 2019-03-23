from matplotlib.pyplot import *
import networkx as nx
import math

G=nx.karate_club_graph()
(faction1_col, faction2_col) = ('yellow','lightgreen')
node_color = [faction1_col] * len(G.nodes())
node_dict = dict(G.nodes(data=True))
for n in G.nodes():
    if node_dict[n]['club'] == 'Officer':
        node_color[n] = faction2_col

pos = nx.spring_layout(G,scale=0.2)
new_labels = dict((x,x + 1) for x in G.nodes())
nx.draw_networkx_labels(G,pos,new_labels,font_size=14,font_color='black')
nx.draw_networkx_nodes(G,pos,{0:0,33:33},node_color=['red','red'],node_size=800)
nx.draw_networkx_nodes(G,pos,new_labels,node_color=node_color,node_size=500)
nx.draw_networkx_edges(G,pos)

