def create_list(line):
    for x in range(2):
        v = int(line.split()[x])
        if len(Graph) < v:
            for y in range(v - len(Graph)):
                Graph.append([])

    return


def get_edges(line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    Graph[v1].append(v2)

    return


def print_Graph():
    deg_graph = 0
    for x in range(len(Graph)):
        deg_v = len(Graph[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [x + 1 for x in Graph[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("\ndeg(Graph):", deg_graph)
    return deg_graph


def sort_graph():
    for x in range(len(Graph)):
        Graph[x].sort()

    return


def in_out_deg():
    indeg = outdeg = 0

    # indeg
    for x in range(len(Graph)):
        is_exists = False
        for y in range(len(Graph)):
            if Graph[y].count(x) > 0:
                is_exists = True
                break

        if not is_exists:
            indeg += 1

    # outdeg
    for x in range(len(Graph)):
        if not len(Graph[x]):
            outdeg += 1

    return print("zrodel jest (indeg = 0):", indeg, "\nujsc jest (outdeg = 0):", outdeg)


Graph = []
while True:
    try:
        line = input()
        create_list(line)
        get_edges(line)
    except EOFError:
        break

sort_graph()
print_Graph()  # degree of Graph
in_out_deg()

del Graph[:]
