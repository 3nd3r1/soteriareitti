# Implementation Document

## General Structure of the Program

The SoteriaReitti application is designed to be modular and clear, enabling the efficient operation of different components together. The application consists of several main components, such as Emergency, Responders, Station, Graph, and Geo. Each component is responsible for a specific aspect.

### Class Diagram Illustrating the Structure of the Program

![Class Diagram](/docs/images/classdiagram-dark.png#gh-dark-mode-only)
![Class Diagram](/docs/images/classdiagram-light.png#gh-light-mode-only)

-   **SoteriaReitti**: This main class manages the entire application. It includes all Responders, Stations, and Emergencies, which are key actors in managing emergency situations.

-   **Ui Module**: This module is responsible for the user interface of the SoteriaReitti program. It currently uses a Tkinter-based Gui class that allows the application to run in a graphical user interface.

-   **Responder Class**: This class represents response units such as police cars and ambulances. Response units can move on the map and respond to emergencies. Each response unit can have one station.

-   **Station Class**: This class represents stations such as hospitals and police stations, where response units return or depart from.

-   **Emergency Class**: This class represents individual emergency cases. Each emergency can have up to three Responders responding to the situation.

-   **Map Class**: This class represents the map and manages all location data and routing between emergency locations.

-   **Helper Classes**: Additionally, the application includes other helper classes, such as the Geo module related to navigation, the Graph module handling network data structures, and the Algorithms module containing the algorithms used, such as IDA* and Dijkstra. These classes enable the application to have versatile functionality and efficient performance in managing emergency situations.

**Corrections in the Class Diagram:**

-   The _App_ class can contain multiple _Emergency_ class instances.
-   The _Emergency_ class does not contain _Station_ class instances.
-   The _Responder_ class can contain one _Station_ class instance.

### Use of Algorithms

In the current implementation of the application, when a new station (Station) is created, the application uses Dijkstra's algorithm to find all routes from the station to every point on the map. This enables very fast retrieval of the shortest route directly from memory.

The shortest routes for response units, such as ambulances or police cars, to emergencies are determined using the IDA* algorithm. This choice is made because response units can move freely on the map, making static memory usage impractical. The flexibility of the IDA* algorithm allows for dynamic route calculation without the need for long-term memory storage. This way, the application can provide an efficient and flexible routing service for responding to various emergency situations.

## Achieved Time and Space Complexities

### Dijkstra Analysis

The time complexity of Dijkstra's algorithm is $O((V + E) * log(V))$, where $V$ is the number of nodes and $E$ is the number of edges in the network. The algorithm uses a min-heap to organize nodes and performs updates for each node. The time complexity depends on the data structure used and is generally efficient in large networks, but it does not handle negative edges without special measures.

### IDA* Analysis

The time complexity of the IDA* algorithm depends on the heuristic and the network used. The algorithm uses depth-first search, where in each iteration, it searches for routes with a weight below a certain "threshold." The time complexity varies based on the threshold and heuristic used. If the heuristic is admissible (i.e., it does not overestimate costs), IDA* will find the optimal route.

In general, the time complexity of the IDA* algorithm is difficult to precisely determine because it depends on the heuristic and network used. However, in large and complex networks, the IDA* algorithm can be slow because it may need to explore a large number of states before finding the optimal solution. The algorithm's efficiency largely depends on the quality of the heuristic function and how well it estimates distances from the final goal state. To improve efficiency, better search space pruning strategies and optimization techniques could be considered in the use of the IDA* algorithm.

In developing my program, I have employed several strategies to enhance the performance of the IDA* algorithm. For example, I have implemented a delta parameter that defines the allowable error level that the IDA* search can produce. During each iteration, the threshold value must increase by at least the delta unit, allowing for a slightly inaccurate but significantly faster result. This trade-off between accuracy and performance has proven effective in optimizing the execution time of the IDA* algorithm, especially in large and complex networks.

### Comparison

The IDA* algorithm shows its efficiency particularly in small networks, where its heuristic-based next-node selection occurs effectively. In small networks, the IDA* algorithm performs well and finds the optimal route.

On the other hand, in large networks, the Dijkstra algorithm is often a faster option in this project. Dijkstra's algorithm offers more efficient performance for large network areas.

Although the IDA* algorithm is not always the fastest, it uses less memory. This feature is particularly significant for responders who can move around the map and require continuous route finding. Lower memory usage makes the IDA* algorithm a useful option in situations where memory is limited.

## Potential Shortcomings and Improvement Suggestions

-   The user interface could be improved by providing the user with more visual information, such as showing routes animated on the map. This could have been implemented as a web-based JavaScript application.
-   The functionality of the application could be separated into its own component, which could be handled through a REST API.
-   It was noted during the demo session that in most cases, the A* algorithm would be more efficient than Dijkstra and IDA*. Therefore, it might be reasonable to implement the application solely using the A* algorithm.

## Use of Large Language Models

The majority of the project was completed without using large language models. However, I utilized ChatGPT to explain scientific articles, particularly in researching the IDA* algorithm. I summarized the content of the articles to ChatGPT and asked for a concise summary.

Additionally, I used ChatGPT a few times to correct writing errors.

## References

The following sources were utilized in the development of the application:

-   Official Python Documentation: [python.org](https://python.org)
-   Tkinter Documentation: [tkdocs.com](https://tkdocs.com)
-   CustomTkinter Documentation: [customtkinter.com](https://customtkinter.tomschimansky.com/)
-   OSM Wiki: [wiki.openstreetmap.org](https://wiki.openstreetmap.org/)
-   Overpy Docs: [readthedocs.io](https://python-overpy.readthedocs.io/en/latest/)

-   IDA* Wikipedia: [wikipedia.com](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
-   Real-time Vehicle Routing and Scheduling in Dynamic and Stochastic Traffic Networks: [scholar.google.com](https://scholar.google.com/scholar?q=Fu%20L.%20Real-time%20vehicle%20routing%20and%20scheduling%20in%20dynamic%20and%20stochastic%20traffic%20networks.%20Unpublished%20Ph.D.%20Dissertation,%20University%20of%20Alberta,%20Edmonton,%20Alberta,%201996)
