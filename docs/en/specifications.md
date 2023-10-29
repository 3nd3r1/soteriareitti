# SoteriaReitti - Project Specifications

SoteriaReitti is a Python-based application designed for emergency dispatchers. The application assists them in finding the best routes during emergencies and on congested roads. SoteriaReitti originates from Greek and translates to "path of salvation," reflecting the core goal of the project: to provide a saving route for those in need.

## Programming Language and Other Languages

### Programming Language:

The SoteriaReitti project will primarily be implemented in the Python programming language. Python offers a versatile range of libraries and tools for data processing, building network structures, and route planning, making it an ideal choice for this project.

In the initial phase, the focus will be on command-line functionality, and later, a Tkinter-based or Django-based graphical user interface (GUI) will be implemented.

If a Tkinter-based GUI is used, [TkinterMapView](https://github.com/TomSchimansky/TkinterMapView) can be employed.

### Languages:

The project will primarily focus on the Finnish language for documentation. Code and related names such as variables and functions will mostly be written in English. Code comments will also be written in English to ensure good collaboration and clear communication throughout different phases of the project.

## Algorithms and Data Structures

### Algorithms

The main route planning algorithms used will be Dijkstra's algorithm and IDA* (Iterative Deepening A*). The selection of these two algorithms is based on the following rationale:

-   **Dijkstra's Algorithm**: Dijkstra's algorithm is a widely used shortest path algorithm that operates in a weighted graph. This algorithm is particularly suitable for situations requiring precise and optimal route finding. Dijkstra's algorithm can calculate the shortest route to all possible destinations from the starting point. [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

-   **IDA* (Iterative Deepening A*)**: IDA* is an efficient algorithm that finds the shortest route from the starting point to the destination, iteratively using less memory than the traditional A* algorithm. IDA* is a good choice when quick real-time route searches are needed, and memory usage is limited. [Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_A*)

### Data Structures

The SoteriaReitti application utilizes heap data structures and various network structures based on traffic information and route planning. Heap structures are a key part of the functioning of Dijkstra's algorithm, while network structures aid in efficient route planning.

## Time and Space Complexities:

The time complexity of Dijkstra's algorithm depends on the size and structure of the network but can be either $O(V^2)$ or $O(E + V \cdot log(V))$, where $V$ is the number of nodes and $E$ is the number of edges in the network.

The IDA* algorithm is based on the A* algorithm, and its time complexity depends on the quality of the heuristic, and space complexity depends on the depth of recursive calls. Typically, IDA* has a better space complexity than A*, but it can be slower as it iteratively performs the same work multiple times.

Additionally, reading OpenStreetMap (OSM) data will take some time and memory.

## Inputs:

The SoteriaReitti application has several inputs that help define emergency parameters and route search parameters. The inputs include the following information:

-   Emergency Location: The user provides the location of the emergency, either as coordinates or an address. This is the starting point from which route planning begins.

-   Emergency Type: The user specifies the type of emergency, for example, heart attack, accident, fire, etc. Each emergency type can have different route search parameters.

-   <del>Route Optimization: The user can choose the desired route optimization algorithm (such as Dijkstra, IDA\*). Each algorithm may yield different results and parameters.</del>

The application takes these inputs into account and uses them to initiate route planning. The nature of the emergency and the type of emergency vehicle impact how the route is optimized. The application's task is to find the fastest and most efficient route to the emergency location as well as from the emergency location, for example, to the hospital if it's an ambulance. The goal is to provide a rapid and smooth route guide for emergency healthcare personnel, enabling them to arrive at the destination quickly and safely.

### External Data

In the early stages of the SoteriaReitti application development, the focus will be on the city of Helsinki, utilizing services and data sources specifically available in Helsinki. This allows efficient route planning and optimization for emergencies in the Helsinki area. Here are some key external data sources:

-   Traffic Data Source: The application receives real-time traffic data from various route segments. This data can come from different traffic authorities or service providers, such as city traffic information services or traffic data-providing companies. For instance, [City of Helsinki](https://hri.fi/data/fi/dataset/liikennemaarat-helsingissa) may provide its traffic data through an open data API.

-   Map Data Source: Map data is an essential part of route planning. The application can use map data from open map data sources like [OpenStreetMap](https://www.openstreetmap.org) (OSM). OSM provides a vast database of map data, including street locations, traffic signs, and geographical features.

-   Route Data and Address Information: To obtain information about route segments and addresses, the application can utilize public APIs providing route data, such as [Nominatim](https://nominatim.openstreetmap.org/ui/search.html). This data can be used for route planning and address identification.

-   Emergency Service Information: Information about various emergency services, such as hospitals, fire stations, and police stations, can be obtained directly from official emergency service organizations. The application can utilize this information to provide routes to these critical destinations during emergencies. Additionally, considering real-time tracking of emergency vehicles' locations might be explored in the future. In the initial stages, most data will be manually inputted until automated data collection systems can be integrated into the application.

These external data sources and APIs are crucial for the functioning of the SoteriaReitti application, enabling real-time and precise route optimization considering traffic data, map data, and essential destinations.

## Miscellaneous

-   **Degree Program:** Bachelor of Science in Computer Science (BSc)
-   **Other programming languages I am proficient in:** Javascript, Python
