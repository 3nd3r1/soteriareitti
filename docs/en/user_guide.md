# SoteriaReitti - Using the Application

Using the SoteriaReitti application is straightforward and intuitive. Here is a step-by-step guide on how to use the application:

## Configuring the Application

You can configure the application using the .env file. This file allows you to specify various settings, allowing you to tailor the application's behavior to your needs. Here are a few key settings:

_APP_PLACE_: This setting determines the location the application operates in. You can change this value by modifying the place name or coordinates. For example, you can set it to "Töölö, Helsinki" or other coordinates corresponding to the area where you want to test the application.

_CACHING_: This setting determines whether the network data is cached in memory or not. If this setting is `True`, the application caches the graph in memory, improving performance in subsequent launches. If the setting is `False`, the network is not cached in memory and is recalculated every time the application is launched.

Example .env file:

```
APP_PLACE=Töölö
CACHING=True
```

Please note that the .env file is sensitive, and it should not contain extra spaces or comments. Make sure that the setting names are correctly spelled, and their values correspond to your desired configurations. The application reads these settings automatically on startup, so when you modify the .env file, the application will reflect these changes on the next launch.

## Starting the Application:

First, download the latest release of the project [here](https://github.com/3nd3r1/soteriareitti/releases).

### Running from Source Code

1. Navigate to the root directory using the command

    `cd soteriareitti`

2. Before you start, make sure you have installed the application's dependencies with the command

    `poetry install`.

3. Start the application with the command

    `poetry run invoke start`.

### Running from the Zip File

**NOTE:** Currently, the zip file contains an executable for Linux only. You can create an executable file for Windows with the command `poetry run invoke build`, which will create the file in the _dist_ directory.

1. Once the download is complete, extract the downloaded zip file to your machine.
2. Start SoteriaReitti by running the _SoteriaReitti.exe_ file (Windows) or _SoteriaReitti_ file (Linux).

## Responders and Stations

Responders are mobile units that respond to emergencies, such as ambulances and police cars, capable of quickly reacting and moving from one location to another as needed.

Stations are stationary emergency responders, such as hospitals and police stations, that can receive customers brought in by responders.

### Adding a Responder or Station:

1. Add a responder or station to the map by clicking on the desired location with the **right** mouse button. Choose "Create Responder" or "Create Station" from the popup menu.
   ![Add Responder or Station](/docs/images/add_responder_1.png)

-   In the popup window, select the desired type of responder or station. For responders, you can also choose to voluntarily assign them to their own station if available. Confirm the selection, and the responder or station will now appear on the map at the selected location.
    ![Specify Type](/docs/images/add_responder_2.png)

## Emergencies

An emergency, denoted as **Emergency**, represents an active emergency situation at a specific location on the map. An emergency can be, for example, a car accident or a reported crime. When a user creates an emergency, the application attempts to find the nearest responders that can navigate to the location of the emergency. If there are no nearby units available, the emergency cannot be handled properly.

### Creating an Emergency:

1. Select the emergency location on the map by clicking with the **left** mouse button at the desired location on the map. The emergency location must be within the area specified in the .env file.

    ![Emergency Location](/docs/images/emergency_1.png)
    ![Emergency Location](/docs/images/emergency_2.png)

2. Enter the emergency details into the left menu of the application. At this stage, you can specify what type of responders are needed for the emergency and provide other essential information.

    ![Emergency Info](/docs/images/emergency_3.png)

3. Create the emergency by clicking 'Create'. The application will now display the route from the nearest responders to the emergency location.

    ![Emergency Info](/docs/images/emergency_4.png)

With these instructions, you can utilize the route planning functionalities provided by the SoteriaReitti application for managing emergencies effectively!

## Simulation

Responder movement on the map can be simulated within the application. When the simulation is running, responders return to their own station if defined or navigate to the emergency location if assigned. This simulation function is intended to give the user an idea of how the application would operate in a real emergency situation.

### How to Start the Simulation

You can start the simulation by clicking the "Simulate Responders" button in the left menu of the application.

![Simulate](/docs/images/simulate.png)

## Known Issues

-   Some random errors might cause the application to get stuck in the loading view. In such cases, restarting the application resolves the issue, and the program functions correctly again.
