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


def print_graph():
    deg_graph = 0
    for x in range(len(Graph)):
        deg_v = len(Graph[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [x + 1 for x in Graph[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("deg(Graph):", deg_graph, "\n")
    return deg_graph


def merge(l, r):
    arr = []
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            arr.append(l[0])
            l.remove(l[0])
        else:
            arr.append(r[0])
            r.remove(r[0])

    if len(l) == 0:
        arr += r
    else:
        arr += l

    return arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        m = len(arr) // 2
        l = merge_sort(arr[:m])
        r = merge_sort(arr[m:])
        return merge(l, r)


def bubble_sort(arr):
    l = [x for x in range(len(arr))]

    for x in range(len(arr) - 1, 0, -1):
        for y in range(x):
            if arr[y] < arr[y + 1]:
                a = arr[y]
                arr[y] = arr[y + 1]
                arr[y + 1] = a

                a = l[y]
                l[y] = l[y + 1]
                l[y + 1] = a

    return l


def sort_graph():
    for x in range(len(Graph)):
        Graph[x] = merge_sort(Graph[x])

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


def print_colored(l, meth, opt):
    for x in range(len(Graph)):
        color = "0;30;" + str(40 + l[x] + 1)
        print("v" + str(x + 1), "colored on", "\x1b[" + color + "m       \x1b[0m", l[x])

    if opt == 0:
        print("Kolorowanie metodą", meth + ":", l, "\n")
    elif opt == 1:
        print("(liczba chromatyczna = " + str(max(l) + 1) + ")", "\n")
    elif opt == 2:
        print("Kolorowanie metodą", meth + ":", l, "(liczba chromatyczna = " + str(max(l) + 1) + ")", "\n")

    return


def color_graph(method, opt):
    l = [len(Graph[x]) for x in range(len(Graph))]
    sorted_list = []
    if method == "LF":
        sorted_list = bubble_sort(l)
    elif method == "SL":
        sorted_list = bubble_sort(l)[::-1]

    #print(sorted_list)
    ColorArr = [-1] * len(Graph)

    while sorted_list:
        v = sorted_list.pop(0)
        colored = [False] * len(Graph)
        for x in Graph[v]:
            if ColorArr[x] > -1:
                colored[ColorArr[x]] = True

        for x in range(len(colored)):
            if not colored[x]:
                ColorArr[v] = x
                break

        del colored[:]

    print_colored(ColorArr, method, opt)
    del ColorArr[:]
    del sorted_list[:]
    del l[:]
    return


Graph = []
option = 2  # 0 - print color; 1 - print chromatic number; 2 - 0 & 1
while True:
    try:
        line = input()
        create_list(line)
        get_edges(line)
    except EOFError:
        break

sort_graph()
# print_graph()
color_graph("LF", option)
color_graph("SL", option)

del Graph[:]
