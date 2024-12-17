import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def tsp_nn(self):
        visited = [False] * self.vertices
        path = [0]
        visited[0] = True

        for _ in range(self.vertices - 1):
            curr_vertex = path[-1]
            nearest_neighbor = sys.maxsize
            next_vertex = -1

            for vertex in range(self.vertices):
                if not visited[vertex] and self.graph[curr_vertex][vertex] < nearest_neighbor:
                    nearest_neighbor = self.graph[curr_vertex][vertex]
                    next_vertex = vertex

            path.append(next_vertex)
            visited[next_vertex] = True

        path.append(0)  # Return to the starting node
        return path

# Create a graph
g = Graph(6)
g.add_edge(0, 1, 100)  # Nairobi - Kirinyaga
g.add_edge(0, 2, 200)  # Nairobi - Meru
g.add_edge(0, 3, 150)  # Nairobi - Nyeri
g.add_edge(1, 2, 50)   # Kirinyaga - Meru
g.add_edge(1, 3, 80)   # Kirinyaga - Nyeri
g.add_edge(2, 3, 100)  # Meru - Nyeri
g.add_edge(2, 4, 250)  # Meru - Nandi
g.add_edge(3, 4, 200)  # Nyeri - Nandi
g.add_edge(3, 5, 180)  # Nyeri - Kisumu
g.add_edge(4, 5, 300)  # Nandi - Kisumu

# Solve the TSP using the Nearest Neighbor heuristic
path = g.tsp_nn()

# Print the path
for vertex in path:
    print(vertex)
