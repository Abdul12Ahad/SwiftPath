import time
from heuristic import haversine
from map_utils import geocode_location, load_map_graph, get_nearest_node
from astar_algorithm import astar_search


MAX_DISTANCE_KM = 80  


def calculate_path_distance(graph, path):
    total_distance = 0

    for i in range(len(path) - 1):
        edge_data = graph.get_edge_data(path[i], path[i + 1])

        min_length = min(
            data["length"]
            for data in edge_data.values()
        )

        total_distance += min_length

    return total_distance


def main():
    try:
        start_place = input("Enter starting location: ")
        end_place = input("Enter destination: ")

        print("\nGeocoding locations...")
        start_coord = geocode_location(start_place)
        end_coord = geocode_location(end_place)

        distance_km = haversine(start_coord, end_coord)

        if distance_km > MAX_DISTANCE_KM:
            print(
                f"Error: Distance ({round(distance_km,2)} km) exceeds "
                f"{MAX_DISTANCE_KM} km stable routing limit."
            )
            return

        print("Loading road network...")
        graph = load_map_graph(start_place)

        print("Finding nearest nodes...")
        start_node = get_nearest_node(graph, start_coord)
        end_node = get_nearest_node(graph, end_coord)

        print("Running A* algorithm...")
        start_time = time.time()
        path = astar_search(graph, start_node, end_node)
        end_time = time.time()

        if path is None:
            print("No path found.")
            return

        distance = calculate_path_distance(graph, path)

        print("\nRoute found!")
        print("Number of nodes:", len(path))
        print("Total distance (km):", round(distance / 1000, 2))
        print("Execution Time:", round(end_time - start_time, 4), "seconds")

        from visualization import draw_route_map
        draw_route_map(graph, path, start_coord, end_coord)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
