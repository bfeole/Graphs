
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
    # q = Queue()
    s = Stack()
    # q.enqueue([starting_node])
    s.push([starting_node])
    deep_path = []

    # visited = set()

    # While the stack is not empty...
    while s.size() > 0:
        # pop the first vertex
        path = s.pop()
        # set var for last element in vertex
        vertex = path[-1]

        # if we have vertex in graph
        if graph.vertices[vertex]:
            if len(path) > len(deep_path):
                deep_path = path
            if len(path) == len(deep_path):
                if path[-1] < deep_path[-1]:
                    deep_path = path

        for neighbor in graph.vertices[vertex]:
            path_copy = path.copy()
            path_copy.append(neighbor)
            s.push(path_copy)
            # q.enqueue(neighbor)
            # print(neighbor)

        # if not deep_path[-1]:
        #     return -1
    return deep_path[-1]

    # Given the dataset and the ID of an individual node/vert
    # return the vert farthest away from the starting vert
    # if more than one vert tied for distance, return the lowest numeric ID.
    # If no parent nodes/verts, return -1
