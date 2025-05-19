class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def print_Graph(self, size):
        for r in range(size):
            for c in range(size):
                print(self.graph[r][c], end=' ')
            print()


G1 = Graph(4)
G3 = Graph(4)
G_self = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G1 무방향 그래프")
G1.print_Graph(G1.SIZE)


# 0 == A, 1 == B, 2 == C, 3 == D
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print("G3 방향 그래프")
G1.print_Graph(G3.SIZE)

# 0 == A, 1 == B, 2 == C, 3 == D
G_self.graph[0][3] = 1
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1
G_self.graph[2][1] = 1
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1

print("G_self 무방향 그래프")
G_self.print_Graph(G_self.SIZE)
