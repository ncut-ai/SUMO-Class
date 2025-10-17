# Parking Areas

[停车场相关设置示例](experiments/parkingArea_ex)

https://sumo.dlr.de/docs/Simulation/ParkingArea.html

Areas for parking outside the road network (either road-side parking or
car parks) can be defined using the `<parkingArea>` element. This accomplishes the
following purposes:

- arbitrary parking positions and angles can be defined to visualize
  fishbone or parallel parking
- parking space outside the road network can be limited to a set
  capacity
- [automatic rerouting to an alternative parking](Rerouter.md#rerouting_to_an_alternative_parking_area) area can be triggered
  whenever a parking area becomes full

## 定义停车场的两种方式

### 直接在.net.xml文件中定义

```xml
<parkingArea id="ParkAreaA" lane="E2_0" startPos="250" endPos="300" roadsideCapacity="5" angle="45" length="30"/>
<parkingArea id="ParkAreaB" lane="-E3_0" startPos="240" endPos="460" roadsideCapacity="0" width="105" length="120" angle="30">
  <space x="-450" y="20" width="4" length="8" angle="120"/>
  <space x="-450" y="30" width="4" length="8" angle="120"/>
  <space x="-250" y="20"/>
</parkingArea>
```

The total capacity of a parking area is given by the sum of its
*roadsideCapacity* and the number of its `<space>` elements.

The parkingArea supports the following attributes:

| Attribute Name | Value Type | Value Range| Default| Description|
| ---------------- | -------------- | ---------------------------------------- | -------------------------------------- | --------------------------------------------------- |
| **id** | string | id || The name of the parking area; must be unique |
| **lane** | string | valid lane id|| The name of the lane the parking area shall be located at|
| **startPos** | float| \-lane.length < x < lane.length (negative values count backwards from the end of the lane) | 0| The begin position on the lane (the lower position on the lane) in meters|
| endPos | float| \-lane.length < x < lane.length (negative values count backwards from the end of the lane) | lane.length| The end position on the lane (the higher position on the lane) in meters, must be larger than *startPos* by more than 0.1m |
| friendlyPos| bool | *true,false* | *false*| whether invalid stop positions should be corrected automatically (default *false*) |
| name | string | simple String|| Arbitrary text to describe the parking area. This is only used for visualization purposes. |
| roadsideCapacity | int| non-negative | 0| The number of parking spaces for road-side parking |
| onRoad | bool || false| Whether vehicles remain on the road while parking.<br>**Note:**<br>If set to *true*, only roadsideCapacity is used and no `<space>`-definitions are permitted.|
| width| float| positive | 3.2| The width of the road-side parking spaces|
| length | float| positive | (endPos - startPos) / roadsideCapacity | The length of the road-side parking spaces |
| angle| float (degree) || 0| The angle of the road-side parking spaces relative to the lane angle, positive means clockwise |

## Custom parking spaces

The space element supports the following attributes:

| Attribute Name | Value Type | Value Range | Default| Description |
| -------------- | -------------- | ----------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| **x**| float| || The x-position in meters of the parking vehicle |
| **y**| float| || The y-position in meters of the parking vehicle |
| z| float| | 0| The z-position in meters of the parking vehicle |
| width| float| | width value of the parent parking area | The width of the parking space|
| length | float| | length value of the parent parking area| The length of the parking space |
| angle| float (degree) | | absolute angle of the parent parking area (lane angle + angle attribute) | Absolute angle of the parking space |
| slope| float (degree) | | 0| Slope angle of the parking space|

### 在addtional files文件中定义

Please note that parking areas must be added to a config via the *--additional-files* parameter (see {{AdditionalFile}}).

定义"parkingarea_def.add.xml":

```xml
<additional>
<!-- StoppingPlaces -->
<parkingArea id="pa_20" lane="-E0_0" startPos="100.00" endPos="180.00" roadsideCapacity="5" length="5.00" angle="120.00" departPos="200"/>
</additional>
```

在.sumocfg文件中添加:

```xml
<input>
  ......
  <additional-files value="parkingarea_def.add.xml"/>
</input>
```

## 定义停靠停车场的车辆、车流

在.flows.xml文件中（jtrrouter方式）

```xml
<vehicle id="p0" depart="0">
  <route edges="E2 -E1"/>
  <stop parkingArea="ParkAreaA" duration="120"/>
</vehicle>
<vehicle id="p1" depart="0">
  <route edges="E2 -E3"/>
  <stop parkingArea="ParkAreaB" duration="120"/>
</vehicle>
<flow id="pp0" from="E2" begin="0" end="7200" period="100">
  <stop parkingArea="ParkAreaA" duration="120"/>
</flow>
<flow id="pp1" from="E2" begin="0" end="7200" period="100">
  <stop parkingArea="ParkAreaC" duration="120"/>
</flow>
```

For a complete list of attributes for the "stop"-element of a vehicle
see
[Definition_of_Vehicles,_Vehicle_Types,_and_Routes\#Stops](../Definition_of_Vehicles,_Vehicle_Types,_and_Routes.md#stops).

## 采用jtrrouter生成rou.xml的两种方式

以“.bat”方式执行。

```bash
call="%SUMO_HOME%bin\jtrrouter" -n test.net.xml --additional-files parkingarea_def.add.xml -r test.flows.xml -t test.turns.xml -o test.rou.xml --accept-all-destinations
pause
```

或者

```bash
call="%SUMO_HOME%bin\jtrrouter" -c jtrrouter.jtrrcfg --accept-all-destinations
pause
```

".jtrrcfg"文件构造格式：

```xml
<configuration>
    <input>
        <net-file value="test.net.xml"/>
        <route-files value="test.flows.xml"/>
        <turn-ratio-files value="test.turns.xml"/>
        <additional-files value="parkingarea_def.add.xml"/>
    </input>
    <output>
        <write-license value="true"/>
        <output-file value="test.rou.xml"/>
    </output>

<!--
    <processing>
        <sink-edges value="end"/>
    </processing>
-->
    <report>
        <ignore-errors value="true"/>
        <no-step-log value="true"/>
    </report>
</configuration>
```

## 当停车场停满后需要重新计算路径 Rerouting when the current parkingArea is full

If a vehicle reaches a parkingArea that is filled to capacity it must
wait on the road until a space becomes available or [reroute to a new
parking
area](../Simulation/Rerouter.md#rerouting_to_an_alternative_parking_area).

## TraCI

Some information regarding parking areas can be accessed directly using
[traci.simulation.getParameter()
calls](../TraCI/Simulation_Value_Retrieval.md#generic_parameter_retrieval_0x7e).

- **parkingArea.capacity**: total number of parking spaces
  (roadsideCapacity + number of `<space>` elements)
- **parkingArea.occupancy**: number of vehicles parking at this
  parking area
