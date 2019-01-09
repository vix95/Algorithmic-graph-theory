class Graph:
    def __init__(self):
        self.G = []  # first graph
        self.E = []  # first graph with numeric edges
        self.H = []  # edge graph with double edges
        self.cH = []  # correct edge graph
        self.EdgeList = []  # edge list (1-2; 2-3; 3-4...)
        self.edge_count = 0  # count using by E graph
        return

    def edge_graph(self):
        for x in range(len(self.G)):
            i = 0
            for y in self.G[x]:
                edge_in = self.E[x][i]
                j = 0
                for z in self.G[y]:
                    if z != x:
                        edge_out = self.E[y][j]
                        self.H[edge_in].append(edge_out)
                        self.H[edge_out].append(edge_in)

                    j += 1
                i += 1
        return

    def create_correct_edge_graph(self, l):
        for x in range(len(l)):
            for y in range(len(l)):
                count = l[x].count(y)
                for z in range(int(count / 2)):
                    self.cH[x].append(y)

        return

    def __del__(self):
        return


def create_list(line):
    for x in range(2):
        v = int(line.split()[x])
        if len(G.G) < v:
            for y in range(v - len(G.G)):
                G.G.append([])
                G.E.append([])
    return


def get_edges(line):
    v1, v2 = map(int, line.split())
    v1 -= 1
    v2 -= 1

    G.G[v1].append(v2)
    G.G[v2].append(v1)
    G.E[v1].append(G.edge_count)
    G.E[v2].append(G.edge_count)
    G.H.append([])
    G.cH.append([])
    G.EdgeList.append([])
    G.EdgeList[G.edge_count].append(str(v1) + "-" + str(v2))
    G.edge_count += 1

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

G.edge_graph()
sort_graph(G.G)
print_graph(G.G)
sort_graph(G.H)
G.create_correct_edge_graph(G.H)
sort_graph(G.cH)
print_graph(G.cH)
