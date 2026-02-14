from map_utils import geocode_location, load_map_graph, get_nearest_node

place = "Delhi"
coord = geocode_location(place)
print("Coordinates:", coord)

graph = load_map_graph(coord)
print("Graph loaded.")

node = get_nearest_node(graph, coord)
print("Nearest node:", node)
