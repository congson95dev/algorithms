"""
Ý tưởng:
Đi qua từng node, update shortest distance và previous node khi gặp được distance ngắn hơn, 
sau đó truy ngược lại từ previous node để truy ra được quãng đường với chi phí ít nhất.

Steps:
1. lấy node hợp lệ ra để xét
2. lấy node gần với node đang xét nhất
3. tính và update distance vào bảng, đồng thời update parent node
4. add note này vào array đã xét duyệt
5. back lại step 1

Note: 
Ở bước tính distance, check cả 2 nếu có distance nhỏ hơn distance gốc thì update
Ở bước chọn next node để đi tiếp, check distance trong bảng chọn node có distance nhỏ nhất && chưa được visited để làm next node
Ở bước tính distance, nếu distance mới = distance gốc thì không cần update
Ở bước chọn next node, nếu tới đỉnh cuối (đỉnh mà không còn neighbor nào unvisited) thì dừng thuật toán
"""


import sys


def dijsktra(graph, source, destination):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[source] = 0
    visited = set()
    path = {source: []}

    while True:
        min_distance = sys.maxsize
        min_vertex = None
        # Calculate which node is the next node
        # The smallest distance node will be the next node
        for vertex in graph:
            if distances[vertex] < min_distance and vertex not in visited:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Break if don't found the next node
        if min_vertex is None:
            break

        # Mark the node as visited
        visited.add(min_vertex)

        # Calculate the new distance of the node and update it if it's smaller than the current distance
        for neighbor, weight in graph[min_vertex].items():
            new_distance = distances[min_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # In this example, instead of update the parent node to the list as in theory,
                # we update the full path of it
                path[neighbor] = path[min_vertex] + [min_vertex]

    shortest_path = path[destination] + [destination]
    print(f"Đường đi ngắn nhất từ {source} đến {destination}: {' -> '.join(shortest_path)}")

    return distances[destination]


graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
    'E': {'C': 5, 'D': 11, 'F': 1},
    'F': {'D': 22, 'E': 1}
}

source = 'A'
destination = 'F'

shortest_distance = dijsktra(graph, source, destination)
print(f"Khoảng cách ngắn nhất từ {source} đến {destination} là: {shortest_distance}")


# """
# The below example is using `heap`, which make it more effection than normal
# which will make the time complexity to become `O((V + E) log V)`, which V is node, and E is edge
# meanwhile, if not using `heap`, it's O(V^2)
# https://www.youtube.com/watch?v=OrJ004Wid4o
# """
# import sys
# from heapq import heapify, heappush, heappop

# def dijsktra(graph,src,dest):
#     inf = sys.maxsize
#     node_data = {'A':{'cost':inf,'pred':[]},
#     'B':{'cost':inf,'pred':[]},
#     'C':{'cost':inf,'pred':[]},
#     'D':{'cost':inf,'pred':[]},
#     'E':{'cost':inf,'pred':[]},
#     'F':{'cost':inf,'pred':[]}
#     }
#     node_data[src]['cost'] = 0
#     visited = []
#     temp = src
#     for i in range(5):
#         if temp not in visited: # TODO: Reassign source
#             visited.append(temp)
#             min_heap = []
#             for j in graph[temp]:
#                 if j not in visited:
#                     cost = node_data[temp]['cost'] + graph[temp][j]
#                     if cost < node_data[j]['cost']:
#                         node_data[j]['cost'] = cost
#                         node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
#                     heappush(min_heap,(node_data[j]['cost'],j))
#         heapify(min_heap)
#         temp = min_heap[0][1]
#     print("Shortest Distance: " + str(node_data[dest]['cost']))
#     print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


# if __name__ == "__main__":
#     graph = {
#         'A':{'B':2,'C':4},
#         'B':{'A':2,'C':3,'D':8},
#         'C':{'A':4,'B':3,'E':5,'D':2},
#         'D':{'B':8,'C':2,'E':11,'F':22},
#         'E':{'C':5,'D':11,'F':1},
#         'F':{'D':22,'E':1}
#     }

#     source = 'A'
#     destination = 'F'
#     dijsktra(graph,source,destination)
