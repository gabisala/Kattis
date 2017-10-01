
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]


def create_adjacent_matrix(case):

    # Number of vertices in the graph
    num_vertices = data[0][0]

    # Map vertices to adjacency matrix
    keys = xrange(num_vertices)
    values = data[1:]
    adjacent_matrix = {k: v for k, v in zip(keys, values)}

    return adjacent_matrix


def find_edge(vertex):
    """
    Finds vertex edges
    :param vertex: a list of vertices
    :return: a list of adjacent vertices
    """

    return [i for i, v in enumerate(vertex) if v is 1]


def create_edge_vertices_mapping(adjacent_matrix):

    # Map vertices to neighbors
    edge_vertices = {key: find_edge(vertex) for key, vertex in adjacent_matrix.iteritems()}
    return edge_vertices


def find_conected_neighbors(edge_vertices, values):
    """
    Find connected vertices that are neighbors
    :param edge_vertices: a dict, vertices mapped to neighbors
    :param values: ints, neighbors
    :return: True if there are connected neighbors, False otherwise
    """

    neighbors = []
    connected = []

    for num in values:

        neighbors.append(num)
        connected.extend(edge_vertices[num])

    # print 'neighbors =', neighbors
    # print 'connected =', connected

    # Check if there are connected neighbors
    is_connected = False

    for n in neighbors:
        if n in connected:
            is_connected = True

    return is_connected


def find_weak_vertices(edge_vertices):
    """
    Find weak vertices in graphs – those vertices that is not part of any triangle.
    :param edge_vertices: a dict, vertices mapped to neighbors
    :return: a list of weak vertices
    """

    weak_vertices = []

    for k, v in edge_vertices.iteritems():

        # If no neighbors or 1
        if len(v) < 2:
            weak_vertices.append(k)

        # Otherwise check if there are other weak vertices
        else:
            if not find_conected_neighbors(edge_vertices, v):
                weak_vertices.append(k)

    return weak_vertices


# For each graph, produce a line listing the weak vertices ordered from least to greatest.
while data[0][0] != -1:

    final = data[0][0] + 1
    case = data[0: final]

    adjacent_matrix = create_adjacent_matrix(case)
    edge_vertices = create_edge_vertices_mapping(adjacent_matrix)
    weak_vertices = find_weak_vertices(edge_vertices)

    print ' '.join(map(str, (sorted(weak_vertices))))

    data = data[final:]
