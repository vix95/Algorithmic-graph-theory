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


def print_graph(l, offset_v):
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
        if x > offset_v - 1:
            print("v" + str(x + 1) + ":", l[x], "deg(v" + str(x) + "):", deg_v)
        else:
            print("v" + str(x) + ":", l[x], "deg(v" + str(x) + "):", deg_v)

    print("\ndeg(Graph):", deg_graph)
    return


def delete_vertex(l):
    while True:
        try:
            v = int(input("Enter vertex which you want to remove: "))
            if v not in range(int(len(l))):
                print("Bad value, vertex must be in range 0 -", int(len(l)) - 1)
                print("Insert correct values, please.")
            else:
                break
        except ValueError:
            print("Enter correct values")

    l.pop(v - 1)
    for x in range(len(l)):
        count = 0
        for y in l[x]:
            if y == v:
                l[x].pop(count)

            count += 1

    return v


def delete_edge(l, del_v):
    while True:
        try:
            v1, v2 = map(int, input("Enter edges (from v1 to v2) which you want to remove: ").split())
            if v1 not in range(int(len(l) + 1)) or v2 not in range(int(len(l) + 1)):
                print("Bad value, edges must be in range 0 -", int(len(l)))
                print("Insert correct values, please.")
            else:
                break
        except ValueError:
            print("Enter correct values, v1, v2")

    if v1 >= del_v:
        v1 -= 1
    for x in range(len(l)):
        if x == v1:
            count = 0
            for y in l[x]:
                if y == v2:
                    l[x].pop(count)

                count += 1
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
print_graph(graph, v)
del_v = delete_vertex(graph)
print_graph(graph, del_v)
delete_edge(graph, del_v)
print_graph(graph, del_v)
del graph[:]
