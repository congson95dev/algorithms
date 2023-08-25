"""
Ý tưởng: 
Là thuật toán tìm kiếm áp dụng trên graph.
Tìm kiếm lần lượt theo chiều rộng, 
và nhét các node liên kết với node đang trỏ vào 1 queue 
và tiếp tục tìm kiếm cho tới khi nào tìm thấy shortest path.
"""

from collections import deque


def bfs_shortest_path(graph, start, end):
    queue = deque()
    visited = set()
    parent = {}

    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current_vertex = queue.popleft()
        if current_vertex == end:
            break

        neighbors = graph[current_vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_vertex

    if end not in parent:
        return None

    # find the shortest path by collect information from "parent"
    shortest_path = []
    vertex = end
    while vertex is not None:
        shortest_path.append(vertex)
        vertex = parent[vertex]

    shortest_path.reverse()
    return shortest_path


graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['b', 'c', 'e'],
    'e': ['d'],
}
start_vertex = 'a'
end_vertex = 'e'
shortest_path = bfs_shortest_path(graph, start_vertex, end_vertex)

if shortest_path:
    print("Shortest way from", start_vertex, "to", end_vertex, "is:", shortest_path)
else:
    print("Don't found the shortest way from", start_vertex, "to", end_vertex)
