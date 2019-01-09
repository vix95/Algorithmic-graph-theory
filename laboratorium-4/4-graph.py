class Graph:
    def __init__(self):
        self.G = []  # first graph
        self.H = []  # square of graph
        return

    def copy_vertexes(self, l):
        arr = []
        for x in range(len(l)):
            arr.append([])

        return arr

    def copy_list(self, l):
        arr = []
        for x in l:
            arr.append(x)

        return arr

    def square_graph(self, l):
        G.H = self.copy_vertexes(l)
        for x in range(len(l)):
            G.H[x] = self.copy_list(l[x])  # if you want to square graph for undirected you have to comment this one
            for y in l[x]:
                for z in l[y]:
                    if G.H[x].count(z) == 0:
                            G.H[x].append(z)

        return

    def __del__(self):
        return


def create_list(line):
    for x in range(2):
        v = int(line.split()[x])
        if len(G.G) < v:
            for y in range(v - len(G.G)):
                G.G.append([])
                G.H.append([])
    return


def get_edges(line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    G.G[v1].append(v2)
    # G.G[v2].append(v1)  # if you want to square graph for undirected you have to uncomment this one
    G.H.append([])

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
G.square_graph(G.G)
sort_graph(G.H)
print_graph(G.H)
