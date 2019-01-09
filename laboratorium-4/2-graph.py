class Graph:
    def __init__(self):
        self.G = []
        self.H = []
        return

    def completing_graph(self):
        for x in range(len(self.G)):
            self.H.append([])
            Stack = self.G[x]
            v = Stack.pop(0) if Stack else -1
            for y in range(len(self.G)):
                if y != v:
                    self.H[x].append(y)
                    if y == x:
                        self.H[x].append(y)
                else:
                    v = Stack.pop(0) if Stack else -1

            del Stack[:]
        return

    def __del__(self):
        return


def create_list(line):
    for x in range(2):
        v = int(line.split()[x])
        if len(G.G) < v:
            for y in range(v - len(G.G)):
                G.G.append([])

    return


def get_edges(line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    G.G[v1].append(v2)
    G.G[v2].append(v1)

    return


def print_graph(l):
    deg_graph = 0
    for x in range(len(l)):
        deg_v = len(l[x])
        deg_graph = deg_v if deg_v > deg_graph else deg_graph
        vertex = [x + 1 for x in l[x]]
        print("v" + str(x + 1) + ":", vertex, "deg(v" + str(x + 1) + "):", deg_v)
        del vertex[:]

    print("deg(Graph):", deg_graph, "\n")
    return deg_graph


def sort_graph(l):
    for x in range(len(l)):
        l[x].sort()

    return


def get_count_empty(l):
    qty = 0
    for x in l.G:
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


G = Graph()
while True:
    try:
        line = input()
        create_list(line)
        get_edges(line)
    except EOFError:
        break

sort_graph(G.G)
print_graph(G.G)
G.completing_graph()
print_graph(G.H)
