---
title: Traffic Lights
---

# 信号配时相关设置

<https://github.com/eclipse/sumo/blob/main/docs/web/docs/Simulation/Traffic_Lights.md>

## 1. 自动生成 TLS-Programs

“.bat”此种方式并不起作用：

```bash
call="%SUMO_HOME%bin\netconvert" -s updated.net.xml --plain-output-prefix PLAIN
call="%SUMO_HOME%bin\netconvert" -e plain.edg.xml -n plain.nod.xml -x plain.con.xml -i plain.tll.xml  -o updated-actuated.net.xml   --default.crossing-width 4 --default.sidewalk-width 2 --default.bikelane-width 2 --tls.cycle.time 150 --tls.default-type actuated --ignore-errors.edge-type
pause
```

## 2. <tlLogic\> 的属性说明

The following attributes/elements are used within the tlLogic element:

| Attribute Name | Value Type| Description|
| -------------- | ------------------------------------- | ---------------- |
| **id** | id (string) | Typically the id for a traffic light is identical with the junction id. |
| **type** | enum (static, actuated, delay_based) |  (固定配时, phase prolongation based on time gaps between vehicles (actuated), or on accumulated time loss of queued vehicles (delay_based) )|
| **programID**| id (string) | |
| **offset** | int | |

## 3. <phase\> Attributes

| Attribute Name | Value Type| Description|
| -------------- | --------------------- | -------------------------- |
| **duration** | time (int)| The duration of the phase|
| **state**| list of signal states | The traffic light states for this phase, see below |
| minDur | time (int)|  控制类型为**actuated**时起作用|
| maxDur | time (int)| 控制类型为**actuated**时起作用，和minDur一起使用|
| name | string| 采用additional-files方式时，可以使用汉字 |
| next | list of phase indices (int ...) |  |

### 信号状态的定义 Signal state definitions

The following signal colors are used:

| Character | GUI Color| Description|
| --------- | ---------------------------------------------------------- | -------------------- |
| r | <span style="color:#FF0000; background:#FF0000">FOO</span> |   |
| y | <span style="color:#FFFF00; background:#FFFF00">FOO</span> |  |
| g | <span style="color:#00B300; background:#00B300">FOO</span> |  no priority  |
| G | <span style="color:#00FF00; background:#00FF00">FOO</span> |  priority |
| s | <span style="color:#800080; background:#800080">FOO</span> | 'green right-turn arrow' requires stopping - vehicles may pass the junction if no vehicle uses a higher priorised foe stream. They always stop before passing. This is only generated for junction type *traffic_light_right_on_red*. |
| u | <span style="color:#FF8000; background:#FF8000">FOO</span> | 'red+yellow light' for a signal, may be used to indicate upcoming green phase but vehicles may not drive yet (shown as orange in the gui) |
| o | <span style="color:#804000; background:#804000">FOO</span> | 'off - blinking' signal is switched off, blinking light indicates vehicles have to yield|
| O | <span style="color:#00FFFF; background:#00FFFF">FOO</span> | 'off - no signal' signal is switched off, vehicles have the right of way|

## 4. 交通信号控制

### 4.1 固定信号配时

信号配时文件“tls-program-static.xml”：

```xml
<additional>
    <tlLogic id="J7" type="static" programID="pid-0" offset="0">
        <phase duration="50" name="南北直行"         state="gGrgrrgGrgrr" />
        <phase duration="3"  name="黄灯（南北直行）"  state="gyrgrrgyrgrr"/>
        <phase duration="1"  name="全红（南北直行）"  state="rrrrrrrrrrrr"/>
        <phase duration="20" name="南北左转"         state="grGgrrgrGgrr"/>
        <phase duration="3"  name="黄灯（南北左转）"  state="grygrrgrygrr"/>
        <phase duration="1"  name="全红（南北左转）"  state="rrrrrrrrrrrr"/>
        <phase duration="50" name="东西直行"         state="grrgGrgrrgGr"/>
        <phase duration="3"  name="黄灯（东西直行）"  state="grrgyrgrrgyr"/>
        <phase duration="1"  name="全红（东西直行）"  state="rrrrrrrrrrrr"/>
        <phase duration="20" name="东西左转"         state="grrgrGgrrgrG"/>
        <phase duration="3"  name="黄灯（东西左转）"  state="grrgrygrrgry"/>
        <phase duration="1"  name="全红（东西左转）"  state="rrrrrrrrrrrr"/>
    </tlLogic>
</additional>
```

在.sumocfg中添加：

```xml
<additional-files value="tls-program-static.xml"/>
```

### 4.2 'actuated'类型 （基于车辆时距的相位延长方法 phase prolongation based on time gaps between vehicles (actuated)）

构造“tls-program-actuated.xml”：

```xml
<additional>
    <tlLogic id="J7" type="actuated" programID="pid-actuated" offset="0">
        <param key="max-gap" value="5.0"/>
        <param key="detector-gap" value="15.75"/>
        <param key="passing-time" value="2.0"/>
        <param key="vTypes" value=""/>
        <param key="show-detectors" value="true"/>
        <param key="file" value="tsl-actuated-output.xml"/>
        <param key="freq" value="300"/>
        <param key="jam-threshold" value="100"/>
        <param key="detector-length" value="350"/>

        <phase duration="50" name="南北直行"         state="gGrgrrgGrgrr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="黄灯（南北直行）"  state="gyrgrrgyrgrr"   />
        <phase duration="1"  name="全红（南北直行）"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="南北左转"         state="grGgrrgrGgrr"   minDur="10" maxDur="50"/>
        <phase duration="3"  name="黄灯（南北左转）"  state="grygrrgrygrr"   />
        <phase duration="1"  name="全红（南北左转）"  state="rrrrrrrrrrrr"   />
        <phase duration="50" name="东西直行"         state="grrgGrgrrgGr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="黄灯（东西直行）"  state="grrgyrgrrgyr"   />
        <phase duration="1"  name="全红（东西直行）"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="东西左转"         state="grrgrGgrrgrG"   minDur="10" maxDur="50"/>
        <phase duration="3"  name="黄灯（东西左转）"  state="grrgrygrrgry"   />
        <phase duration="1"  name="全红（东西左转）"  state="rrrrrrrrrrrr"   />
    </tlLogic>
</additional>
```

在.sumocfg中添加：

```xml
<additional-files value="tls-program-actuated.xml"/>
```

#### Detectors

The detector names take the form `TLSID_PROGRAMID_EDGEINDEX.LANEINDEX` where

- **TLSID** is the id of the tlLogic element
- **PROGRAMID** is the value attribute 'programID'
- **EDGEINDEX** is a running index that starts at 0 for edge that approaches tls linkIndex 0 (typically the northern approach)
- **LANEINDEX** is a running index for the current edge that starts at the first vehicular lane (sidewalks do not count)

#### Parameters

Several optional parameters can be used to control the behavior of actuated traffic lights. The examples values in the previous section are the default values for these parameters and their meaning is given below:

- **max-gap**: the maximum time gap between successive vehicles that will cause the current phase to be prolonged
(within maxDur limit)
- **detector-gap**: determines the time distance between the (automatically generated) detector and the stop line in seconds (at
each lanes maximum speed).
- **passing-time**: estimates the headway between vehicles when passing the stop line. This sets an upper bound on the distance between detector and stop line according to the formula `(minDur / passingTime + 0.5) / 7.5`. The intent of this bound is to allow all vehicles between the detector and the stop line to pass the intersection within the minDur time. A warning will be issued if the minDur gives insufficient clearing time.
- **linkMaxDur:X** (where X is a traffic light index): This sets an additional maximum duration criterion based on individual signals green duration rather than phase duration.
- **linkMinDur:X** (where X is a traffic light index): This sets an additional minimum duration criterion based on individual signals green duration rather than phase duration.
- **show-detectors** controls whether generated detectors will be visible or hidden in [sumo-gui](../sumo-gui.md). The default for all traffic lights can be set with option **--tls.actuated.show-detectors**. It is also possible to toggle this value from within the GUI by right-clicking on a traffic light.
- parameters **vTypes**, **file** and **freq** have the same meaning as for [regular
induction loop detectors](../Simulation/Output/Induction_Loops_Detectors_(E1).md).
- **coordinated** (true/false) Influence there reference point for time-in-cycle when using [coordination](#coordination)
- **cycleTime** sets the cycle time (in s) when using [coordination](#coordination). Defaults to the sum of all phase 'durations' values.
- **jam-threshold**: ignore detected vehicles if they have stood on a detector for the given time or more (activated by setting a position value)
- **detector-length**: set detector length to the given value (to ensure robust request detection with varying gaps and vehicle positions)

Some parameters are only used when a signal plan with [dynamic phase selection](#dynamic_phase_selection_phase_skipping) is active:

- **inactive-threshold** (default 180): The parameter sets the time in s after which an inactive phase will be entered preferentially.
- **linkMinDur:X** (where X is a traffic light index): This sets an additional minimum duration criterion based on individual signals rather than phase duration

#### Visualization

By setting the sumo option **--tls.actuated.show-detectors** the default visibility of detectors can be
set.

### 4.3 'delay_based'类型

在“tls-program-delay_based.xml”中定义：

```xml
<additional>
    <tlLogic id="J7" type="delay_based" programID="pid-delay_based" offset="0">
      <param key="detectorRange" value="300" />
      <param key="minTimeLoss" value="100" />
      <param key="file" value="tsl-delay_based-output.xml"/>
      <param key="freq" value="300"/>
      <param key="show-detectors" value="true"/>

        <phase duration="50" name="南北直行"         state="gGrgrrgGrgrr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="黄灯（南北直行）"  state="gyrgrrgyrgrr"   />
        <phase duration="1"  name="全红（南北直行）"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="南北左转"         state="grGgrrgrGgrr"   minDur="5" maxDur="50"/>
        <phase duration="3"  name="黄灯（南北左转）"  state="grygrrgrygrr"   />
        <phase duration="1"  name="全红（南北左转）"  state="rrrrrrrrrrrr"   />
        <phase duration="50" name="东西直行"         state="grrgGrgrrgGr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="黄灯（东西直行）"  state="grrgyrgrrgyr"   />
        <phase duration="1"  name="全红（东西直行）"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="东西左转"         state="grrgrGgrrgrG"   minDur="5" maxDur="50"/>
        <phase duration="3"  name="黄灯（东西左转）"  state="grrgrygrrgry"   />
        <phase duration="1"  name="全红（东西左转）"  state="rrrrrrrrrrrr"   />
    </tlLogic>
</additional>
```

在.sumocfg中添加：

```xml
<additional-files value="tls-program-delay_based.xml"/>
```

## 5 显示信号控制方案

在SUMO-GUI中，右键点击信号灯，在弹出窗口中选择“Show Phases”、“Track Phases”，可分别显示相位图和跟踪相位变化。
