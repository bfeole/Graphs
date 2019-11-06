
from util import Stack, Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):

        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()
    # pass all ancestors and relationships (parent/child) into graph

    # Create verts
    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
        graph.add_edge(node[1], node[0])

    # Create Edges
    # for node in ancestors:

    # Start DFS with starting node
    q = Queue()
    q.enqueue([starting_node])

    visited = set()

    while q.size() > 0:
        v = q.dequeue()
        if v not in visited:
            visited.add(v)
            for neighbors in graph.vertices[v]:
                q.enqueue(neighbors)
                print(neighbors)

    # Given the dataset and the ID of an individual node/vert
    # return the vert farthest away from the starting vert
    # if more than one vert tied for distance, return the lowest numeric ID.
    # If no parent nodes/verts, return -1
