import networkx as nx
import operator
import matplotlib.pyplot as plt
import pylab as p

def girvan_newman (G):

    if len(G.nodes()) == 1:
        return [G.nodes()]

    def find_best_edge(G0):       
        eb = nx.edge_betweenness_centrality(G0)
        return sorted(eb.items(), key = lambda x: float(x[1]), reverse = True)[0][0]

    components = nx.connected_component_subgraphs(G)
    clusterCount = 0
    while sum(1 for x in components) == 1:
        G.remove_edge(*find_best_edge(G))
        components = nx.connected_component_subgraphs(G)
        pos = nx.spring_layout(G,k=0.25,iterations=20)
        new_labels = dict((x,x + 1) for x in G.nodes())
        nx.draw_networkx_labels(G,pos,new_labels,font_size=14,font_color='black')
        nx.draw_networkx_nodes(G,pos,{0:0,33:33},node_color=['yellow','green'],node_size=800)
        # Now draw all the nodes, including leaders, using faction color scheme.
        nx.draw_networkx_nodes(G,pos,new_labels,node_color='r',node_size=500,alpha=0.8)
        nx.draw_networkx_edges(G,pos)
        clusterCount = clusterCount +1
        output = "C:\\Karate\\Iteration#%(id)02d.png" % {"id": clusterCount}
        p.savefig(output)       
        p.close()
    result = [c.nodes() for c in components]

    for c in components:
        result.extend(girvan_newman(c))

    return result

G = nx.karate_club_graph()
kn = girvan_newman(G)