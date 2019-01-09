def create_list(l, v):
    for x in range(v):
        l.append([])

    return


def get_edges(l, v, e):
    for x in range(e):
        while True:
            try:
                # v1, v2 = map(int, input().split())
                v1, v2 = map(int, file.readline().split())
                if v1 not in range(v) or v2 not in range(v):
                    print("Bad values, vertex must be in range 0 -", v - 1)
                    print("Insert correct values, please.")
                else:
                    break
            except ValueError:
                print("Enter correct values, v1 v2.")

        l[v1].append(v2)
        l[v2].append(v1)

    return


def print_Graph(l):
    print("Graph by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(l)):
        deg_v = len(l[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        print("v" + str(x) + ":", l[x], "deg(v" + str(x) + "):", deg_v)

    print("\ndeg(Graph):", deg_graph)
    return deg_graph


def check_is_cyclic_unconnected(l):
    visited = [False] * len(l)
    for x in range(len(l)):
        if visited[x]:
            pass
        elif check_is_vertex_cyclic(l, x, visited):
            del visited[:]
            return print("Graph is cyclic")

    del visited[:]
    return print("Graph isn't cyclic")


def check_is_vertex_cyclic(l, v, visited):
    Stack = []
    Stack.append(v)
    Stack.append(-1)
    visited[v] = True
    while Stack:
        p = Stack.pop(0)  # previous vertex
        v = Stack.pop(0)  # current vertex
        for x in l[v]:
            if not visited[x]:
                Stack.append(x)
                Stack.append(v)
                visited[x] = True
            elif x != p:
                del Stack[:]
                return True

    del Stack[:]
    return False


def sort_graph(l):
    for x in range(len(l)):
        l[x].sort()

    return


def check_is_connected(l):
    visited = [False] * len(l)
    Stack = []
    Stack.append(0)
    visited[0] = True
    counter = 0
    while Stack:
        v = Stack.pop(0)
        counter += 1
        for x in l[v]:
            if not visited[x]:
                visited[x] = True
                Stack.append(x)

    if counter == len(l):
        print("Graph is connected")
        return True

    del visited[:]
    del Stack[:]
    print("Graph isn't connected")
    return False


def check_is_cyclic_connected(l, n):
    visited = [False] * len(l)
    Stack = []
    Stack.append(0)
    Stack.append(-1)
    visited[0] = True
    while Stack:
        p = Stack.pop(0)  # previous vertex
        v = Stack.pop(0)  # current vertex
        for x in l[v]:
            if not visited[x]:
                Stack.append(x)
                Stack.append(v)
                visited[x] = True
            elif x != p:
                del visited[:]
                del Stack[:]
                if n == len(l):
                    print("Graph is C_n =", n)
                else:
                    print("Graph isn't C_n =", n)

                return print("Graph isn't tree")

    del visited[:]
    del Stack[:]
    print("Graph isn't C_n =", n)
    return print("Graph is tree")


def check_is_fully(l):
    for x in range(len(l)):
        for y in l[x]:
            for z in range(len(l)):
                if z not in l[x]:
                    return print("Graph isn't fully")

    return print("Graph is fully")


def check_is_k_regular(l, deg_graph, n):
    for x in range(len(l)):
        deg_v = len(l[x])
        if deg_graph != deg_v:
            print("Graph isn't k regular")
            print("Graph isn't K_n =", n)
            return

    print("Graph is k regular")
    if deg_graph == n:
        print("Graph is K_n =", n)
    else:
        print("Graph isn't K_n =", n)
    return


file = open("tests.txt")
n = int(file.readline())
for x in range(n):
    Graph = []
    v = e = -1
    while v < 0 or e < 0:
        try:
            # v, e = map(int, input("Enter the number of vertices and edges: ").split())
            v, e = map(int, file.readline().split())
        except ValueError:
            print("Enter correct values")

    create_list(Graph, v)
    get_edges(Graph, v, e)
    sort_graph(Graph)
    deg_graph = print_Graph(Graph)  # degree of Graph
    if check_is_connected(Graph):
        n = -1
        while n < 0:
            try:
                n = int(input("Enter C_n: "))
            except ValueError:
                print("Enter correct value")

        check_is_cyclic_connected(Graph, n)
    else:
        check_is_cyclic_unconnected(Graph)

    check_is_fully(Graph)

    n = -1
    while n < 0:
        try:
            n = int(input("Enter K_n: "))
        except ValueError:
            print("Enter correct value")
    check_is_k_regular(Graph, deg_graph, n)

    del Graph[:]
    print("\n\n-------")
    file.readline()  # read empty line
