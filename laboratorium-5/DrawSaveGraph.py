import networkx as nx
import matplotlib.pyplot as plt


def write_adjMatrix():
    f = open('adjMatrix.txt', 'w')
    f.write(str(M.todense()))
    f.close()


def write_ajdList():
    f = open('adjList.txt', 'w')
    for line in nx.generate_multiline_adjlist(G):
        f.write(line + '\n')

    f.close()


#G = nx.complete_graph(5)
G = nx.Graph()
for x in range(4):
    G.add_node(x)

G.add_edges_from([
    (0, 1), (0, 3),
    (1, 0), (1, 2),
    (2, 1), (2, 3),
    (3, 0), (3, 2)
])

M = nx.adjacency_matrix(G)
plt.figure(1, figsize=(3, 3))
nx.draw(G, node_size=2)
plt.show()

write_adjMatrix()
write_ajdList()
