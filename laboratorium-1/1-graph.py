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

    return


def print_graph(l):
    print("Graph by Pawel Labuda\nweb: http://itvix.pl\n")
    deg_graph = 0
    for x in range(len(l)):
        deg_v = 0
        for y in l:
            for z in y:
                if x == z:
                    deg_v += 1

        deg_v += len(l[x]) - l[x].count(x)
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        print("v" + str(x) + ":", l[x], "deg(v" + str(x) + "):", deg_v)

    print("\ndeg(Graph):", deg_graph)
    return


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
del graph[:]
