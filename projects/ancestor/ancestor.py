
from util import Stack


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

    # Create edges
    for node in ancestors:
        graph.add_edge(node[1], node[0])

    # Start DFS with starting node
    s = Stack()
    s.push([starting_node])
    deep_path = []

    # While the stack is not empty...
    while s.size() > 0:
        # pop the first vertex
        path = s.pop()
        print(f"first pop path{path}")
        # set var for last element in vertex
        vertex = path[-1]
        print(f"vertex = path[-1]{path[-1]}")

        if len(path) > len(deep_path):
            print(f"is len {len(path)} > len {len(deep_path)}")
            print(f"deep_path{deep_path} = path{path}")
            deep_path = path
        if len(path) == len(deep_path):
            print(f"is {path[-1]} < {deep_path[-1]}")
            if path[-1] < deep_path[-1]:
                print(f"{deep_path} = {path}")
                deep_path = path
                # print(f"deep path 2{deep_path}")

        for neighbor in graph.vertices[vertex]:
            path_copy = path.copy()
            path_copy.append(neighbor)
            print(f"path copy {path_copy}")
            s.push(path_copy)

    if len(path) == 1:
        print(f"edge case{len(path)}")
        return -1

    print(f"deep path return {deep_path[-1]}")
    print('BREAK __ ')
    return deep_path[-1]

    # Given the dataset and the ID of an individual node/vert
    # return the vert farthest away from the starting vert
    # if more than one vert tied for distance, return the lowest numeric ID.
    # If no parent nodes/verts, return -1


an_test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
           (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


# earliest_ancestor(an_test, 1)
# earliest_ancestor(an_test, 3)
earliest_ancestor(an_test, 8)
