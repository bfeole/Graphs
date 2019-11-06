
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


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
#                   (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 1))


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

    visited = set()

    # While the stack is not empty...
    while s.size() > 0:
        # pop the first vertex
        path = s.pop()
        print(f"path{path}")
        # set var for last element in vertex
        vertex = path[-1]

        # if we have vertex in graph
        # if not graph.vertices[vertex]:
        # if vertex not in visited:
        #     # print(deep_path)
        #     deep_path.append([vertex])
        #     visited.add([vertex])

        if len(path) > len(deep_path):
            deep_path = path
            print(f"deep path 1{deep_path}")
        if len(path) <= len(deep_path):
            deep_path = path
            if path[-1] == deep_path[-1]:
                deep_path = path
                print(f"deep path 2{deep_path}")

        for neighbor in graph.vertices[vertex]:

            for neighbor in graph.vertices[vertex]:
                path_copy = path.copy()
                path_copy.append(neighbor)
                print(f"path copy {path_copy}")
                s.push(path_copy)
                # q.enqueue(neighbor)
                # print(neighbor)

    if len(path) == 1:
        print(f"edge case{len(path)}")
        return -1

    if len(path_copy[-1]) == len(path_copy[-2]):
        print(path_copy[-2][-1])
        return path_copy[-2][-1]
    else:
        return path_copy[-1][-1]

        # if not deep_path[-1]:
        #     return -1
    print(f"deep path return {deep_path[-1]}")
    return deep_path[-1]

    # Given the dataset and the ID of an individual node/vert
    # return the vert farthest away from the starting vert
    # if more than one vert tied for distance, return the lowest numeric ID.
    # If no parent nodes/verts, return -1


# print(earliest_ancestor(test_ancestors, 1))
