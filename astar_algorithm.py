import heapq
import math

def heuristic(node1, node2, graph):

    x1 = graph.nodes[node1]['x']
    y1 = graph.nodes[node1]['y']
    x2 = graph.nodes[node2]['x']
    y2 = graph.nodes[node2]['y']

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path

def astar_search(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0,start))

    came_from = {}

    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal, graph)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph.neighbors(current):

            edge_data = graph.get_edge_data(current, neighbor)
            weight = edge_data[0]['length']

            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, graph)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None