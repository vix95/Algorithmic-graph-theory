def create_list(line):
    for x in range(2):
        v = int(line.split()[x])
        if len(GraphG) < v:
            for y in range(v - len(GraphG)):
                GraphG.append([])

    return


def get_edges(line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    GraphG[v1].append(v2)

    return


def print_Graph(graph):
    deg_graph = 0
    for x in range(len(graph)):
        deg_v = len(graph[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [x + 1 for x in graph[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("deg(Graph):", deg_graph, "\n")
    return deg_graph


def sort_graph(graph):
    for x in range(len(graph)):
        graph[x].sort()

    return


def reversed_Graph(graphG, graphH):
    # create graph
    for x in range(len(graphG)):
        graphH.append([])

    for x in range(len(graphG)):
        for y in graphG[x]:
            graphH[y].append(x)

    return


GraphG = []
GraphH = []
while True:
    try:
        line = input()
        create_list(line)
        get_edges(line)
    except EOFError:
        break

sort_graph(GraphG)
print_Graph(GraphG)  # degree of GraphG
reversed_Graph(GraphG, GraphH)
sort_graph(GraphH)
print_Graph(GraphH)

del GraphG[:]
del GraphH[:]
