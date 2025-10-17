
https://sumo.dlr.de/docs/sumo-gui.html

# Changing the appearance/visualisation of the simulation

The View Settings menu allows to change and customize the simulations'
appearance and visualization. To open the visualization settings use
![Colorwheel.gif](images/Colorwheel.gif "Colorwheel") in the
menu bar at the top of the view.

For customizing the simulation one can make changes e.g. to the
background coloring, streets and vehicle appearance as well as the
visualization of POIs. Furthermore one can save
(![Save_to_registry.gif](images/Save_to_registry.gif "Save to registry")) and delete
(![Delete_from_registry.gif](images/Delete_from_registry.gif "Delete from registry")‎) settings to the registry or export
(![Save.gif](images/Save.gif "Save")) custom made settings
files and load previews settings again
![Open_sim.png](images/Open_sim.png "Open sim"). So one can
use different favorite settings files for any simulation.

The current settings file is shown in a drop down menu in the top bar of
the View Settings window where you can switch back to default settings.

## Common Visualization Settings

Separate settings exist for different simulation objects such as
vehicle, lanes, persons and detectors. Some options exist for all (or
most) of these objects:

- Size options
  - *Exaggerate by*: Draws objects bigger to make them more visible
  - *Minimum Size*: Do not draw objects below a minimum size
  - *Draw with constant size when zoomed out*: Automatically
    increase the drawing size when zooming out to keep the visual
    size constant.
- id options
  - *Show id*: Enable drawing of object IDs
  - *constant text size*: toggle whether the visual text size will stay constant when zooming
  - *Size*: Size of the drawn ID  
  - *Color*: Color of drawn ID
  - *Background*: Background color of drawn ID
  - *Show name*: Show optional name (either using the 'name' attribute or 'name' `<param>`)  
- Coloring options: Color by some attribute and change the color
value/range
  - Show color value: show the numerical value that is used for
    coloring (text configuration options as for the id)

## Vehicle Visualisation Settings

### Vehicle shape shemes

| Name          | Description                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| triangle      | All vehicles are shaped triangular                                                                                               |
| boxes         | All vehicles are shaped square                                                                                                   |
| simple shapes | All vehicles have simple car shape                                                                                               |
| raster images | All vehicles are drawn with a loaded bitmap defined for their type using attribute `imgFile` (using *simple shapes* as fallback) |

!!! note
    When using an `imgFile` as the shape, it is necessary to select the vehicles to show as "raster images" in the *View Settings* menu.

### Vehicle coloring schemes

| Name                           | Measure | Description         |
| ------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| given vehicle/type/route color | \-      | The color given within the vehicle definition with fallback to type and then to route color                                                                                                                   |
| uniform                        | \-      | All vehicles are colored uniformly                                                                                                                                                                            |
| given/assigned vehicle color   | \-      | The color given within the vehicle definition                                                                                                                                                                 |
| given/assigned type color      | \-      | The color given within the vehicle type definition                                                                                                                                                            |
| given/assigned route color     | \-      | The color given within the vehicle route definition                                                                                                                                                           |
| depart position as HSV         | \-      | The depart position of each vehicle, relative to the network center, is used to color the vehicle. Direction will be used as H(ue), distance from the center as S(aturation), V(alue) is always 1.            |
| arrival position as HSV        | \-      | The arrival position of each vehicle, relative to the network center, is used to color the vehicle. Direction will be used as H(ue), distance from the center as S(aturation), V(alue) is always 1.           |
| direction/distance as HSV      | \-      | The direction and distance between a vehicle's departure and arrival position, are used to color the vehicle. Direction will be used as H(ue), distance from the center as S(aturation), V(alue) is always 1. |
| by speed                       | m/s     | The current vehicle speed                                                                                                                                                                                     |
| by action step                 | \-      | Action in current step, next stop or otherwise
| by waiting time                | s       | The time for which a vehicle is halting                                                                                                                                                                       |
| by accumulated waiting time    | s       | The total time for which a vehicle has been halting recently (default: within the last 300s.)                                                                                                                 |
| by time since last lanechange  | s       | The time since the last lane change. The color also indicates the direction of the last lane-change (negative values indicated a change to the right).                                                        |
| by max speed                   | m/s     | Vehicle's maximum velocity                                                                                                                                                                                    |
| by CO2 emissions               | g/s     | The amount of CO2 currently emitted by the vehicle                                                                                                                                                            |
| by CO emissions                | g/s     | The amount of CO currently emitted by the vehicle                                                                                                                                                             |
| by PMx emissions               | g/s     | The amount of PMx currently emitted by the vehicle                                                                                                                                                            |
| by NOx emissions               | g/s     | The amount of NOx currently emitted by the vehicle                                                                                                                                                            |
| by HC emissions                | g/s     | The amount of HC currently emitted by the vehicle                                                                                                                                                             |
| by fuel consumption            | l/s     | The consumed fuel                                                                                                                                                                                             |
| by electricity consumption     | kWh/s   | The consumed electricity (for electric vehicles only)                                                                                                                                                         |
| by noise emissions             | dbA     | The noise produced by the vehicle                                                                                                                                                                             |
| by reroute number              | count   | The number of times this vehicle has bee rerouted                                                                                                                                                             |
| by selection                   | \-      | Colors selected and unselected vehicles differently                                                                                                                                                           |
| by offset from best lane       | count   | The number of immediate lane changes the vehicle must perform in order to follow its route                                                                                                                 |
| by acceleration                | m/s^2   | The current vehicle acceleration                                                                                                                                                                                                              |
| by time gap                    | s       | The time to collide with the leader vehicle assuming constant speeds                                                                                                                                       |
| by depart delay                | s       | The difference of actual insertion time and intended depart time                                                                                                                                       |
| by time loss                   | s       | The total time loss from driving slower than desired since departure                                                                                                                                       |
| by stop delay                  | s       | The departure delay for next (or current) public transport stop (with defined 'until' time)                                                                                                                                        |
| by stop arrival delay          | s       | The arrival delay for next (or current) public transport stop (with defined 'arrival' time)                                                                                                                                        |
| by lateral speed               | m/s     | The lateral speed of the vehicle                                                                                                                                        |
| by param (numerical)           | value   | The numerical value of the given vehicle, [device or model](TraCI/Vehicle_Value_Retrieval.md#device_and_lanechangemodel_parameter_retrieval_0x7e) parameter                                                                                                                                       |
| random                         | \-      | Random vehicle color                                                                                                                                       |
| by angle                       | \-      | Color by heading angle of the vehicle                                                                                                                                       |

### Toggles

- Show blinkers / brake lights
- Show brake gap
- Show route index: When activating *show route* in the vehicle context menu, each highlighted edge is annotated with it's index along the route (permitting to analyze looped routes)
- Show parking info: When activating *show route* in the vehicle context menu, the vehicle is annotated with the number of failed parking attempts and each parking area is annotated with the last target selection score
- Show minimum gap
- Show [Bluetooth range](Simulation/Bluetooth.md)
- Scale length with gemeotry (see [length-geometry-mismatch](Simulation/Distances.md#vehicle_lengths_in_sumo-gui)

### Scaling

Vehicle size is affected by the following features

- **Exaggerate by** : Sets a constant scaling factor
- **Draw with constant size when zoomed out**: Increases vehicle size (relative to road network) and thereby keeps them visible when zooming out
It is also possible to scale the size of the vehicle according it's attributes.
- **Scale size**: Selects scaling by a given attribute (i.e. speed). The user may configure a table of scaling factors corresponding to a list of numerical values (with automatic interpolation). This works similar to color interpolation.

### Textual annotations

The following textual annotations are supported:

- **vehicle id**: Renders the vehicle id and also 'line' attribute if defined for the vehicle
- **vehicle color value**: The numerical value that forms the basis for coloring (i.e. speed) is rendered
- **vehicle scale value**: The numerical value that forms the basis for scaling (i.e. acceleration( is rendered. It may be useful to activate scaling just for the textual value (and setting a scaling factors to 1). 
- **Vehicle text param**: Renders any [Generic Parameter](Simulation/GenericParameters.md) set on the vehicle. This also supports any [virtual parameters accessible via TraCI](TraCI/Vehicle_Value_Retrieval.md#device_and_lanechangemodel_parameter_retrieval_0x7e)


Each text can be configured with regard to it's size color and background color. By activating the option *Only for selected*, The textual annotation is limited to vehicles with the [*selected*](#selecting_objects) status.

## Edge/Lane Visualisation Settings

**Table 2.1 Lane coloring schemes**

| Name                                     | Measure | Description                                                                                   |
| ---------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| uniform                                  | \-      | All road edges are drawn using the same color. Bicycle lanes are drawn in brown, sidewalks in grey and prohibited lanes (allowing no vehicle classes) are transparent. |
| by selection (lane-/streetwise)          | \-      | selected lanes are drawn different than those that are not                                                                                                             |
| by permission code                       | \-      | all lanes are colored according to the permitted vehicle classes. The code for each lane can be retrieved from the lane parameter dialog (permission code).            |
| by allowed speed (lanewise)              | m/s     | The maximum velocity allowed on this lane                                                                                                                              |
| by current occupancy (lanewise, brutto)  | % / 100 | By the amount of place that is covered by vehicles (including minGap)                                                                                                  |
| by current occupancy (lanewise, netto)   | % / 100 | By the amount of place that is covered by vehicles (excluding minGap)                                                                                                  |
| by first vehicle waiting time (lanewise) | s       | By the time the first vehicle on the lane waits                                                                                                                        |
| by lane number (streetwise)              | \-      | By the number of lanes this edge has                                                                                                                                   |
| by CO2 emissions                         | g/s     | The mean amount of CO2 emitted per a lane's meter                                                                                                                      |
| by CO emissions                          | g/s     | The mean amount of CO emitted per a lane's meter                                                                                                                       |
| by PMx emissions                         | g/s     | The mean amount of PMx emitted per a lane's meter                                                                                                                      |
| by NOx emissions                         | g/s     | The mean amount of NOx emitted per a lane's meter                                                                                                                      |
| by HC emissions                          | g/s     | The mean amount of HC emitted per a lane's meter                                                                                                                       |
| by fuel consumption                      | l/s     | The mean amount of consumed fuel per a lane's meter                                                                                                                    |
| by electricity consumption               | kWh/s   | The mean amount of consumed electricity per a lane's meter                                                                                                             |
| by noise emission                        | dBa     | The noise generated by the vehicles on the lane                                                                                                                        |
| by global travel time                    | s       | The travel time on that edge loaded from a weight file                                                                                                                 |
| by global speed percentage               | %       | By the fraction of the maximum speed that the edge allows based on travel times from a loaded weight file                                                              |
| by given length/geometrical length       |         | The factor by which the geometrical length differs from the user-specified edge length                                                                                 |
| by angle                                 |         | The angle of the edge measured from start to end (excluding in-between geometry)                                                                                       |
| by loaded weight                         |         | By the value loaded using options **--weight-files, --weight-attribute**   |
| by priority                              |         | By the right-of-way priority using during network building                                                                                                             |
| by height at start                       | m       | By the z-coordinate at the start of the lane                                                                                                                           |
| by height at segment start               | m       | By the z-coordinate at the start of each geometry segment                                                                                                              |
| by inclination                           | %       | By the average change in height between start and end of the lane per m                                                                                                |
| by segment inclination                   | %       | By the average change in height between start and end of each geometry segment                                                                                         |
| by average speed                         | m/s     | By the average speed of vehicles on the lane                                                                                                                           |
| by average relative speed                | %       | By the average speed of vehicles on the lane as percentage of the allowed speed                                                                                        |

**Table 2.2 Lane scaling schemes**

| Name                                     | Measure | Description                                                                                               |
| ---------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| by selection (lane-/streetwise)          | \-      | selected lanes are drawn different than those that are not                                                |
| by allowed speed (lanewise)              | m/s     | The maximum velocity allowed on this lane                                                                 |
| by current occupancy (lanewise, brutto)  | % / 100 | By the amount of place that is covered by vehicles (including minGap)                                     |
| by current occupancy (lanewise, netto)   | % / 100 | By the amount of place that is covered by vehicles (excluding minGap)                                     |
| by first vehicle waiting time (lanewise) | s       | By the time the first vehicle on the lane waits                                                           |
| by lane number (streetwise)              | \-      | By the number of lanes this edge has                                                                      |
| by CO2 emissions                         | g/s     | The mean amount of CO2 emitted per a lane's meter                                                         |
| by CO emissions                          | g/s     | The mean amount of CO emitted per a lane's meter                                                          |
| by PMx emissions                         | g/s     | The mean amount of PMx emitted per a lane's meter                                                         |
| by NOx emissions                         | g/s     | The mean amount of NOx emitted per a lane's meter                                                         |
| by HC emissions                          | g/s     | The mean amount of HC emitted per a lane's meter                                                          |
| by fuel consumption                      | l/s     | The mean amount of consumed fuel per a lane's meter                                                       |
| by electricity consumption               | kWh/s   | The mean amount of consumed electricity per a lane's meter                                                |
| by noise emission                        | dBa     | The noise generated by the vehicles on the lane                                                           |
| by global travel time                    | s       | The travel time on that edge loaded from a weight file                                                    |
| by global speed percentage               | %       | By the fraction of the maximum speed that the edge allows based on travel times from a loaded weight file |
| by given length/geometrical length       |         | The factor by which the geometrical length differs from the user-specified edge length                    |
| by angle                                 |         | The angle of the edge measured from start to end (excluding in-between geometry)                          |
| by loaded weight                         |         | By the value loaded using options **--weight-files, --weight-attribute**                                  |
| by priority                              |         | By the right-of-way priority using during network building                                                |
| by average speed                         | m/s     | By the average speed of vehicles on the lane                                                              |
| by average relative speed                | %       | By the average speed of vehicles on the lane as percentage of the allowed speed                           |

In addition to the lane / edge coloring one can display lane borders,
link decals, rails, edge names, street names, internal edge names, and
hide macro connectors. The edge names as well as the street and internal
edge names will always be scaled to the chosen size, no matter which
zoom step is chosen.

## Loading Shapes and POIs

[Polygonal shapes and Points of Interests
(POIs)](Simulation/Shapes.md) can either be loaded in a
*.sumocfg* configuration file or interactively through the *Open Shapes*
option in the *File*-menu.

Shapes and POIs can be [located based on their unique
ID](#locating_objects) and their appearance can be
[customized as
well](#changing_the_appearancevisualisation_of_the_simulation).

## Showing Background Images

In addition to changing the appearance of simulated structures, one may
also load additional background images ("decals") into
**sumo-gui**. For this, open the visualization
settings using ![Colorwheel.gif](images/Colorwheel.gif "Colorwheel") and - if you are not yet here - choose the
"Background" panel (see Figure below). You will see a table with the following
columns: **file**, **centerX**, **centerY**, **width**,
**height**, **rotation**, **layer** and **relative**.

![](images/Decals_gui.png "The decals GUI")

**The decals GUI.**

Now, if you click into the first row of the "picture file" column, you
should be able to enter the complete path of an image file. Confirming
the path by pressing RETURN should force **sumo-gui**
to load and display the file below the road network, as shown in the figure:

![](images/Background_example.png "Background example")

**Example of a background image (decal).**

Currently, **sumo-gui** may load .gif, .png, .jpeg and .bmp
files. If built with gdal-support further formats such as .tif are also
usable.

Now, you may position/stretch/rotate the image using the columns
**centerX**, **centerY**, **width**, **height**, and **rotation**.

When setting the column **relative** to *1*, position and size values
will be taken as screen-relative pixel values instead of
network-relative meter values.

After aligning your decals, you can save them using the "Save Decals"
button located in the dialog. Accordingly, previously saved decals can
be loaded by pressing the "Load Decals" button.

When defining decals in XML a single line which looks like this:

```xml
<decal file="background.gif" centerX="550.00" centerY="1530.00" width="64.00" height="64.00" rotation="0.00"/>
```

The following attributes are supported

| Attribute Name | Value Type    | Description                                                                                                                     |
| -------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **file**       | path (string) | *picture file*, the full name of the background image                                                                           |
| **centerX**    | float         | *center x*, the x-position of the center of the image in network coordinates (in meters)                                        |
| **centerY**    | float         | *center y*, the y-position of the center of the image in network coordinates (in meters)                                        |
| **width**      | float         | The width of the image in network coordinates (in meters)                                                                       |
| **height**     | float         | The height of the image in network coordinates (in meters)                                                                      |
| rotation       | float         | The angle of the image in degrees                                                                                               |
| layer          | float         | The layer at which the image is drawn in meters over ground                                                                     |
| screenRelative | bool          | *relative*, whether the position and size are pixel coordinates relative to the screen rather then the network coordinates      |
| centerZ        | float         | The z-position of the center of the object in network coordinates (in meters), only used in 3D visualization instead of *layer* |
| tilt           | float         | The tilt angle of the object, only used in 3D visualization                                                                     |
| roll           | float         | The roll angle of the object, only used in 3D visualization                                                                     |

!!! note
    The contents of a decal-configuration can also be embedded in a view-settings file and thus loaded on startup. see [Configuration Files](#configuration_files)

!!! note
    When loading an image file with an embedded geo-reference (i.e. [GeoTIFF](https://en.wikipedia.org/wiki/GeoTIFF)) and the simulation network also has a geo-reference, then the image will be positioned automatically.
    
!!! note
    Background images for a network can be downloaded with the [tileGet tool](Tools/Misc.md#tilegetpy) or by using the [osmWebWizard](Tools/Import/OSM.md#osmwebwizardpy).

## Transparency

All image files in the visualization support transparency. For vehicles,
pois and polygons, this transparency can be set dynamically by changing
the color via [TraCI](TraCI.md) and setting the alpha-channel.

All objects that have their color set (via input files or visualisation
settings) support (Red,Green,Blue,Alpha) color values.

## 3D-specific Settings
The scene is illuminated by a directional light source ("the sun"). The light color originates from the grayscale range can be varied through the 3D-specific Visualization Settings. The **sun brightness** value ranges from 0 (=black) to 255 (=white) and represents the grayscale diffuse light. The ambient light value is half of the diffuse light.

The 3D scene background color can be set to any RGB color. The OSG standard background color is _(51,51,102)_.

Additionally, the visibility of traffic light related items can be set (see [automatically generated 3D environment](#automatically_generated_3d_environment)).

# Configuration Files

**sumo-gui** uses the same configuration files as
SUMO. The recognized options can be obtained by calling *sumo --help* or
you save a configuration file with default settings by calling `sumo --save-template <file> --save-commented`. 

The options in the *GUI* category are specific to sumo-gui

-  **--gui-settings-file** (shortcut **-g**) allows to load a previously saved gui-settings file (see below)
-  **-S, --start**: starts the simulation upon opening the gui (without the need to click the *start* button
-  **-Q, --quit-on-end**: closes the gui upon simulation end
-  **-d, --delay**: sets an initial simulation delay to prevent the simulation from running to quickly
- **--window-size WIDTH,HEIGHT**: sets the iniial window size (by default the previous size is restored)
- **--window-pos X,Y**: sets the initial window position (by default the previous position is restored)

A sumo configuration that loads gui settings is shown below:

*example.sumocfg*

```xml
    <configuration>
        <net-file value="yournetwork.net.xml"/>
        <gui-settings-file value="viewsettings.xml"/>
    </configuration>
```

You may either load *example.sumocfg* using the *open simulation*-dialog
or by using the command-line `sumo-gui -c example.sumocfg`.

You may use a XML schema definition file for setting up a sumo-gui
configuration:
[sumoConfiguration.xsd](https://sumo.dlr.de/xsd/sumoConfiguration.xsd).****

# GUI-settings Files

All the settings configured in the *View Settings* dialog can be saved to a file and re-used for a new simulation. We refer to such files as gui-settings files. Such a file can also include information about breakpoints, screenshots, simulation delay and background images.
The easiest way to obtain a gui-settings file is via the *View Settings*-Dialog
![Open_viewsettings_editor.gif](images/Open_viewsettings_editor.gif
"Open viewsettings editor"). Simply modify the settings and
save ![Save.gif](images/Save.gif "Save").

Note, that the gui-settings-file obtained this way only contain
information about the viewport (zoom and offset), delay, breakpoints and
decals if the corresponding check-boxes are activated before saving.


*viewsettings.xml*

```xml
    <viewsettings>
        <scheme name="..."
           ...
        </scheme>

        <viewport zoom="200" x="100" y="-100"/>
        <delay value="42"/>
        <decal file="background.gif" centerX="550.00" centerY="1530.00" width="64.00" height="64.00" rotation="0.00"/>
        <breakpoint value="42"/>
        <breakpoint value="1337"/>
    </viewsettings>
```


## Minimal settings file

It possible to reference a predefined scheme by it's name alone:

```xml
<viewsettings>
    <scheme name="real world"/>
</viewsettings>
```

The name may either be one of the "native" schemas ("standard", "real world", ...) or any schema [stored in the registry](#changing_the_appearancevisualisation_of_the_simulation) by the user.

## Breakpoints

There are multiple ways to load pre-defined [breakpoints](#breakpoints).
The breakpoint element can be included directly in a gui-settings file: `<breakpoint value="1337"/>`

Alternatively, a breakpoint-file definition can be specified in the gui-settings file:

```xml
<viewsettings>
    ...
    <breakpoints-file value="breakpoints.txt"/>
</viewsettings>
```

The breakpoints file should hold one time-value per line.
A file, suitable for loading breakpoints can be obtained by setting
breakpoints in the gui and using the menu-option for saving (Edit-\>Edit
Breakpoints-\>save). 

A further way to set breakpoints is by using the sumo option **--breakpoints** to load a comma-separated list of time values (shortcut **-B**). This circumvents the need for a gui-settings file.

## Screenshots

It is possible to take screenshots at predefined times by adding
elements to the configuration:

```xml
<viewsettings>
    <snapshot file="myScreenshot.png" time="42"/>
</viewsettings>
```

## Miscellaneous View Settings

3D Scene lighting can be defined via the following (indices 0 - 9 are supported):

```xml
<light index="0" centerX="671.02" centerY="639.20" centerZ="200"/>
```

# Multiple Views

Using the (![NewView.gif](images/NewView.gif
"New view"))-button, multiple viewing windows can be opened onto the same
simulation. The visualization settings can be set
independently for each view. The viewing windows can be managed using
the *Windows* menu in the main menu bar.

When passing multiple files to the [sumo](sumo.md)-option **--gui-settings-file**, one
viewing window is opened for each file at the start of the simulation.

# 3D Visualization

When sumo-gui was compiled with [OpenSceneGraph 
(OSG)](http://www.openscenegraph.org/) support an additional
(![NewView3D.gif](images/NewView3D.gif "New 3D view"))-button is
present to open a new 3D view. A pre-compiled Windows version for testing is available
[here](https://sumo.dlr.de/daily/sumo-win64extra-git.zip). Optionally sumo-gui will open a 3D view already from the start by 
supplying the command line option **--osg-view true**.

## 3D Viewport
The view of the 3D scene can be changed using two methods: The camera can be moved by mouse actions 
(LMB drag for translational movement, MMB drag for pitch and yaw rotation) or the view can be defined in the 
viewport dialog. Open the viewport editor using the ![Open_viewport_editor.gif](images/Open_viewport_editor.gif
"Open viewport editor") button. The camera position itself is listed in the left column wheras right "LookAt" coordinates define the 
target to look at. "LookAt" coordinates are normalized to length 1 by OSG automatically.

Interacting with network elements and vehicles works like in the 2D view: Context-dependent options are available by RMB click on the object 
to inspect.

## Automatically generated 3D environment
Only some of the regular network components have been ported to the 3D view (yet). Currently the following are displayed:

- edges (with sidewalks curbs)
- junctions
 - pedestrian crossings
- traffic lights

Automatically generated traffic lights come in different variants and can be shown/hidden independently of each other 
through the 3D part of the [GUI settings](#changing_the_appearancevisualisation_of_the_simulation):

- bubbles above the stop line which change their color according to the connection they belong to
- detailed model with pole(s) and signals (either a cantilever beam or a signal bridge for large roads; single pedestrian signals are placed across the street)

![OSGTrafficLights.png](images/OSGTrafficLights.png)

### Semi-automatic 3D traffic light
Alternatively to automatically generated traffic lights, there is the option to place a single traffic light on a pole 
at a custom position and orientation in the network. The [decals table](#showing_background_images) interprets the following 
*magic* entry in the file column to a single traffic light: `tl:<TL_ID>:<TLLINKINDEX>`. The current signal state is updated 
accordingly to the *tlLinkIndex* `<TLLINKINDEX>` of the traffic light `<TL_ID>`.

## Adding 3D objects
### Static models
Loading individual 3D objects can be done through the [decals table](#showing_background_images) of the GUI settings.
3D object files in file formats supported by OSG (e.g. obj, 3ds) are loaded in the scene and positioned with the 
offset values from the decals table. For large scenes, it may be advantageous to build a single 3D object which 
contains all elements (e.g. buildings) used in sumo-gui.

Additionally, the same background images as in the 2D view can be loaded.

### Vehicle models
Some basic vehicle models are shipped with SUMO in the `data/3D` directory. Custom vehicle models can be specified 
in the `osgFile` attribute of the respective vehicle type (see [vehicle types](Definition_of_Vehicles,_Vehicle_Types,_and_Routes.md#available_vtype_attributes)). If the custom model 
cannot be used, it is replaced by a cone shape pointing to the direction of travel.


## Limitations

!!! caution
    The 3D-Visualization is still experimental
    
- no pedestrian and cyclist models
- performance problems when simulating several vehicles
- reload leaves previous 3D scene in place


# Visualizing edge-related data

Several applications generated edge-related measures for one or more
time-intervals.

- [edgeData-output files](Simulation/Output/Lane-_or_Edge-based_Traffic_Measures.md)  
- edge-probability files generated by [randomTrips.py](Tools/Trip.md#customized_weights) with option **--weights-output-prefix**
- [marouter netload-output](marouter.md#macroscopic_outputs)
- [Smoothed traveltimes from device.rerouting](Demand/Automatic_Routing.md) when running [sumo](sumo.md) with option **--device.rerouting.output**.
- [countEdgeUsage.py](Tools/Routes.md#countedgeusagepy)
- [edgeDataFromFlow.py](Tools/Detector.md#edgedatafromflowpy) transforms detector counts into edgeData
- [routeSampler.py](Tools/Turns.md#routesamplerpy) writes achieved counts and the deficit with regard to the input counts with option **--mismatch-output**
- [netedit](Netedit/index.md#data_specific_modes) can be used to create and modify edgeData files

These files can be used with
[duarouter](Demand/Shortest_or_Optimal_Path_Routing.md#custom_edge_weights)
and with [sumo](sumo.md) to affect vehicle routing.

**sumo-gui** can also visualize the
contained data to see how various traffic measures changed over time
(without running a simulation at the same time).

## Loading Data

Edgedata files for visualization can be loaded by setting option **--edgedata-files**. 
When loaded this way, the simulation end time will be
automatically adjusted to the end of the data range.

Edgedata files can also be loaded in **sumo-gui** from
the menu using *File-\>Open EdgeData*. 

All attributes will be loaded and can be selected in the street visualization
settings

## Coloring by Data

To make use of the loaded data, street coloring must be set to **color by
edgeData** in the visualization settings dialog. 
The button *Recalibrate Rainbow* can be used to generate a
coloring scheme that spans the loaded data range for the selected attribute.

!!! note
    In the gui-settings dialog, the function 'Recalibrate Rainbow' can be used to adapt the coloring to the data range of the current attribute.
!!! note
    edgeData is time based so it will only be shown when the simulation time has advance to the begin time of the respective data interval. Make sure to advance the simulation to time 0 (step once) or to whatever begin time was used for edgeData generation before using *Recalibrate Rainbow*. To see further data frames, advance the simulation by using delay or breakpoints.

When defining a color scheme, a dedicated color for missing data ('No Data') can always be configured.

# Usage Examples

## Visualizing Shapes and Points of Interest

see [Using additional Polygons and POIs within the
Simulation](Simulation/Shapes.md)

## Display Arbitrary Text in the Simulation View
To display arbitrary text in the simulation view, the easiest way is to place a poi element with alpha channel 0 (invisible),
set it's type attribute to the text you wish to show and load gui settings that show poi types in the desired color and size.

```xml
<poi id="textPlacement0" type="my custom text" x="myX" y="myY" color="0,0,0,0"/>
```

To use another text size or color, you can use a poi parameter and pick that parameter next to the "show poi text param" checkbox:

```xml
<poi id="textPlacement2" x="myX2" y="myY2" color="0,0,0,0">
   <param key="anykey" value="my custom text in another size or color"/>
<poi>
```

The same trick can be repeated for Polygons.

You can also use `traci.simulation.writeMessage` to put custom messages into the bottom message window.

## Display a custom Logo in the simulation View
The [background images (decals)](#showing_background_images) support attribute `screenRelative` to place an object relative to the screen rather than the network. This allows to place a logo in a fixed position.

## Showing routes and route-related information

- To show the route(s) of a vehicle in the simulation, right-click and
  select *Show Current Route* or *Show all Routes*. 
  - To show only the remaining portion of the current route, select *Show Future Route*.
  - The upcoming stops and their planned timing (or trigger condition) is automatically shown along the route. To show only the next round of a cyclic route (i.e. for public transport), disable the checkbox 'show looped route'
  - Direction reversal of rail vehicles will be shown along the route with the text 'reverse' and an index.
  - To show the index of each edge along the route, the vehicle visualization option 'Show route index' can be activated
- To show the route of a person, right click and select *Show Current
  Route*. To show the trajectory on a walkingarea, select *Show
  Walkingarea Path*.
- To highlight an arbitrary set of edges in the simulation create a
  [selection file](#selecting_objects) and [color edges *by
  selection*](#edgelane_visualisation_settings)
- To Visualize all routes in a route file use the tool
  [Tools/Routes\#route2poly.py](Tools/Routes.md#route2polypy)
  or
  [Tools/Routes\#route2sel.py](Tools/Routes.md#route2selpy)
- To Visualize the number of vehicles arriving or departing at any
  edge use the tool
  [Tools/Routes\countEdgeUsage](Tools/Routes.md#countedgeusagepy)

## Investigating internal edges and lanes

[Internal Edges](Networks/SUMO_Road_Networks.md#internal_edges)
define the movements across an intersection. By default they are hidden
behind the shape of the junction to give a prettier visualization.
Occasionally it is of interest to understand which internal lane
corresponds to which movement as their IDs may be referenced in the
output or in error messages. The following visualization settings are
helpful:

- Junction settings:
  - disable *draw junction shape* (toggle with hotkey CTRL+J)
  - *show internal edge name*
  - *show internal junction name*
  - *show link junction index* (to see the correspondence between IDs and link indices)
- Edge settings:
  - *Exaggerate width by 0.1* (otherwise the shapes overlap which makes it hard to understand them)
  - *Color by selection* (coloring individual lanes makes it easier to understand geometry before and after [internal junctions](Networks/SUMO_Road_Networks.md#internal_junctions))

-----

## Investigation Stopping At Intersections

1.  Select Vehicle visualization settings "color by selection"
2.  Right-Click on a vehicle and activate "Select Foes"

The foe vehicles which cause a vehicle to stop or slow down will be
highlighted.