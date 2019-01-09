import networkx as nx


G = nx.Graph()
for x in range(7):
    G.add_node(x)

G.add_edges_from(
    [(0, 1), (0, 4), (0, 5), (0, 7),
     (1, 0), (1, 2), (1, 3), (1, 4), (1, 7),
     (2, 1), (2, 3), (2, 6),
     (3, 1), (3, 2), (3, 4),
     (4, 0), (4, 1), (4, 3), (4, 5), (4, 7),
     (5, 0), (5, 4), (5, 7),
     (6, 2),
     (7, 0), (7, 1), (7, 4), (7, 5)])

for x in G.nodes():
    print('deg v%d = %d' % (x, G.degree(x)))

print('\nnumber of nodes = %d' % (G.number_of_nodes()))
print('number of edges = %d' % (G.number_of_edges()))

num_of_leafs = [x for x in G.nodes() if G.degree(x) == 1]
print('number of leafs = %d' % len(num_of_leafs))

num_of_edges_on_3_deg = [x for x in G.nodes() if G.degree(x) == 3]
print('number of 3 degree nodes = %d' % (len(num_of_edges_on_3_deg)))
