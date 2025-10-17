# 发车、跟驰、换道

相关定义：[SUMO中的车辆类型跟驰换道模型设置.md](../SUMO中的车辆类型跟驰换道模型设置.md)

## 1. 发车

### 1.1 车辆属性表

A vehicle may be defined using the following attributes:

| Attribute Name  | Value Type | Description  |
| --------------- | ----------------------------------------------------------------------------- | -------------------------------------- |
| **id** | id (string)| The name of the vehicle   |
| type   | id| The id of the [vehicle type](#vehicle_types) to use for this vehicle.   |
| route  | id| The id of the route the vehicle shall drive along  |
| color  | [color](#colors)   | This vehicle's color|
| **depart**  | float (s) or [human-readable-time](Other/Glossary.md#t) or one of *triggered*, *containerTriggered*   | The time step at which the vehicle shall enter the network; see [\#depart](#depart). Alternatively the vehicle departs once a [person enters](Specification/Persons.md#rides) or a [container is loaded](Specification/Containers.md) |
| **departLane**  | int/string (≥0, "random", "free", "allowed", "best", "first")| The lane on which the vehicle shall be inserted; see [\#departLane](#departlane). *default: "first"*|
| departPos| float(m)/string ("random", "free", "random_free", "base", "last", "stop")   | The position at which the vehicle shall enter the net; see [\#departPos](#departpos). *default: "base"* |
| departSpeed | float(m/s)/string (≥0, "random", "max", "desired", "speedLimit", "last", "avg") | The speed with which the vehicle shall enter the network; see [\#departSpeed](#departspeed). *default: 0* |
| departEdge | int (index from \[0, routeLength\[ or "random"| The initial edge along the route where the vehicle should enter the network (only supported if a complete route is defined); see [\#departEdge](#departEdge). *default: 0* |
| arrivalLane | int/string (≥0,"current") | The lane at which the vehicle shall leave the network; see [\#arrivalLane](#arrivallane). *default: "current"*   |
| arrivalPos  | float(m)/string (≥0<sup>(1)</sup>, "random", "max") | The position at which the vehicle shall leave the network; see [\#arrivalPos](#arrivalpos). *default: "max"* |
| arrivalSpeed| float(m/s)/string (≥0,"current")| The speed with which the vehicle shall leave the network; see [\#arrivalSpeed](#arrivalspeed). *default: "current"*  |
| arrivalEdge | int (index from \[0, routeLength\[ or "random"| The final edge along the route where the vehicle should leave the network (only supported if a complete route is defined); see [\#arrivalEdge](#arrivalEdge).   |
| line   | string | A string specifying the id of a public transport line which can be used when specifying [person rides](Specification/Persons.md#rides)|
| personNumber| int (in \[0,personCapacity\]) | The number of occupied seats when the vehicle is inserted. *default: 0*   |
| containerNumber | int (in \[0,containerCapacity\])| The number of occupied container places when the vehicle is inserted. *default: 0* |
| reroute| bool| Whether the vehicle should be equipped with a [rerouting device](Demand/Automatic_Routing.md) (setting this to *false* does not take precedence over other assignment options) |
| via| id list| List of intermediate edges that shall be passed on [rerouting](Simulation/Routing.md#features_that_cause_rerouting) <br><br>**Note:** when via is not set, any `<stop>`-elements that belong to this route will automatically be used as intermediate edges. Otherwise via takes precedence.|
| departPosLat| float(m)/string ("random", "free", "random_free", "left", "right", "center") | The lateral position on the departure lane at which the vehicle shall enter the net; see [Simulation/SublaneModel](Simulation/SublaneModel.md). *default: "center"*  |
| arrivalPosLat   | float(m)/string ("default", "left", "right", "center")| The lateral position on the arrival lane at which the vehicle shall arrive; see [Simulation/SublaneModel](Simulation/SublaneModel.md). by default the vehicle does not care about lateral arrival position |
| speedFactor   | float > 0| Sets custom speedFactor (factor on road speed limit) and overrides the [speedFactor distribution](#speed_distributions) of the vehicle type |
| insertionChecks  | string list  |  Sets the list of safety checks to perform during vehicle insertion. Possible values are: `all`, `none`, `collision`, `leaderGap`, `followerGap`, `junction`, `stop`, `arrivalSpeed`, `oncomingTrain`, `speedLimit`, `pedestrians`. default *all* |

### 1.2 flows定义（repeated vehicles）

| Attribute Name | Value Type | Description  |
| -------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| begin | float (s) or [human-readable-time](Other/Glossary.md#t) or one of *triggered*, *containerTriggered* | first vehicle departure time |
| end   | float(s)| end of departure interval (if undefined, defaults to 24 hours) |
| vehsPerHour| float(\#/h)| number of vehicles per hour, equally spaced (not together with period or probability)  |
| period| float(s) or "exp(X)" where x is float  | if float is given, insert equally spaced vehicles at that period. If exp(X) is given, insert vehicles with exponentially distributed time gaps. This turns insertion into a [Poisson process](https://en.wikipedia.org/wiki/Poisson_point_process) with an expected value of *X* insertions per second. (not together with vehsPerHour or probability), see also [Simulation/Randomness](Simulation/Randomness.md#flows_with_a_random_number_of_vehicles)  |
| probability| float(\[0,1\]) | probability for emitting a vehicle each second (not together with vehsPerHour or period), see also [Simulation/Randomness](Simulation/Randomness.md#flows_with_a_random_number_of_vehicles) |
| number| int(\#) | total number of vehicles, equally spaced|

- **发车的几种示例**
```xml
<flow id="f1" begin="0" end="3600" from="E0" number="1000">
<flow id="f2" begin="0" end="3600" from="E0" vehsPerHour="1000">
<flow id="f3" begin="0" end="3600" from="E0" period="10">
<flow id="f4" begin="0" end="3600" from="E0" period="exp(2.0)">
<flow id="f5" begin="0" end="3600" from="E0" probability="0.1">
```

- **构造[.flows.xml（period=float方式）](2.sumo.period_float/test.flows.xml)**

```xml
<routes>
    <vType id="t01" vClass="passenger" probability="0.9"/>
    <vType id="t02" vClass="truck" probability="0.1"/>
    <vTypeDistribution id="typedist1" vTypes="t01 t02"/>
<interval begin="0" end="3600">
  <flow id="0" from="E1" begin="0" end="3600" departLane="best" period="5" type="typedist1"/>
  <flow id="1" from="E3" begin="0" end="3600" departLane="best" period="5" type="typedist1"/>
  <flow id="2" from="E2" begin="0" end="3600" departLane="best" period="5" type="typedist1"/>
  <flow id="3" from="E0" begin="0" end="3600" departLane="best" period="5" type="typedist1"/>
  </interval>
</routes>
```

- **构造[.flows.xml（period=exp(X)方式）](2.sumo.period_exp()/test.flows.xml)**

```xml
<routes>
    <vType id="t01" vClass="passenger" probability="0.9"/>
    <vType id="t02" vClass="truck" probability="0.1"/>
    <vTypeDistribution id="typedist1" vTypes="t01 t02"/>
<interval begin="0" end="3600">
  <flow id="0" from="E1" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  <flow id="1" from="E3" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  <flow id="2" from="E2" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  <flow id="3" from="E0" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  </interval>
</routes>
```

| Attribute Name  | Value Type | Description|
| --------------- | ----------------------------------------------------------------------------- | -------------------------------------- |
| departLane  | int/string (≥0, "random", "free", "allowed", "best", "first") | The lane on which the vehicle shall be inserted; see [\#departLane](#departlane). *default: "first"* |
| period| float(s) or "exp(X)" where x is float  | if float is given, insert equally spaced vehicles at that period. If exp(X) is given, insert vehicles with exponentially distributed time gaps. This turns insertion into a [Poisson process](https://en.wikipedia.org/wiki/Poisson_point_process) with an expected value of *X* insertions per second. (not together with vehsPerHour or probability), see also [Simulation/Randomness](Simulation/Randomness.md#flows_with_a_random_number_of_vehicles)  |

## 2. 跟驰


```xml
<routes>
  <vType id="t01" vClass="passenger" carFollowModel="EIDM" probability="0.9" accel="2.6" decel="4.5" sigma="0.5"/>
  <vType id="t02" vClass="truck" carFollowModel="EIDM" probability="0.1" accel="2.6" decel="4.5" sigma="0.5"/>
  <vTypeDistribution id="typedist1" vTypes="t01 t02"/>
  <interval begin="0" end="3600">
    <flow id="0" from="E1" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="1" from="E3" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="2" from="E2" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="3" from="E0" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  </interval>
</routes>
```

### 2.1 跟驰模型 Car-Following Models

The car-following models currently implemented in SUMO are given in the
following table.

| Element Name *(deprecated)* | Attribute Value *(when declaring as attribute)* | Description |
| --------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| carFollowing-Krauss  | Krauss| The Krauß-model with some modifications which is the default model used in SUMO|
| carFollowing-KraussOrig1| KraussOrig1  | The original Krauß-model  |
| carFollowing-PWagner2009| PWagner2009  | A model by Peter Wagner, using Todosiev's action points   |
| carFollowing-BKerner | BKerner| A model by Boris Kerner<br><br>**Caution:** currently under work |
| carFollowing-IDM| IDM   | The Intelligent Driver Model by Martin Treiber<br><br>**Caution:** Default parameters result in very conservative lane changing gap acceptance |
| carFollowing-IDMM| IDMM  | Variant of IDMM<br><br>**Caution:** lacking documentation |
| carFollowing-EIDM| EIDM  | [Extended Intelligent Driver Model for subsecond simulation by Dominik Salles](Car-Following-Models/EIDM.md)   |
| carFollowing-KraussPS| KraussPS| the default Krauss model with consideration of road slope |
| carFollowing-KraussAB| KraussAB| the default Krauss model with bounded acceleration (only relevant when using PHEM classes)   |
| carFollowing-SmartSK | SmartSK| Variant of the default Krauss model<br><br>**Caution:** lacking documentation  |
| carFollowing-Wiedemann| Wiedemann| Car following model by Wiedemann (2-Parameters)|
| carFollowing-W99| W99   | Car following model by Wiedemann, [10-Parameter version](http://w99demo.com/)  |
| carFollowing-Daniel1 | Daniel1| Car following model by Daniel Krajzewicz<br><br>**Caution:** lacking documentation|
| carFollowing-ACC| ACC   | [Car following model by Milanés V. and Shladover S.E.](Car-Following-Models/ACC.md)  |
| carFollowing-CACC| CACC  | [Car following model by Milanés V. and Shladover S.E.](Car-Following-Models/CACC.md) |
| carFollowing-Rail| Rail  | [Model for various train types](Simulation/Railways.md#modelling_trains)|

### 2.2 相关参数 Car-Following Model Parameters

Mostly, each model uses its own set of parameters. The following table
lists which parameter are used by which model(s). [Details on car-following models and their parameters can be found here](Car-Following-Models.md).

| Attribute| Default| Range| Description| Models  |
| ---------------------------- | ----------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| minGap  | [vClass-specific](Vehicle_Type_Parameter_Defaults.md) | >= 0| Minimum Gap when standing (m)| all models|
| accel   | [vClass-specific](Vehicle_Type_Parameter_Defaults.md) | >= 0| The acceleration ability of vehicles of this type (in m/s^2) | all models |
| decel   | [vClass-specific](Vehicle_Type_Parameter_Defaults.md) | >= 0| The deceleration ability of vehicles of this type (in m/s^2) | all models |
| emergencyDecel | [vClass-specific](Vehicle_Type_Parameter_Defaults.md) | >= decel | The maximum deceleration ability of vehicles of this type in case of emergency (in m/s^2)| all models except "Daniel1" |
| startupDelay   | 0 | >=0  | The extra delay time before starting to drive after having had to stop| all models except "Daniel1" |
| sigma   | 0.5  | [0,1]| The driver imperfection (0 denotes perfect driving)   | Krauss, SKOrig, PW2009 |
| sigmaStep| step-length | > 0| The frequence for updating the acceleration associated with driver imperfection. If set to a constant value (i.e *1*), this decouples the driving imperfection from the simulation step-length   | Krauss, SKOrig, PW2009 |
| tau| 1| >= 0| The driver's desired (minimum) time headway. Exact interpretation varies by model. For the default model *Krauss* this is based on the net space between leader back and follower front). For limitations, see [Car-Following-Models\#tau](Car-Following-Models.md#tau)). | all models|
| k||   || Kerner|
| phi||   || Kerner|
| delta   | 4|   | acceleration exponent| IDM, EIDM |
| stepping| 0.25 | >= 0| the internal step length (in s) when computing follow speed| IDM, EIDM |
| adaptFactor| 1.8  | >= 0| the factor for taking into account past level of service| IDMM| 
| adaptTime| 600  | >= 0| the time interval (in s) for relaxing past level of service| IDMM|
| security||   | desire for security| Wiedemann |
| estimation||   | accuracy of situation estimation| Wiedemann |
| speedControlGain| -0.4 |   | The control gain determining the rate of speed deviation (Speed control mode) | ACC|
| gapClosingControlGainSpeed   | 0.8  |   | The control gain determining the rate of speed deviation (Gap closing control mode)  | ACC|
| gapClosingControlGainSpace   | 0.04 |   | The control gain determining the rate of positioning deviation (Gap closing control mode)   | ACC|
| gapControlGainSpeed   | 0.07 |   | The control gain determining the rate of speed deviation (Gap control mode)   | ACC|
| gapControlGainSpace   | 0.23 |   | The control gain determining the rate of positioning deviation (Gap control mode)| ACC|
| collisionAvoidanceGainSpace  | 0.8  |   | The control gain determining the rate of positioning deviation (Collision avoidance mode)   | ACC|
| collisionAvoidanceGainSpeed  | 0.23 |   | The control gain determining the rate of speed deviation (Collision avoidance mode)  | ACC|
| collisionAvoidanceOverride  | 2|   | If the ACC followSpeed is higher than the Krauss-followSpeed by the given value X, limit the speed to Krauss-speed + X to avoid collision   | ACC, CACC  |
| speedControlGainCACC  | -0.4 |   | The control gain determining the rate of speed deviation (Speed control mode) | CACC|
| gapClosingControlGainGap| 0.005|   | The control gain determining the rate of positioning deviation (Gap closing control mode)   | CACC|
| gapClosingControlGainGapDot  | 0.05 |   | The control gain determining the rate of the positioning deviation derivative (Gap closing control mode)  | CACC|
| gapControlGainGap| 0.45 |   | The control gain determining the rate of positioning deviation (Gap control mode)| CACC|
| gapControlGainGapDot  | 0.0125|   | The control gain determining the rate of the positioning deviation derivative (Gap control mode)   | CACC|
| collisionAvoidanceGainGap| 0.45 |   | The control gain determining the rate of positioning deviation (Collision avoidance mode)   | CACC|
| collisionAvoidanceGainGapDot | 0.05 |   | The control gain determining the rate of the positioning deviation derivative (Collision avoidance mode)  | CACC|
| cc1||   | Spacing Time - s  | W99|
| cc2||   | Following Variation - m  | W99|
| cc3||   | Threshold for Entering "Following" - s | W99|
| cc4||   | Negative "Following" Threshold - m/s   | W99|
| cc5||   | Positive "Following" Threshold - m/s   | W99|
| cc6||   | Speed Dependency of Oscillation - 10^-4 rad/s | W99|
| cc7||   | Oscillation Acceleration - m/s^2| W99|
| cc8||   | Standstill Acceleration - m/s^2 | W99|
| cc9||   | Acceleration at 80km/h - m/s^2  | W99|
| trainType||   | [string id for pre-defined train type](Simulation/Railways.md#modelling_trains)| Rail|
| tpreview| 4.00 | >= 1| The look ahead time headway for the desired speed. Lower values result in late and hard braking when turning at junctions or when speed limits change (s)| EIDM|
| tPersDrive| 3.00 | >= 1| Correlation time of the Wiener Process for the driving error (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (s)| EIDM|
| tPersEstimate  | 10.00| >= 1| Correlation time of the Wiener Process for the estimation errors (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (s) | EIDM|
| treaction| 0.50 | >= 0| The interval length for which CF-model performs its decision logic (acceleration only). Works similiar to the [actionStepLength](Car-Following-Models.md#actionsteplength) attribute, but here it can be seen as a maximal value. The driver will react faster in critical situations. ActionStepLength/Driverstate should not be used together with this model [Reference](https://doi.org/10.1016/j.trpro.2017.05.011) (s)  | EIDM|
| ccoolness| 0.99 | [0,1]| Coolness Parameter, the driver takes the acceleration of the leading vehicle into account. How cool the driver reacts to lane changes, which reduce the gap to the next leading vehicle. 0 means that this term is not used at all. (originally from [Enhanced Intelligent Driver Model](https://doi.org/10.1098/rsta.2010.0084) (-)  | EIDM|
| sigmaleader| 0.02 | [0,1]| Estimation error magnitude of the leading vehicle's speed (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (-) | EIDM|
| sigmagap| 0.10 | [0,1]| Estimation error magnitude of the gap between the vehicle and the leading vehicle (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (-)  | EIDM|
| sigmaerror| 0.10 | [0,1]| Driving error magnitude (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (-)| EIDM|
| jerkmax | 3.00 | >= 1| The maximal change in acceleration between simulation steps (m/s^3)| EIDM|
| epsilonacc| 1.00 | >= 0| Maximal acceleration difference between simulation steps. The driver reacts immediately when the computed threshold is reached (originally from [Reference](https://doi.org/10.1016/j.trpro.2017.05.011)) (m/s^2)  | EIDM|
| taccmax | 1.20 | >= 0| Time it approx. takes the driver to reach the maximal acceleration after drive-off (s)| EIDM|
| Mflatness| 2.00 | >= 1 & <= 5.0 | Value to flatten the drive-off acceleration curve (-)| EIDM|
| Mbegin  | 0.70 | >= 0 & <= 1.5 | Value to shift the drive-off acceleration curve along the x-axis (-)| EIDM|
| maxvehpreview  | 0| >= 0| - not yet integrated - Number of vehicles the driver can see for spatial anticipation (originally from [Human Driver Model](https://doi.org/10.1016/j.physa.2005.05.001)) (-)  | EIDM|
| vehdynamics| 0| 0 or 1   | - not yet integrated - Bool variable to add vehicle resistance terms to the CF-model's acceleration calculation (turn on=1/off=0) (-)| EIDM|

To select a car following model the following syntax should be used:

```xml
<vType id="idmAlternative" length="5" minGap="2" carFollowModel="IDM" tau="1.0" .../>
```

## 3. 换道


```xml
<routes>

  <vType id="t01" vClass="passenger" carFollowModel="Krauss" probability="0.9" accel="2.6" decel="4.5" sigma="0.5" laneChangeModel="DK2008"/>
  <vType id="t02" vClass="truck" carFollowModel="Krauss" probability="0.1" accel="2.6" decel="4.5" sigma="0.5" laneChangeModel="DK2008"/>
  <vTypeDistribution id="typedist1" vTypes="t01 t02"/>
  <interval begin="0" end="3600">
    <flow id="0" from="E1" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="1" from="E3" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="2" from="E2" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
    <flow id="3" from="E0" begin="0" end="3600" departLane="best" period="exp(0.2)" type="typedist1"/>
  </interval>

</routes>
```

### 3.1 换道模型 Lane-Changing Models

The lane-changing models currently implemented in SUMO are given in the
following table.

| Attribute Value | Description|
| --------------- | -------------------------------------------------------------------------------------------------------- |
| LC2013   | The default car following model, developed by Jakob Erdmann based on DK2008 (see [SUMO’s Lane-Changing Model](http://elib.dlr.de/102254/)). This is the default model.|
| SL2015   | Lane-changing model for [sublane-simulation](Simulation/SublaneModel.md) (used by default when setting option **--lateral-resolution** {{DT_FLOAT}}). This model can only be used with the sublane-extension.<br><br>**Caution:** This model may technically be used without activating sublane-simulation but this usage has not been fully tested and may not work as expected.  |
| DK2008   | The original lane-changing model of sumo until version 0.18.0, developed by Daniel Krajzewicz (see [Traffic Simulation with SUMO – Simulation of Urban Mobility](http://link.springer.com/chapter/10.1007/978-1-4419-6142-6_7)). |

### 3.2 相关参数 Car-Following Model Parameters

Mostly, each model uses its own set of parameters. The following table
lists which parameter are used by which model(s).

| Attribute | Description| Models  |
| ----------------------- | ----------------------------- | -------------- |
| lcStrategic| The eagerness for performing strategic lane changing. Higher values result in earlier lane-changing. *default: 1.0, range \[0-inf), -1*  A value of 0 sets the lookahead-distance to 0 (vehicles can still change at the end of their lane) whereas -1 disables strategic changing completely.| LC2013, SL2015 |
| lcCooperative| The willingness for performing cooperative lane changing. Lower values result in reduced cooperation. *default: 1.0, range \[0-1\]* , -1  A value of 0 would still permit changing if the target lane affords higher speed whereas -1 disables cooperative changing completely| LC2013, SL2015 |
| lcSpeedGain| The eagerness for performing lane changing to gain speed. Higher values result in more lane-changing. *default: 1.0, range \[0-inf)*| LC2013, SL2015 |
| lcKeepRight| The eagerness for following the obligation to keep right. Higher values result in earlier lane-changing. *default: 1.0, range \[0-inf)*| LC2013, SL2015 |
| lcOvertakeRight  | The probability for violating rules gainst overtaking on the right *default: 0, range \[0-1\]*| LC2013, SL2015 |
| lcOpposite| The eagerness for overtaking through the opposite-direction lane. Higher values result in more lane-changing. *default: 1.0, range \[0-inf)*| LC2013  |
| lcLookaheadLeft  | Factor for configuring the strategic lookahead distance when a change to the left is necessary (relative to right lookahead). *default: 2.0, range \[0-inf)*| LC2013, SL2015 |
| lcSpeedGainRight | Factor for configuring the threshold asymmetry when changing to the left or to the right for speed gain. By default the decision for changing to the right takes more deliberation. Symmetry is achieved when set to 1.0. *default: 0.1, range \[0-inf)* | LC2013, SL2015 |
| lcSpeedGainLookahead| Lookahead time in seconds for anticipating slow down. *default: 0 (LC2013), 5 (SL2015), range \[0-inf)* | LC2013, SL2015 |
| lcOvertakeDeltaSpeedFactor | Speed difference factor for the eagerness of overtaking a neighbor vehicle before changing lanes. If the actual speed difference between ego and neighbor is higher than factor\*speedlimit, this vehicle will try to overtake the leading vehicle on the neighboring lane before performing the lane change. *default: 0 range \[-1-1]* | LC2013, SL2015 |
| lcKeepRightAcceptanceTime | Time threshold for changing the willingness to change right. The value is compared against the anticipated time of unobstructed driving on the right. Lower values will encourage keepRight changes. If the value is changed from it's default, fast approaching follower vehicles will also impact willingness to move to the right lane. *default: -1 (legacy behavior where acceptance time ~ 7 \* currentSpeed) range \[0-inf)* | LC2013, SL2015 |
| lcCooperativeRoundabout | Factor that increases willingness to move to the inside lane in a multi-lane roundabout. *default: lcCooperative, range \[0-1\]* | LC2013, SL2015 |
| lcCooperativeSpeed| Factor for cooperative speed adjustments. *default: lcCooperative, range \[0-1\]* | LC2013, SL2015 |
| minGapLat| The desired minimum lateral gap when using the [sublane-model](Simulation/SublaneModel.md) , *default: 0.6* | SL2015 |
| lcSublane | The eagerness for using the configured lateral alignment within the lane. Higher values result in increased willingness to sacrifice speed for alignment. *default: 1.0, range \[0-inf)*| SL2015  |
| lcPushy   | Willingness to encroach laterally on other drivers. *default: 0, range \[0-1\]*| SL2015  |
| lcPushyGap| Minimum lateral gap when encroaching laterally on other drives (alternative way to define lcPushy). *default: minGapLat, range 0 to minGapLat*| SL2015  |
| lcAssertive| Willingness to accept lower front and rear gaps on the target lane. The required gap is divided by this value. *default: 1, range: positive reals*| LC2013,SL2015  |
| lcImpatience| Dynamic factor for modifying lcAssertive and lcPushy. *default: 0 (no effect) range -1 to 1*. Impatience acts as a multiplier. At -1 the multiplier is 0.5 and at 1 the multiplier is 1.5.   | SL2015  |
| lcTimeToImpatience| Time to reach maximum impatience (of 1). Impatience grows whenever a lane-change manoeuvre is blocked.. *default: infinity (disables impatience growth)*  | SL2015  |
| lcAccelLat| maximum lateral acceleration per second. *default: 1.0*| SL2015  |
| lcTurnAlignmentDistance | Distance to an upcoming turn on the vehicles route, below which the alignment should be dynamically adapted to match the turn direction. *default: 0.0 (i.e., disabled)*| SL2015  |
| lcMaxSpeedLatStanding   | Constant term for lateral speed when standing. *default: maxSpeedLat (i.e., disabled)*   | LC2013, SL2015  |
| lcMaxSpeedLatFactor| Bound on lateral speed while moving computed as lcMaxSpeedLatStanding + lcMaxSpeedLatFactor \* getSpeed(). If > 0, this is an upper bound (vehicles change slower at low speed, if < 0 this is a lower bound on speed and should be combined with lcMaxSpeedLatStanding > maxSpeedLat (vehicles change faster at low speed).  *default: 1.0*  | LC2013, SL2015  |
| lcMaxDistLatStanding   | The maximum lateral maneuver distance in *m* while standing (currently used to prevent "sliding" keepRight changes).  *default: 1.6 and 0 for two-wheelers*   | LC2013, SL2015  |
| lcLaneDiscipline| Reluctance to perform speedGain-changes that would place the vehicle across a lane boundary. *default: 0.0*| SL2015  |
| lcSigma| Lateral positioning-imperfection. *default: 0.0*  | LC2013, SL2015  |

The parameters are set within the `<vType>`:

```xml
<vType id="myType" lcStrategic="0.5" lcCooperative="0.0"/>
```
