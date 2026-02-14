import osmnx as ox
from geopy.geocoders import Nominatim
from math import fabs

ox.settings.use_cache = True
ox.settings.log_console = False

def geocode_location(place_name):
    geolocator = Nominatim(user_agent="swiftpath")
    location = geolocator.geocode(place_name)

    if location is None:
        raise ValueError(f"Location '{place_name}' not found.")

    return (location.latitude, location.longitude)


def create_bounding_box(start_coord, end_coord):
    lat_diff = fabs(start_coord[0] - end_coord[0])
    lon_diff = fabs(start_coord[1] - end_coord[1])

    buffer_lat = lat_diff * 0.2
    buffer_lon = lon_diff * 0.2

    min_buffer = 0.02

    north = max(start_coord[0], end_coord[0]) + max(buffer_lat, min_buffer)
    south = min(start_coord[0], end_coord[0]) - max(buffer_lat, min_buffer)
    east = max(start_coord[1], end_coord[1]) + max(buffer_lon, min_buffer)
    west = min(start_coord[1], end_coord[1]) - max(buffer_lon, min_buffer)

    return north, south, east, west


city_graph_cache = {}

city_graph_cache = {}

def load_map_graph(start_place):
    import osmnx as ox
    import networkx as nx

    if "," in start_place:
        city = start_place.split(",")[-1].strip()
    else:
        city = start_place.strip()

    city_key = city.lower()

    if city_key in city_graph_cache:
        return city_graph_cache[city_key]

    print(f"Downloading road network for {city}...")

    graph = ox.graph_from_place(
        f"{city}, India",
        network_type="drive"
    )

    largest_cc = max(nx.strongly_connected_components(graph), key=len)
    graph = graph.subgraph(largest_cc).copy()

    city_graph_cache[city_key] = graph
    return graph


def get_nearest_node(graph, coord):
    return ox.distance.nearest_nodes(
        graph,
        X=coord[1],
        Y=coord[0]
    )