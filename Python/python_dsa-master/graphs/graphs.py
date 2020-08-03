#!/usr/bin/python3
# Define vertex and graph
import sys


class Vertex:
    # Define vertex
    def __init__(self, key):
        # Initialize vertex
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def add_neighbor(self, number, weight=0):
        # Add connection to another vertex
        self.connected_to[number] = weight

    def set_color(self, color):
        # Set color
        self.color = color

    def set_distance(self, distance):
        # Set distance
        self.distance = distance

    def set_predecessor(self, predecessor):
        # Set predecessor
        self.predecessor = predecessor

    def set_discovery(self, d_time):
        # Set discovery time
        self.discovery = d_time

    def set_finish(self, f_time):
        # Set finish time
        self.finish = f_time

    def get_finish(self):
        # Get finish time
        return self.finish

    def get_discovery(self):
        # Get discovery time
        return self.discovery

    def get_predecessor(self):
        # Get predecessor
        return self.predecessor

    def get_distance(self):
        # Get distance
        return self.distance

    def get_color(self):
        # Get color
        return self.color

    def __str__(self):
        # Display vertex
        '''
        return (str(self.id) + ' connected to: ' +
                str([x.id for x in self.connected_to]))
        '''
        return (str(self.id) + ':color ' + self.color +
                ':discovery ' + str(self.discovery) +
                ':finish ' + str(self.finish) +
                ':distance ' + str(self.distance) +
                ':predecessor \n\t[' + str(self.predecessor) + ']\n')

    def get_connections(self):
        # Return all the vertices in the adjacency list
        return self.connected_to.keys()

    def get_id(self):
        # Return the id
        return self.id

    def get_weight(self, number):
        # Return the weight
        return self.connected_to[number]


class Graph:
    # Define graph
    def __init__(self):
        # Initialize graph
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        # Add vertex
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        # Return vertex with given key
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        # Check if key is in graph
        return n in self.vert_list

    def add_edge(self, f, t, weight=0):
        # Add edge
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        # Return names of all the vertices in the graph
        return self.vert_list.keys()

    def __iter__(self):
        # Iterate over all vertices
        return iter(self.vert_list.values())
