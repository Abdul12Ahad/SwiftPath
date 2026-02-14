SwiftPath - Intelligent Road Routing Engine

SwiftPath is a Python-based road routing engine that computes the shortest driving path between two locations using the A* search algorithm on real-world OpenStreetMap road network data.

It demonstrates graph theory, heuristic search, and real-world map data integration in a practical routing system.

---

Features

- Real road network data from OpenStreetMap
- Custom A* algorithm implementation
- Haversine distance heuristic
- City-level routing support
- Interactive route visualization (HTML map)
- Performance measurement (execution time)
- Graph connectivity optimization
- Caching enabled for faster repeated queries

---

Technologies Used

- Python
- OSMnx
- NetworkX
- Geopy
- Folium
- OpenStreetMap Data

---

Project Architecture

SwiftPath/
│
├── main.py                # Main program e
├── map_utils.py           # Graph loading and geocoding
├── astar_algorithm.py     # A* implementation
├── heuristic.py           # Haversine distance heuristic
├── visualization.py       # Route map rendering
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

---

How It Works

1. User inputs starting and destination locations.
2. Locations are geocoded into latitude/longitude.
3. City road network is downloaded using OSMnx.
4. Graph is reduced to the largest connected component.
5. Nearest graph nodes are located.
6. A* search computes the optimal driving path.
7. Total distance is calculated.
8. Interactive route map is generated.

---

Example Input

Start: Hitech City, Hyderabad  
End: Charminar, Hyderabad  

---

Output

- Number of nodes in path
- Total distance (km)
- Execution time
- Interactive HTML map showing route
