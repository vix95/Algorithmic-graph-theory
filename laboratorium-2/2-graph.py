def create_list(l, line):
    for x in range(2):
        v = int(line.split()[x])
        if len(l) < v:
            for y in range(v - len(l)):
                l.append([])

    return


def get_edges(l, line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    l[v1].append(v2)
    l[v2].append(v1)

    return


def print_Graph(l):
    # print("Neighbors of vertices by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(l)):
        deg_v = len(l[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [y + 1 for y in l[x]]
        print("v" + str(x + 1) + ":", vertex)
        del vertex[:]

    # print("\ndeg(Graph):", deg_graph)
    return deg_graph


def sort_graph(l):
    for x in range(len(l)):
        l[x].sort()

    return


Graph = []
while True:
    try:
        line = input()
        create_list(Graph, line)
        get_edges(Graph, line)
    except EOFError:
        break

sort_graph(Graph)
print_Graph(Graph)  # degree of Graph

del Graph[:]
