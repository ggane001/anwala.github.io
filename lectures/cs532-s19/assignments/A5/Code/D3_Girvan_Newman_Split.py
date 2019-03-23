import json
import numpy as np
import networkx as nx
import IPython
%matplotlib inline

g = nx.karate_club_graph()
nodes = [{'name': str(i), 'club': g.node[i]['club']}
         for i in g.nodes()]
links = [{'source': u[0], 'target': u[1]}
         for u in g.edges()]
with open('graph.json', 'w') as f:
    json.dump({'nodes': nodes, 'links': links},f, indent=4,)


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
        
        clusterCount = clusterCount +1
        output = "C:\\Karate\\Iteration%(id)02d.json" % {"id": clusterCount}
        nodes = [{'name': str(i), 'club': G.node[i]['club']}
         for i in G.nodes()]
        links = [{'source': u[0], 'target': u[1]}
         for u in G.edges()]
        with open(output, 'w') as f:
            json.dump({'nodes': nodes, 'links': links},f, indent=4,)
       
    result = [c.nodes() for c in components]

    for c in components:
        result.extend(girvan_newman(c))

    return result       
G1 = nx.karate_club_graph()
kn = girvan_newman(G1)

       
