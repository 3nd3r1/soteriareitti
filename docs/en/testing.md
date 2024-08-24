# SoteriaReitti - Testing Documentation

The application has been thoroughly tested with automated performance and unit tests, as well as manual system and user interface tests. This has ensured the stability and error-free operation of the SoteriaReitti application in various situations and environments.

Updated on 28.10.2023

## Unit Tests

[![Coverage Report](/docs/images/coverage.svg "Coverage Badge")](https://htmlpreview.github.io/?https://github.com/3nd3r1/soteriareitti/blob/main/docs/coverage/index.html)
(The badge is clickable.)

The unit testing coverage report includes tests for individual components of the SoteriaReitti application, such as _Emergency_ and _Responders_. The tests cover all critical functions, including emergency routing, station and responder management, and the functionality of individual data structures.

The tests were conducted using Python's unittest library, which enabled the writing of automated tests for each component. Each component was tested separately to ensure that every aspect functions correctly and as expected.

Unit tests can be run as follows:

1. Navigate to the project root.
2. Install the project dependencies using the command:
   `poetry install`
3. Run the tests using the command:
   `poetry run invoke test`

### App

The functionality of the _SoteriaReitti_ class, the main class of the application, has been tested using the _TestSoteriaReitti_ class. This class tests that all the smaller components of the application work together correctly at the main class level.

### Map

The functionality of the _Map_ class has been thoroughly tested using the _TestMap_ class. The test results cover various aspects, such as creating the graph and loading it from cache. The _TestMap_ class not only checks the basic functions of the _Map_ class but also tests the functionality of the _MapPoint_ class. Specifically, it ensures that _MapPoint_ finds the correct routes using both Dijkstra and IDA* algorithms. This testing process is essential to ensure that map creation, loading, and routing work as intended in different scenarios.

### Emergency

The functionality of the _Emergency_ class has been thoroughly tested using the _TestEmergency_ class. These tests cover the management of emergencies, route calculation, and the selection of the appropriate responder. The tests ensure that emergency routing and the selection of the nearest responder function correctly.

### Station

The functionality of the _Station_ class (such as hospitals and fire stations) has been tested using the _TestStation_ class. The tests ensure that stations can be added to the map.

### Responder

The functionality of the _Responder_ class (such as ambulances and police cars) has been tested using the _TestResponder_ class. The tests ensure that responders can be correctly added to the map.

### Geo

The functionality of the _geo_ module has been thoroughly tested using the _TestGeo_ class. The test cases cover all geographical calculations, such as calculating distances between map points and converting locations from different coordinate formats. Additionally, the tests ensure that all data structures in the geo module, such as Location and Distance, function correctly.

### Graph

The functionality of the _graph_ module has been tested using the _TestGraph_ class. The test cases ensure that all graph-related functions and data structures, such as the _Graph_ class and the _get_largest_component_ method, work correctly and efficiently. The tests ensure that the graph module accurately meets our needs.

### Algorithms

The functionality of the _IDA*_ and _Dijkstra_ algorithms has been tested by comparing their results to known shorter paths in a simple network. The unit tests also ensure that the algorithms produce results in the correct format.

### Simulators

The functionality of the _ResponderSimulator_ class has been tested using the _TestSimulation_ class. The tests ensure that the simulation of responders works correctly.

## Performance Testing

The purpose of performance testing is to assess the performance of the IDA* and Dijkstra algorithms in networks of different sizes.
Performance testing also allows for comparing the performance of the two algorithms.

Performance testing is conducted as follows:

1. Network Creation: First, create a map in the specified location, which will serve as the test environment.

2. Random Nodes: Randomly select two nodes from the network, representing the start and end points of the route.

3. Route Calculation: Both IDA* and Dijkstra algorithms calculate the shortest route between these two nodes.

4. Comparison and Analysis: The performance of the two algorithms is compared, and the results are analyzed.

Performance testing is conducted in three different locations:

-   Sipoo (37,690 nodes)
-   Kirkkonummi (65,489 nodes)
-   Espoo (131,369 nodes)
-   Helsinki (146,464 nodes)

### Performance Testing Execution

1. Navigate to the project root.
2. Install the project dependencies using the command: `poetry install`
3. Run the tests using the command: `poetry run invoke benchmark`

### Conclusions

#### Performance Testing in Helsinki

![Benchmark Lines](/docs/images/benchmark-result.png)

-   IDA* -> <font color="#FFAB40">Yellow</font>
-   Dijkstra -> <font color="#999999">Gray</font>

The results indicate that the IDA* and Dijkstra algorithms are approximately equally fast on small routes that take about 9 minutes or less. However, when the route duration exceeds 9 minutes, IDA* begins to require significantly more time compared to Dijkstra. Dijkstra's runtime remains relatively constant even on larger routes, while IDA*'s runtime increases rapidly with the length of larger routes.

## System Testing

In system testing, the application has been tested as a whole to ensure that all classes and their interactions function correctly.

## User Interface Testing

In manual user interface tests, it has been ensured that the user interface responds correctly to various user interactions. The test cases cover various scenarios, such as adding emergencies, selecting responders, and displaying routes in the user interface.

## Remaining Issues and Improvement Suggestions

The application has been extensively tested, but certain edge cases or atypical behavior scenarios may still present unexpected issues. One potential area for improvement is to add a broader range of manual user interface tests, particularly scenarios testing user interactions.

Additionally, it may be worth considering the addition of automated integration tests to avoid potential integration issues between different components.

The tests and coverage mentioned in this testing document are up to date at this moment, and further testing will be conducted with each new version and update of the application.
