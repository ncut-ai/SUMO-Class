# 交叉口模型

## Junction Model Parameters

The behavior at intersections may be configured with the parameters
listed below.

| Attribute| Value Type | Default| Description |
| ---------------------- | ------------------------------------ | ---------- | ----------------------------------------- |
| jmCrossingGap| float \>= 0 (m)| 10 | Minimum distance to pedestrians that are walking towards the conflict point with the ego vehicle. If the pedestrians are further away the vehicle may drive across the pedestrian crossing (excluding walking area). So, the lower the value, the braver (more aggressive) the driver. |
| jmIgnoreKeepClearTime| float (s)| \-1| The accumulated waiting time (see Option [**--waiting-time-memory**](sumo.md#processing)) after which a vehicle will [drive onto an intersection even though this might cause jamming](Simulation/Intersections.md#junction_blocking). For negative values, the vehicle will always try to keep the junction clear.|
| jmDriveAfterRedTime| float (s)| \-1| This value causes vehicles to violate a red light if the light has changed to red more recently than the given threshold. When set to 0, vehicles will always drive at yellow but will try to brake at red. If this behavior causes a vehicle to drive so fast that stopping is not possible any more it will not attempt to stop. This value also applies to [the default pedestrian model](Simulation/Pedestrians.md#model_striping). |
| jmDriveAfterYellowTime | float (s)| \-1| This value causes vehicles to violate a yellow light if the light has changed more recently than the given threshold. Vehicles that are too fast to brake always drive at yellow..|
| jmDriveRedSpeed| float (m/s)| *maxSpeed* | This value causes vehicles affected by *jmDriveAfterRedTime* to slow down when violating a red light. The given speed will not be exceeded when entering the intersection.|
| jmIgnoreFoeProb| float| 0| This value causes vehicles and pedestrians to ignore foe vehicles that have right-of-way with the given probability. The check is performed anew every simulation step. (range \[0,1\]).|
| jmIgnoreFoeSpeed | float (m/s)| 0| This value is used in conjunction with *jmIgnoreFoeProb*. Only vehicles with a speed below or equal to the given value may be ignored.|
| jmIgnoreJunctionFoeProb| float| 0| This value causes vehicles to ignore foe vehicles and pedestrians that have already entered a junction with the given probability. The check is performed anew every simulation step. (range \[0,1\]).|
| jmSigmaMinor | float, scaling factor (like *sigma*) | sigma| This value configures driving imperfection (dawdling) while passing a minor link (ahead of the intersection after having committed to drive and while still on the intersection).|
| jmStoplineGap| float \>= 0 (m)| 1| This value configures stopping distance in front of prioritary / TL-controlled stop line. In case the stop line has been relocated by a [**stopOffset**](Networks/SUMO_Road_Networks.md#stop_offsets) item, the maximum of both distances is applied. |
| jmTimegapMinor | float s| 1| This value defines the minimum time gap when passing ahead of a prioritized vehicle.|
| impatience | float or 'off' | 0.0| Willingness of drivers to impede vehicles with higher priority. See below for semantics.|

The parameters are set within the `<vType>`:

```xml
<vType id="ambulance" jmDriveAfterRedTime="300" jmDriveRedSpeed="5.56"/>
```

### Impatience

The impatience of a driver is value between 0 and 1 that grows whenever
the driver has to stop unintentionally (i.e. due to a jam or waiting at
an intersection). The impatience value is computed as

```xml
MAX(0, MIN(1.0, baseImpatience + waitingTime / timeToMaxImpatience))
```

Where baseImpatience is configured by setting the vType-attribute
*impatience* and timeToMaxImpatience is set using the option **--time-to-impatience** (default
300s). Setting this option to 0 disables impatience growth. The value of baseImpatience may be negative to slow the growth of
the dynamically computed impatience. It may also be defined with the
value **off** to prevent drivers from becoming impatient.

The impatience value is used to represent a drivers willingness to
impede vehicles with higher priority. At a value of 1 or above, the
driver will use any gap that is *safe* in the sense of
collision-avoidance even if it means that another vehicle has to brake
as hard as it can. At a value of 0, the driver will only perform
maneuvers that do not force other vehicles to slow down. Intermediate
values interpolate smoothly between these extremes.

### Transient Parameters

Junction model parameters that are expected to change during the simulation are modelled via [generic parameters](https://sumo.dlr.de/docs/Simulation/GenericParameters.md). The following parameters are supported (via xml input and `traci.vehicle.setParameter`):

- junctionModel.ignoreIDs : ignore foe vehicles with the given ids
- junctionModel.ignoreTypes : ignore foe vehicles that have any of the given types

If multiple ignore parameters are set, they are combined with "or".
Foes are ignored while they are approaching a junction and also while they are on the junction.

Example:

```xml
<vehicle id="ego" depart="0" route="r0">
   <param key="junctionModel.ignoreIDs" value="foe1 foe2"/>
   <param key="junctionModel.ignoreTypes" value="bikeType"/>
</vehicle>
```