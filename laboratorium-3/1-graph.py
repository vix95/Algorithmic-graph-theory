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
    Graph[v2].append(v1)

    return


def print_Graph():
    print("Bipartite graph by Pawel Labuda\nweb: http://itvix.pl\n")
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


def get_count_empty(l):
    qty = 0
    for x in Graph:
        if len(x) == 0:
            qty += 1

    return qty


def check_is_connected():
    visited = [False] * len(Graph)
    Stack = []
    Stack.append(0)
    visited[0] = True
    while Stack:
        v = Stack.pop(0)
        for x in Graph[v]:
            if not visited[x] and len(Graph[v]) != 0:
                visited[x] = True
                Stack.append(x)

    del Stack[:]

    count_empty = get_count_empty(Graph)  # substract empty vertexes

    if visited.count(True) == len(Graph) - count_empty:
        del visited[:]
        return True
    else:
        del visited[:]
        return False


def check_is_bipartite():
    Arr = ["blank"] * len(Graph)
    Stack = []
    for x in range(len(Graph)):
        if Arr[x] == "blank":
            Arr[x] = "X"
            Stack.append(x)
            while Stack:
                v = Stack.pop(0)
                for y in Graph[v]:
                    if Arr[y] == Arr[v]:
                        del Arr[:]
                        del Stack[:]
                        return print("isn't bipartite")
                    if Arr[y] == "blank":
                        Arr[y] = "X" if Arr[v] == "Y" else "Y"
                        Stack.append(y)

    print("X =", [x + 1 for x in range(len(Arr)) if Arr[x] == "X"])
    print("Y =", [x + 1 for x in range(len(Arr)) if Arr[x] == "Y"])
    del Arr[:]
    del Stack[:]
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
# print_Graph(Graph)  # degree of Graph
#if check_is_connected():
check_is_bipartite()
#else:
#    print("isn't connected")

del Graph[:]
