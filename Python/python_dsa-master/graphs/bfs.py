#!/usr/bin/python3
# Implement breadth first search
from collections import deque


def bfs(graph, start):
    # Implement breadth first search
    queue = deque([start])
    level = {start: 0}
    parent = {start: None}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:
                queue.append(n)
                level[n] = level[v] + 1
                parent[n] = v
    return level, parent

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
    }
    print(bfs(graph, 'A'))
