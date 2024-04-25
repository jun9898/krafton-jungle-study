infinity = float("inf")

def make_graph():
    # tuple = (cost, to_node)
    return {
        'A': [(10, 'B'), (30, 'C'), (15, 'D')],
        'B': [(20, 'E')],
        'C': [(5, 'F')],
        'D': [(5, 'C'), (20, 'F')],
        'E': [(20, 'F')],
        'F': [(20, 'D')]
    }

def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = dict.fromkeys(G.keys())

    for node in unvisited:
        shortest_paths[node] = (infinity, None)  # (최단 거리, 이전 노드)

    shortest_paths[start] = (0, None)

    while unvisited:
        min_node = None

        for node in unvisited:
            if min_node is None:
                min_node = node
            elif shortest_paths[node][0] < shortest_paths[min_node][0]:
                min_node = node

        for edge in G[min_node]:
            cost, to_node = edge
            new_distance = cost + shortest_paths[min_node][0]
            print(new_distance)

            if new_distance < shortest_paths[to_node][0]:
                shortest_paths[to_node] = (new_distance, min_node)

        del unvisited[min_node]

    return shortest_paths

def print_shortest_path(shortest_paths, start, end):
    path = []
    node = end
    print(shortest_paths, start, end)
    while node is not None:
        path.append(node)
        node = shortest_paths[node][1]

    if path[-1] == start:
        print(f'Shortest path from {start} to {end}: {path[::-1]}')
    else:
        print(f'No path from {start} to {end}')

def main():
    G = make_graph()
    start = 'A'
    end = 'F'

    shortest_paths = dijkstras(G, start)
    print_shortest_path(shortest_paths, start, end)

main()