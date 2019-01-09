import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def import_matrix(num):
    l = [line.rstrip('\n') for line in open('graphTests/' + str(num) + '_adjmatrix.txt')]
    A = []
    for x in range(len(l)):
        A.append([])
        for y in l[x]:
            if y != ' ':
                A[x].append(int(y))

    return A


def diff_graph():
    H = nx.complete_graph(len(M.nodes))
    for x in M.edges:
        H.remove_edge(x[0], x[1])

    return H


def create_edge_graph():
    N = M.copy()
    i = 0
    for x in N.edges():
        N[x[0]][x[1]]['number'] = i
        i += 1

    for x in N.edges():
        e1 = nx.get_edge_attributes(N, 'number')[x]
        for y in N.edges():
            e2 = nx.get_edge_attributes(N, 'number')[y]
            if x != y and (x[0] in y or x[1] in y):
                E.add_node(e1)
                E.add_node(e2)
                E.add_edge(e1, e2)


for x in range(1, 25):
    M = nx.from_numpy_matrix(np.matrix(import_matrix(x)))
    R = diff_graph()
    E = nx.Graph()
    create_edge_graph()
    plt.figure(1, figsize=(3, 3))
    #nx.draw(M, node_size=2)
    #plt.show(M)
    nx.draw(R, node_size=2)
    plt.show(R)
    nx.draw(E, node_size=2)
    plt.show(E)
