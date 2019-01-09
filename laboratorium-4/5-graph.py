class Graph:
    def __init__(self):
        self.G = []
        self.paths = []
        self.max_paths = []
        self.max_path = 0
        return

    @staticmethod
    def print_max_paths(p, max_p):
        print("Max of path:", max_p)
        for x in range(len(p)):
            arr = [y + 1 for y in p[x]]
            print("Path", str(x + 1) + ":", arr)
            del arr[:]

        return

    def find_the_longest_path(self, l):
        for x in range(len(l)):
            for y in range(len(l)):
                if x != y:
                    visited = [False] * len(l)
                    path = []
                    self.max_path = max([len(z) for z in self.paths]) if self.paths else 0
                    self.get_paths(l, x, y, visited, path)
                    del visited [:]
                    del path[:]

        # get only the longest paths
        self.max_paths = [x for x in self.paths if len(x) == self.max_path]

        self.print_max_paths(self.max_paths, self.max_path)
        return

    def get_paths(self, l, v, u, visited, path):
        # recursive get paths
        path.append(v)
        visited[v] = True

        if v == u and len(path) >= self.max_path:
            self.paths.append([])
            for x in path:
                self.paths[len(self.paths) - 1].append(x)
        else:
            for x in l[v]:
                if not visited[x]:
                    self.get_paths(l, x, u, visited, path)

        path.pop()
        visited[v] = False

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
G.find_the_longest_path(G.G)

del G
