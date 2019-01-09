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
    print("Check if Graph is Euler by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(l)):
        deg_v = len(l[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [x + 1 for x in l[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("\ndeg(Graph):", deg_graph)
    return deg_graph


def sort_graph(l):
    for x in range(len(l)):
        l[x].sort()

    return


def get_count_empty(l):
    qty = 0
    for x in l:
        if len(x) == 0:
            qty += 1

    return qty


def check_is_connected(l):
    visited = [False] * len(l)
    Stack = []
    Stack.append(0)
    visited[0] = True
    while Stack:
        v = Stack.pop(0)
        for x in l[v]:
            if not visited[x] and len(l[v]) != 0:
                visited[x] = True
                Stack.append(x)

    del Stack[:]

    count_empty = get_count_empty(l)  # substract empty vertexes

    if visited.count(True) == len(l) - count_empty:
        del visited[:]
        return True
    else:
        del visited[:]
        return False


def check_is_euler(l):
    visited = [False] * len(l)
    Stack = []
    Stack.append(0)
    visited[0] = True
    while Stack:
        v = Stack.pop()
        for x in l[v]:
            if not visited[x] and len(l[v]) != 0:
                visited[x] = True
                Stack.append(x)

    del visited[:]
    del Stack[:]

    DegGraph = [len(l[x]) for x in range(len(l))]
    odd = 0
    for x in DegGraph:
        if x % 2 != 0:
            odd += 1

    del DegGraph[:]

    if odd == 0:
        return print("eulerian")
    elif odd <= 2:
        return print("semi-eulerian")
    else:
        return print("connected")


Graph = []
while True:
    try:
        line = input()
        create_list(Graph, line)
        get_edges(Graph, line)
    except EOFError:
        break

sort_graph(Graph)
# print_Graph(Graph)  # degree of Graph
if check_is_connected(Graph):
    check_is_euler(Graph)
else:
    print("isn't connected")

del Graph[:]
