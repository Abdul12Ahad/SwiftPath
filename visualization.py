import folium
import os


def draw_route_map(graph, path, start_coord, end_coord):
    if not path:
        raise ValueError("Path is empty. Cannot draw route.")

    route_coords = [
        (graph.nodes[node]['y'], graph.nodes[node]['x'])
        for node in path
    ]

    route_map = folium.Map(location=start_coord, zoom_start=13)

    folium.PolyLine(
        route_coords,
        weight=6,
        opacity=0.8
    ).add_to(route_map)

    folium.Marker(
        start_coord,
        popup="Start",
        icon=folium.Icon(color="green")
    ).add_to(route_map)

    folium.Marker(
        end_coord,
        popup="Destination",
        icon=folium.Icon(color="red")
    ).add_to(route_map)

    os.makedirs("output", exist_ok=True)

    output_path = "output/route_map.html"
    route_map.save(output_path)

    print(f"Map saved to {output_path}")