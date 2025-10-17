# 快速做一个sumo仿真

## 0. 说明

1.、2.部分命令可参考[GEN-NET+TRIPS-EXAMPLE.bat](1.simpleexample/GEN-NET+TRIPS-EXAMPLE.bat)

## 1. 生成一个路网

```dos
call="%SUMO_HOME%\bin\netgenerate" --grid --grid.number=4 --grid.length=400 --output-file=MySUMOFile_grid3.net.xml
```

可用NetEdit打开MySUMOFile_grid3.net.xml查看。

## 2. 生成该路网的Trips

```dos
Python "%SUMO_HOME%\tools\randomTrips.py" -n MySUMOFile_grid3.net.xml -o map3.rou.xml -e 3600 -l
```

## 3. 创建并配置test.sumocfg文件

```xml
<configuration>
    <input>
        <net-file value="MySUMOFile_grid3.net.xml"/>
        <route-files value="map3.rou.xml"/>
    </input>
    <processing>
        <default.speeddev value="0"/>
    </processing>
    <report>
        <duration-log.disable value="true"/>
        <no-step-log value="true"/>
    </report>
</configuration>
```

## 4. 运行仿真

用SUMOGUI打开tetst.sumocfg，开始仿真