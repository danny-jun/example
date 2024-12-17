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

# Create a graph with 6 vertices (Nairobi, Nyeri, Nakuru, Laikipia, Nandi, Meru)
g = Graph(6)

# Add edges with distances
g.add_edge(0, 1, 143)  # Nairobi - Nyeri
g.add_edge(0, 2, 159)  # Nairobi - Nakuru
g.add_edge(0, 3, 265)  # Nairobi - Laikipia
g.add_edge(0, 4, 90)  # Nairobi - Nandi
g.add_edge(0, 5, 225)  # Nairobi - Meru
g.add_edge(1, 2, 166)  # Nyeri - Nakuru
g.add_edge(1, 3, 130)   # Nyeri - Laikipia
g.add_edge(1, 4, 214)  # Nyeri - Nandi
g.add_edge(1, 5, 136)  # Nyeri - Meru
g.add_edge(2, 3, 249)  # Nakuru - Laikipia
g.add_edge(2, 4, 156)  # Nakuru - Nandi
g.add_edge(2, 5, 256)  # Nakuru - Meru
g.add_edge(3, 4, 186)  # Laikipia - Nandi
g.add_edge(3, 5, 143)  # Laikipia - Meru
g.add_edge(4, 5, 281)  # Nandi - Meru

# Solve the TSP using the Nearest Neighbor heuristic
path = g.tsp_nn()

# Print the path
cities = ["Nairobi", "Nyeri", "Nakuru", "Laikipia", "Nandi", "Meru"]
for vertex in path:
    print(cities[vertex])
