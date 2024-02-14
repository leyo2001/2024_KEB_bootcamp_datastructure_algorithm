class graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for i in range(size)] for i in range(size)]



g = graph(4)

g.graph[0][3] = 1
g.graph[1][3] = 1
g.graph[1][2] = 1

g.graph[3][0] = 1
g.graph[3][1] = 1
g.graph[2][1] = 1

for i in range(g.size):
    print()
    for j in range(g.size):
        print(g.graph[i][j], end=" ")















