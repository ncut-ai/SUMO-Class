# 公交车相关设置方法

[公交车站、公交线路设置示例](experiments/parkingArea_ex)

## 公交车站

公交车站在busstop_def.add.xml中定义

```xml
<additional>
<busStop id="station1" lane="-E1_0" startPos="220" endPos="240"/>
<busStop id="station2" lane="-E0_0" startPos="220" endPos="240"/>
<busStop id="station3" lane="-E3_0" startPos="220" endPos="240"/>
</additional>
```

## 公交线路

在.flows.xml中定义：

```xml
<vType id="BUS_A" accel="2.6" decel="4.5" sigma="0" length="12" minGap="3" maxSpeed="70" color="1,1,1" guiShape="bus"/>
<vType id="BUS_B" maxSpeed="30" vClass="bus" Length="14.63" guiShape="bus" />

<flow id="type1" color="1,0,1"  begin="0" end= "7200" period="900" type="BUS_A"> <!--设置公交，方法1-->
<route edges="E2 -E1"/>
<stop busStop="station1" duration="30"/>
</flow>

<route id="route1" edges="E2 -E0"/>
<flow id="type2" color="1,1,0"  begin="0" end= "7200" period="900" type="BUS_A" route="route1"> <!--设置公交，方法2-->
<stop busStop="station2" duration="30"/>
</flow>

<flow id="type3" color="1,1,1"  begin="0" end= "7200" period="900" type="BUS_B" from="E2" to="-E3"> <!--设置公交，方法3-->
<stop busStop="station3" duration="30"/>
</flow>
```

## 编译和运行

在.jtrrcfg中添加：

```xml
<configuration>
    <input>
        <net-file value="test.net.xml"/>
        <route-files value="test.flows.xml"/>
        <turn-ratio-files value="test.turns.xml"/>
        <additional-files value="parkingarea_def.add.xml,busstop_def.add.xml"/>
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

在.sumocfg中添加：

```xml
<additional-files value="parkingarea_def.add.xml,busstop_def.add.xml"/>
```
