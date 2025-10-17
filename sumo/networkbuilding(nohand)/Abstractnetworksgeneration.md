# 三种抽象网络生成

The type of network you want to create must be stated with one of the following switches: --grid, --spider or --rand.

## 1. 放射环形路网

### 新建路网文件

- 新建一个“spider_net.bat”文件，并输入代码

  ```dos
  call="%SUMO_HOME%bin\netgenerate" --spider --spider.arm-number=4 --spider.circle-number=3 --spider.space-radius=100 --output-file=spider_map.net.xml
  pause
  ```

### 新建路网的Trips文件

- 新建一个“spider_rou.bat”文件，并输入代码

  ```dos
  python "%SUMO_HOME%tools\randomTrips.py" -n spider_map.net.xml -o spider_map.rou.xml -e 3600 -l
  pause
  ```

### 配置“test.sumocfg”文件

- 新建“spider_test.sumocfg”文档，并输入代码
  
  ```xml
  <configuration>
    <input>
        <net-file value="spider_map.net.xml"/>
        <route-files value="spider_map.rou.xml"/>
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

### 运行仿真

## 2. 棋盘型路网

### 新建路网文件

- 新建一个“checkerboard_net.bat”文件，并输入代码

  ```dos
  call="%SUMO_HOME%bin\netgenerate" --grid --grid.number=4 --grid.length=400 --output-file=checkerboard_map.net.xml
  pause
  ```

### 新建路网的Trips文件

- 新建一个“checkerboard_rou.bat”文件，并输入代码

  ```dos
  python "%SUMO_HOME%tools\randomTrips.py" -n checkerboard_map.net.xml -o checkerboard_map.rou.xml -e 3600 -l
  pause
  ```

### 配置“test.sumocfg”文件

- 新建“spider_test.sumocfg”文档，并输入代码
  
  ```xml
  <configuration>
    <input>
        <net-file value="checkerboard_map.net.xml"/>
        <route-files value="checkerboard_map.rou.xml"/>
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

### 运行仿真

## 3. 随机路网

### 新建路网文件

- 新建一个“random_net.bat”文件，并输入代码

  ```dos
  call = "%SUMO_HOME%bin\netgenerate" --rand -o random_map.net.xml --rand.iterations=200
  pause
  ```

### 新建路网的Trips文件

- 新建一个“random_rou.bat”文件，并输入代码

  ```dos
  python "%SUMO_HOME%tools\randomTrips.py" -n random_map.net.xml -o random_map.rou.xml -e 3600 -l
  pause
  ```

### 配置“test.sumocfg”文件

- 新建“random_test.sumocfg”文档，并输入代码
  
  ```xml
  <configuration>
    <input>
        <net-file value="random_map.net.xml"/>
        <route-files value="random_map.rou.xml"/>
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

### 运行仿真
