# 车辆类别、车辆类型、跟驰模型、换道模型

## 1. 车辆类别 vClass

| vClass  | bitmask bit| comment|
| -------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ignoring| \- (all bits set to 0) | may drive on all lanes regardless of set permissions.|
| private | 0 | |
| emergency| 1 | |
| authority| 2 | |
| army| 3 | |
| vip| 4 | |
| pedestrian| 5 | lanes which only allow this class are considered to be 'sidewalks' in [netconvert](netconvert.md) |
| **passenger**  | 6 | This is the default vehicle class and denotes regular passenger traffic   |
| hov| 7 | [High-occupancy vehicle](https://en.wikipedia.org/wiki/High-occupancy_vehicle_lane)|
| taxi| 8 | |
| bus| 9 | urban line traffic   |
| coach   | 10| overland transport   |
| delivery| 11| Allowed on service roads that are not meant for public traffic|
| truck   | 12| |
| trailer | 13| truck with trailer   |
| motorcycle| 14| |
| moped   | 15| motorized 2-wheeler which may not drive on motorways |
| bicycle | 16| |
| evehicle| 17| future mobility concepts such as electric vehicles which may get special access rights  |
| tram| 18| |
| rail_urban| 19| heavier than 'tram' but distinct from 'rail'. Encompasses [Light Rail](http://en.wikipedia.org/wiki/Light_Rail) and [S-Bahn](http://en.wikipedia.org/wiki/S-Bahn) |
| rail| 20| heavy rail|
| rail_electric | 21| heavy rail vehicle that may only drive on electrified tracks|
| rail_fast| 22| [High-speed-rail](https://en.wikipedia.org/wiki/High-speed_rail)   |
| ship| 23| basic class for navigating waterways|
| custom1 | 24| reserved for user-defined semantics|
| custom2 | 25| reserved for user-defined semantics|

## 2. 车辆类型 vType

A vehicle is defined using the `vType`-element as shown below:

```xml
<routes>
    <vType id="type1" accel="2.6" decel="4.5" sigma="0.5" length="5" maxSpeed="70"/>
</routes>
```

Having defined this, one can build vehicles of type "type1". The values
used above are the ones most of the examples use. They resemble a
standard vehicle as used within the Stefan Krauß' thesis.

```xml
<routes>
    <vType id="type1" accel="2.6" decel="4.5" sigma="0.5" length="5" maxSpeed="70"/>
    <vehicle id="veh1" type="type1" depart="0">
        <route edges="edge1 edge2 edge3"/>
    </vehicle>
</routes>
```

This definition is the initial one which includes both, the definition
of the vehicle's "purely physical" parameters, such as its length, its
color, or its maximum velocity, and also the used car-following model's
parameters. Please note that even though the car-following parameters
are describing values such as max. acceleration, or max. deceleration,
they mostly do not correspond to what one would assume. The maximum
acceleration for example is not the car's maximum acceleration
possibility but rather the maximum acceleration a driver choses - even
if you have a Jaguar, you probably are not trying to go to 100km/h in 5s
when driving through a city.

The default car following model is based on the work of Krauß but other
models can be selected as well. Model selection and parameterization is
done by setting further `vType`-attributes as shown below. The models and their
parameters are described in the following.

```xml
<routes>
    <vType id="type1" length="5" maxSpeed="70" carFollowModel="Krauss" accel="2.6" decel="4.5" sigma="0.5"/>
</routes>
```

Available vType Attributes

These values have the following meanings:

| Attribute Name| Value Type   | Default | Description|
| ----------------- | --------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| **id**| id (string)  | \-   | The name of the vehicle type|
| accel| float | 2.6  | The acceleration ability of vehicles of this type (in m/s^2) |
| decel| float | 4.5| The deceleration ability of vehicles of this type (in m/s^2)|
| apparentDecel| float | `==decel`   | The apparent deceleration of the vehicle as used by the standard model (in m/s^2). The follower uses this value as expected maximal deceleration of the leader.|
| emergencyDecel| float | 9.0| The maximal physically possible deceleration for the vehicle (in m/s^2).  |
startupDelay | float >= 0 | 0  | The extra delay time before starting to drive after having had to stop      
| sigma| float | 0.5| [Car-following model](#car-following_models) parameter, see below  |
| tau | float | 1.0| [Car-following model](#car-following_models) parameter, see below  |
| length| float | 5.0| The vehicle's **netto**-length (length) (in m)|
| minGap| float | 2.5| Empty space after leader \[m\]|
| maxSpeed   | float | 55.55 (200 km/h) for most vehicles, see [vClass-specific defaults](Vehicle_Type_Parameter_Defaults.md) | The vehicle's (technical) maximum velocity (in m/s)|
| desiredMaxSpeed   | float  | 2778 (1e4 km/h), 5.56 (20km/h) for bikes, 1.39 (5 km/h) for pedestrians, see [model details](Simulation/VehicleSpeed.md#desiredmaxspeed) | The vehicle desired maximum velocity (in m/s) is computed as `desiredMaxSpeed * individual_speedFactor`.   |
| speedFactor| float or [distribution spec](#defining_a_normal_distribution_for_vehicle_speeds)  | 1.0 | The vehicles expected multiplier for lane speed limits and desiredMaxSpeed  |
| speedDev   | float | 0.1| The deviation of the speedFactor; see below for details (some vClasses use a different default)|
| color| [RGB-color](#colors)   | "1,1,0" (yellow)   | This vehicle type's color   |
| vClass| class (enum) | "passenger" | An abstract [vehicle class (see below)](#abstract_vehicle_class). By default vehicles represent regular passenger cars.|
| emissionClass| emission class (enum)| ["PC_G_EU4"](Models/Emissions/HBEFA3-based.md)| An [emission class (see below)](#vehicle_emission_classes). By default a gasoline passenger car conforming to emission standard *EURO 4* is used.   |
| guiShape   | shape (enum) | "unknown"   | [a vehicle shape for drawing](#visualization). By default a standard passenger car body is drawn.|
| width| float | 1.8| The vehicle's width \[m\] (used only for visualization with the default model, affects [sublane model](Simulation/SublaneModel.md))  |
| height| float | 1.5| The vehicle's height \[m\]  |
| collisionMinGapFactor | float | depends on carFollowModel (1.0 for most models)| The minimum fraction of minGap that must be maintained to the leader vehicle to avoid a collision event  |
| imgFile| filename (string)   | ""| Image file for rendering vehicles of this type (should be grayscale to allow functional coloring)  |
| osgFile| filename (string)   | ""| Object file for rendering with OpenSceneGraph (any of the file types supported by the available OSG-plugins)|
| laneChangeModel   | lane changing model name (string) | 'LC2013'| The model used for changing lanes  |
| carFollowModel| car following model name (string) | 'Krauss'| The model used for [car following](#car-following_models)|
| personCapacity| int   | 4| The number of persons (excluding an autonomous driver) the vehicle can transport.|
| containerCapacity | int   | 0| The number of containers the vehicle can transport.  |
| boardingDuration  | float | 0.5| The time required by a person to board the vehicle.  |
| loadingDuration   | float | 90.0| The time required to load a container onto the vehicle.|
| latAlignment| float, "left", "right", "center", "compact", "nice", "arbitrary" | "right" for bicycles, "center" otherwise  | The preferred lateral alignment when using the [sublane-model](Simulation/SublaneModel.md). {{DT_FLOAT}} (in m from the center of the lane) or one of ("left", "right", "center", "compact", "nice", "arbitrary"). |
| maxSpeedLat| float | 1.0| The maximum lateral speed when using the [sublane-model or continuous lane change model](Simulation/SublaneModel.md)   |
| actionStepLength  | float | global default (defaults to the simulation step, configurable via **--default.action-step-length**) | The interval length for which vehicle performs its decision logic (acceleration and lane-changing). The given value is processed to the closest (if possible smaller) positive multiple of the simulation step length. See [actionStepLength details](Car-Following-Models.md#actionsteplength)|
| scale  | float >= 0  | scaling factor for traffic. Acts as a multiplier for option **--scale** for all vehicles of this type. Values < 1 cause a proportional reduction in traffic whereas values above 1 increase it by this factor. (default 1)|
| timeToTeleport| float   | | Override option **--time-to-teleport** for vehicles of this type |
| timeToTeleportBidi   | float   | | Override option **--time-to-teleport.bidi** for vehicles of this type |

Note, that the given type id refers to an edge type rather than a vehicle type. The edge type may be [set to an arbitrary value in the network file](Netedit/index.md#inspect).
```xml
<type id="a" priority="3" numLanes="3" speed="38.89"/>
   <restriction vClass="truck" speed="27.89"/>
</type>
```

## 跟驰模型 Car-Following Models

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

### 相关参数 Car-Following Model Parameters

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

### Default *Krauss* Model Description

The default model is a modification of the model defined by Stefan Krauß
in [Microscopic Modeling of Traffic Flow: Investigation of Collision Free Vehicle Dynamics](http://sumo.dlr.de/pdf/KraussDiss.pdf). The
implemented model follows the same idea as that of Krauß, namely: Let
vehicles drive as fast as possibly while maintaining perfect safety
(always being able to avoid a collision if the leader starts braking
within leader and follower maximum acceleration bounds). The implemented
model as in [{{SUMO}}/src/microsim/cfmodels/MSCFModel_Krauss.cpp]({{Source}}src/microsim/cfmodels/MSCFModel_Krauss.cpp) has the following differences:

- Different deceleration capabilities among the vehicles are handled
  without violating safety (the original model allowed for collisions
  in this case)
- The formula for safe velocity was adapted to maintain safety when
  using the *Ballistic*-position update rule. This was done by
  discretizing some of the continuous terms. The original model was
  defined for the *Euler*-position updated rule and would produce
  collisions when using *Ballistic*. See also
  [Simulation/Basic_Definition\#Defining_the_Integration_Method](Simulation/Basic_Definition.md#defining_the_integration_method).

## 换道模型 Lane-Changing Models

The lane-changing models currently implemented in SUMO are given in the
following table.

| Attribute Value | Description|
| --------------- | -------------------------------------------------------------------------------------------------------- |
| LC2013   | The default car following model, developed by Jakob Erdmann based on DK2008 (see [SUMO’s Lane-Changing Model](http://elib.dlr.de/102254/)). This is the default model.|
| SL2015   | Lane-changing model for [sublane-simulation](Simulation/SublaneModel.md) (used by default when setting option **--lateral-resolution** {{DT_FLOAT}}). This model can only be used with the sublane-extension.<br><br>**Caution:** This model may technically be used without activating sublane-simulation but this usage has not been fully tested and may not work as expected.  |
| DK2008   | The original lane-changing model of sumo until version 0.18.0, developed by Daniel Krajzewicz (see [Traffic Simulation with SUMO – Simulation of Urban Mobility](http://link.springer.com/chapter/10.1007/978-1-4419-6142-6_7)). |


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

!!! note
    parameter 'lcMaxSpeedLatStanding' will not be applied when a vehicle is at the end of its lane (to ensure that there are no deadlocks).

!!! caution
    Modifying and Retrieving lane change model attributes via TraCI [works different from other vType attributes](TraCI/Change_Vehicle_State.md#relationship_between_lanechange_model_attributes_and_vtypes)