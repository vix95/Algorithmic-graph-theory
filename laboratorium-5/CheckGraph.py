import networkx as nx


def check_complete_graph(g):
    for x in g.nodes:
        for y in g.nodes:
            if x != y:
                if x not in g.neighbors(y):
                    return False

    return True


def print_check(title, g):
    print('-- Check', title, 'Graph --')
    print('Tree graph?', nx.is_tree(g))
    print('Complete graph?', check_complete_graph(g))
    print('Bipartite graph?', nx.is_bipartite(g))
    print('Cycle graph?', False if len(nx.cycle_basis(g)) == 0 else True)
    print('')


def prepare_tree(g):
    for x in range(8):
        g.add_node(x)

    g.add_edges_from([
        (0, 1), (0, 2),
        (1, 0), (1, 3), (1, 4),
        (2, 0), (2, 5),
        (3, 1), (3, 6), (3, 7),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 3), (7, 8),
        (8, 7)
    ])

    print_check('TREE', g)


def prepare_complete(g):
    for x in range(4):
        g.add_node(x)

    g.add_edges_from([
        (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 3),
        (3, 0), (3, 1), (3, 2)
    ])

    print_check('COMPLETE', g)


def prepare_bipartite(g):
    for x in range(8):
        g.add_node(x)

    g.add_edges_from([
        (0, 4), (0, 5),
        (1, 4), (1, 6),
        (2, 5), (2, 6), (2, 7),
        (3, 5), (3, 6),
        (4, 0), (4, 1),
        (5, 0), (5, 2), (5, 3),
        (6, 1), (6, 2), (6, 3),
        (7, 2)
    ])

    print_check('BIPARTITE', g)


def prepare_cycle(g):
    for x in range(3):
        g.add_node(x)

    g.add_edges_from([
        (0, 1), (0, 2),
        (1, 0), (1, 2),
        (2, 0), (2, 1)
    ])

    print_check('CYCLE', g)


G_tree = nx.Graph()  # drzewo
G_complete = nx.Graph()  # graf pelny
G_bipartite = nx.Graph()  # graf dwudzielny
G_cycle = nx.Graph()  # graf cykliczny

prepare_tree(G_tree)
prepare_complete(G_complete)
prepare_bipartite(G_bipartite)
prepare_cycle(G_cycle)
