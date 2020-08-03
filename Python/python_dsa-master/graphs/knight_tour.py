#!/usr/bin/python3
# Solve the Knight's tour problem using depth first search
# (visit every space on the chess board)
from graphs import Graph, Vertex


def knight_tour(n, path, u, limit):
    # Solve the Knight's tour problem using depth first search
    # n: current depth in the search tree
    # path: list of vertices visited up to this point
    # u: vertex in the graph to explore
    # limit: number of nodes in the path
    u.set_color('gray')
    path.append(u)
    if n < limit:
        number_list = order_by_avail(u)
        i = 0
        done = False
        while i < len(number_list) and not done:
            if number_list[i].get_color() == 'white':
                done = knight_tour(n + 1, path, number_list[i], limit)
            i += 1
        if not done:  # prepare to backtrack
            path.pop()
            u.set_color('white')
    else:
        done = True
    return done


def order_by_avail(n):
    # Select the vertext to visit next that has the fewest available moves
    result_list = []
    for v in n.get_connections():
        if v.get_color() == 'white':
            c = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    c += 1
            result_list.append((c, v))
    result_list.sort(key=lambda x: x[0])
    return [y[1] for y in result_list]


def knight_graph(board_size):
    # Build the graph
    graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            new_positions = generate_legal_moves(row, col, board_size)
            for e in new_positions:
                nid = pos_to_node_id(e[0], e[1], board_size)
                graph.add_edge(node_id, nid)
    return graph


def pos_to_node_id(row, column, board_size):
    # Convert row and column to linear vertex number
    return (row * board_size) + column


def generate_legal_moves(x, y, board_size):
    # Generate possible moves for knight
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if (legal_coordinate(new_x, board_size) and
                legal_coordinate(new_y, board_size)):
            new_moves.append((new_x, new_y))
    return new_moves


def legal_coordinate(x, board_size):
    # Make sure a move is still on the board
    return x >= 0 and x < board_size

if __name__ == '__main__':
    size = 8
    graph = knight_graph(size)
    path = []
    start = graph.get_vertex(0)
    visited = []
    knight_tour(0, path, start, size ** 2 - 1)
    for v in path:
        visited.append(v.get_id())
    print(visited)
