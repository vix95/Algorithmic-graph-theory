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
    print("Euler path & cycle by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(Graph)):
        deg_v = len(Graph[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [y + 1 for y in Graph[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("\ndeg(Graph):", deg_graph)
    return


def sort_graph():
    for x in range(len(Graph)):
        Graph[x].sort()

    return


def check_is_connected(l, n, qty):
    visited = [False] * len(l)
    Stack = []
    Stack.append(n)
    visited[n] = True
    while Stack:
        v = Stack.pop(0)
        for x in l[v]:
            if not visited[x]:
                visited[x] = True
                Stack.append(x)

    del Stack[:]

    if visited.count(True) == qty:
        del visited[:]
        return True
    else:
        del visited[:]
        return False


def set_vertex(G):
    for x in range(len(G)):
        if len(G[x]) % 2 != 0:
            return x, True

    return 0, False


def set_ind(l, n):
    for x in range(len(l)):
        if l[x] == n:
            return x


def get_qty(l):
    qty = 0
    ind = 0
    for x in l:
        if x > 0:
            qty += 1
        else:
            # if is exists vertex but is empty, we have to check it
            for y in range(len(Graph)):
                for z in Graph[y]:
                    if z == ind:
                        qty += 1

        ind += 1

    return qty


def find_path_or_cycle():
    Stack = []
    G = Graph

    n, semi = set_vertex(G)  # set first vertex; if odd then set
    edges = [len(G[x]) for x in range(len(G))]
    while sum(edges) > 0:
        c = n
        for n in G[c]:
            is_connected = check_is_connected(G, c, get_qty(edges))
            if is_connected:
                v = set_ind(G[n], c)
                G[c].pop(0); edges[c] -= 1
                if sum(edges) > 2:
                    is_connected = check_is_connected(G, n, get_qty(edges))
                else:
                    is_connected = True

                if is_connected:
                    Stack.append(c + 1)  # vertex start name from 1
                    break
                else:
                    G[c].append(n); edges[c] += 1
                    n = c
                    break

    if not semi:
        Stack.append(Stack[0])
    else:
        Stack.append(n + 1)

    return Stack


def check_is_euler():
    DegGraph = [len(Graph[x]) for x in range(len(Graph))]
    for x in range(len(Graph)):
        for y in Graph[x]:
            DegGraph[y] += 1

    odd = 0
    for x in DegGraph:
        if x % 2 != 0:
            odd += 1

    del DegGraph[:]

    if odd == 0:
        print("Graph is eulerian")
        print("Path:", find_path_or_cycle())
    elif odd <= 2:
        print("Graph is semi-eulerian")
        print("Cycle:", find_path_or_cycle())
    else:
        print("Graph isn't eulerian")

    return


Graph = []
while True:
    try:
        line = input()
        create_list(line)
        get_edges(line)
    except EOFError:
        break

sort_graph()
# print_Graph()  # degree of Graph
if check_is_connected(Graph, 0, len(Graph)):
    check_is_euler()
else:
    print("Graph isn't connected")

del Graph[:]
