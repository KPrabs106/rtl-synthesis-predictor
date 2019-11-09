import networkx as nx
import json
import itertools
from collections import defaultdict
from gtech_gates import *
import sys

netlist = json.load( open(sys.argv[1] + ".json") )

module = list(netlist['modules'])[0]

net2cell = defaultdict(lambda: [])

G = nx.Graph()

for cell in netlist['modules'][module]['cells']:
    connections = list((netlist['modules'][module]['cells'][cell]['connections']).values())
    connections = list(itertools.chain.from_iterable(connections))
    output_net = connections[-1]
    inputs = connections[:-1]

    w = gates.index(netlist['modules'][module]['cells'][cell]['type'])+1
    for input_net in inputs:    
        G.add_edge(input_net, output_net, weight=w)


#     for connection in list((netlist['modules'][module]['cells'][cell]['connections']).values()):
#         net = connection[0]
#         net2cell[net].append(cell)

# G = nx.Graph()
# for net in net2cell:
#     G.add_edges_from(itertools.combinations(net2cell[net], r=2))

G = nx.convert_node_labels_to_integers(G)

nx.write_weighted_edgelist(G,sys.argv[1]+".edgelist")

