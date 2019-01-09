def create_list(l, v):
    for x in range(v):
        l.append([])

    return


def get_edges(l, v, e):
    for x in range(e):
        while True:
            try:
                v1, v2 = map(int, input().split())
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


def print_graph(l):
    print("Graph by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(l)):
        deg_v = len(l[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        print("v" + str(x) + ":", l[x], "deg(v" + str(x) + "):", deg_v)

    print("\ndeg(Graph):", deg_graph)
    return


def sort_graph(l):
    for x in range(len(l)):
        l[x].sort()

    return


def dfs(l, start_v):
    dfs_arr = []
    Stack = []
    Stack.append(start_v)
    dfs_arr.append(start_v)  # 0 is start vertex
    while Stack:
        v = Stack.pop()  # current vertex
        for x in l[v]:
            if x not in dfs_arr:
                Stack.append(v)
                Stack.append(x)
                dfs_arr.append(x)
                break

    print_dfs(dfs_arr)
    del dfs_arr[:]
    del Stack[:]
    return


def print_dfs(l):
    return print(' '.join(str(x) for x in l))


graph = []
v = e = -1
while v < 0 or e < 0:
    try:
        v, e = map(int, input("Enter the number of vertices and edges: ").split())
    except ValueError:
        print("Enter correct values")

create_list(graph, v)
get_edges(graph, v, e)
print_graph(graph)
sort_graph(graph)
start_v = -1
while start_v < 0:
    try:
        start_v = int(input("Enter the start vertex number: "))
    except ValueError:
        print("Enter correct value")
dfs(graph, start_v)
del graph[:]
