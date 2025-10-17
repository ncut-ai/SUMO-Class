# TraCI开发示例

## 1. 启动并运行仿真

- 导入traci

```python
import traci
```
- 初始化仿真信息

```python
sumoCmd = ["sumo-gui", "-c", "xxx.sumocfg", '--start']
```

- 启动仿真

```python
traci.start(sumoCmd)
```
- 运行仿真

```python
while traci.simulation.getMinExpectedNumber() > 0:
   traci.simulationStep()
```

- 关闭仿真

```python
traci.close()
```

- 示例代码

```python
import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__)) # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo-gui", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

# 运行至仿真结束
while traci.simulation.getMinExpectedNumber() > 0:
   traci.simulationStep()
   print(traci.simulation.getTime()) # 输出仿真时间

# 关闭仿真
traci.close()
```

## 2. 获取数据（Value Retrieval）

### 2.1 车辆相关数据

- [车辆相关数据获取变量表](https://sumo.dlr.de/docs/TraCI/Vehicle_Value_Retrieval.html)
- [车辆类型相关变量表](https://sumo.dlr.de/docs/TraCI/VehicleType_Value_Retrieval.html)

- 示例代码
```python
import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__))  # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

step = 0  # 计数

# 运行至仿真结束
while step < 3600:

    traci.simulationStep()  # 执行一步仿真
    step += 1  # +1s

    veh_id_list = traci.vehicle.getIDList()  # 当前仿真时刻路网中所有车辆ID
    veh_id_count = traci.vehicle.getIDCount()  # 所有id个数

    for veh_id in veh_id_list:  # 遍历所有id
        # 获取车辆信息
        veh_speed = traci.vehicle.getSpeed(veh_id)  # 车辆速度
        veh_pos = traci.vehicle.getPosition(veh_id)  # (x坐标，y坐标)
        veh_lane_pos = traci.vehicle.getLanePosition(veh_id)  # 在车道上的位置
        veh_edge_id = traci.vehicle.getRoadID(veh_id)  # 所在edge
        veh_lane_id = traci.vehicle.getLaneID(veh_id)  # 所在lane
        veh_distance = traci.vehicle.getDistance(veh_id)  # 车辆行驶距离
        # 车辆类型id：BUS_A, BUS_B, vt_car, vt_truck
        veh_type = traci.vehicle.getTypeID(veh_id)
        # veh_class = traci.vehicle.getVehicleClass(veh_type)  # 车辆类型
        veh_max_speed = traci.vehicletype.getMaxSpeed(veh_type)
        veh_class = traci.vehicletype.getVehicleClass(veh_type)  # 车辆类型
# 关闭仿真
traci.close()

```

```python
import os
import traci
import traci.constants as tc
import numpy as np  #被导入的块命名为np

os.chdir(os.path.dirname(__file__)) # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

# 运行至仿真结束
while traci.simulation.getMinExpectedNumber() > 0:
   traci.simulationStep()
   print(traci.simulation.getTime()) # 输出仿真时间
   list_speed = []
   for veh_id in traci.vehicle.getIDList():  # 遍历当前仿真中的每一辆车
        s = traci.vehicle.getSpeed(veh_id)  # 获取指定车辆的速度
        list_speed.append(s)   # 把这辆车的车速添加到列表中
   print(f"当前仿真中所有车辆的平均速度：{np.mean(list_speed)}")
# 关闭仿真
traci.close()
```


### 2.2 检测器相关数据

- [获取E1相关数据变量表](https://sumo.dlr.de/docs/TraCI/Induction_Loop_Value_Retrieval.html)
- [获取E2相关数据变量表](https://sumo.dlr.de/docs/TraCI/Lane_Area_Detector_Value_Retrieval.html)
- [获取E3相关数据变量表](https://sumo.dlr.de/docs/TraCI/Multi-Entry-Exit_Detectors_Value_Retrieval.html)

- 示例代码
```python
import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__))  # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

step = 0  # 计数

# 运行至仿真结束
while step < 3600:

    traci.simulationStep()  # 执行一步仿真
    step += 1  # +1s

    # 获取检测器数据
    # E1
    '''    
    traci.inductionloop.getLastStepVehicleNumber("detID")
    traci.inductionloop.getLastStepMeanSpeed(loopID="e1_det_id")
    traci.inductionloop.getLastStepOccupancy(loopID="e1_det_id")
    traci.inductionloop.getIntervalVehicleNumber("det_id")
    traci.inductionloop.getIntervalMeanSpeed("det_id")
    traci.inductionloop.getIntervalOccupancy("det_id")
    traci.inductionloop.getLastIntervalVehicleNumber("det_id")
    traci.inductionloop.getLastIntervalMeanSpeed("det_id")
    traci.inductionloop.getLastIntervalOccupancy("det_id")
    '''

    # E2
    e2_halting_number = traci.lanearea.getLastStepHaltingNumber('shoutinanlu_N2S_5')  # 停车次数
    e2_mean_speed = traci.lanearea.getLastStepMeanSpeed('shoutinanlu_N2S_5')  # 平均速度
    e2_occupancy = traci.lanearea.getLastStepOccupancy('shoutinanlu_N2S_5')  # 占有率
    e2_veh_num = traci.lanearea.getLastStepVehicleNumber('shoutinanlu_N2S_5')  # 车辆数
    e2_veh_ids = traci.lanearea.getLastStepVehicleIDs('shoutinanlu_N2S_5')  # 车辆ID
    e2_jam_len_veh = traci.lanearea.getJamLengthVehicle('shoutinanlu_N2S_5')  # 排队车辆数
    e2_jam_len_m = traci.lanearea.getJamLengthMeters('shoutinanlu_N2S_5')  # 排队长度

    e2_mean_speed_interval = traci.lanearea.getIntervalMeanSpeed('shoutinanlu_N2S_5')  # 平均速度，时间间隔
    e2_occupancy_interval = traci.lanearea.getIntervalOccupancy('shoutinanlu_N2S_5')  # 占有率，时间间隔
    e2_veh_num_interval = traci.lanearea.getIntervalVehicleNumber('shoutinanlu_N2S_5')  # 车辆数，时间间隔
    e2_jam_len_max_interval = traci.lanearea.getIntervalMaxJamLengthInMeters('shoutinanlu_N2S_5')  # 最大拥堵长度，时间间隔

    e2_mean_speed_interval_last = traci.lanearea.getLastIntervalMeanSpeed('shoutinanlu_N2S_5')  # 平均速度，上个时间间隔
    e2_occupancy_interval_last = traci.lanearea.getLastIntervalOccupancy('shoutinanlu_N2S_5')  # 占有率，上个时间间隔
    e2_veh_num_interval_last = traci.lanearea.getLastIntervalVehicleNumber('shoutinanlu_N2S_5')  # 车辆数，上个时间间隔
    e2_jam_len_max_interval_last = traci.lanearea.getLastIntervalMaxJamLengthInMeters('shoutinanlu_N2S_5')  # 最大拥堵长度，上个时间间隔

    # E3
    e3_halting_num = traci.multientryexit.getLastStepHaltingNumber('首体路整体')  # 停车次数
    e3_mean_speed = traci.multientryexit.getLastStepMeanSpeed('首体路整体')  # 平均速度
    e3_occupancy = traci.multientryexit.getLastStepVehicleNumber('首体路整体')  # 车辆数

    e3_mean_halts_last_interval = traci.multientryexit.getLastIntervalMeanHaltsPerVehicle('首体路整体')  # 平均停车次数
    e3_mean_time_loss_last_interval = traci.multientryexit.getLastIntervalMeanTimeLoss('首体路整体')  # 平均时间损失
    e3_mean_travel_time_last_interval = traci.multientryexit.getLastIntervalMeanTravelTime('首体路整体')  # 平均旅行时间
    e3_veh_num_last_interval = traci.multientryexit.getLastIntervalVehicleSum('首体路整体')  # 车辆数
# 关闭仿真
traci.close()

```

### 2.3 信号灯相关数据

- [信号灯数据获取变量表](https://sumo.dlr.de/docs/TraCI/Traffic_Lights_Value_Retrieval.html)

- 示例代码
```python
import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__)) # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

# 运行至仿真结束
while traci.simulation.getMinExpectedNumber() > 0:
   
   traci.simulationStep() # 执行一步仿真

   s_time = traci.simulation.getTime() # 当前仿真时间
   tls_ryg_state = traci.trafficlight.getRedYellowGreenState('J0') # J0路口当前相位的设置
   tls_phase_duation = traci.trafficlight.getPhaseDuration('J0') # J0当前相位时长
   tls_phase = traci.trafficlight.getPhase('J0') # 当前相位序号
   tls_program = traci.trafficlight.getProgram('J0') # 当前配时方案序号
   tls_next_switch = traci.trafficlight.getNextSwitch('J0') # J0下一个相位切换时间


   print(s_time) # 输出仿真时间
   print(f"J0信号配时方案： {tls_ryg_state}") 
   print(f"J0当前相位时长： {tls_phase_duation}") 
   print(f"J0当前相位： {tls_phase}") 
   print(f"J0当前信号配时方案： {tls_program}") 
   print(f"J0下一相位切换时间： {tls_next_switch}") 

   # J0当前相位已执行时间 = 当前仿真时间 - (J0下一相位切换时间 - J0当前相位时长)
   tls_phase_passed = s_time - (tls_next_switch - tls_phase_duation) 
   # J0当前相位剩余时间 = J0当前相位时长 - J0当前相位已执行时间
   tls_phase_remain = tls_phase_duation - tls_phase_passed 
   
   print(f"J0当前相位已执行时间： {tls_phase_passed}") 
   print(f"J0当前相位剩余时间： {tls_phase_remain}") 

   tls_cycle_time = traci.trafficlight.getParameter('J0', 'cycleTime') # J0周期长度
   print(f"周期长度：{tls_cycle_time}")
   tls_cycle_second = traci.trafficlight.getParameter('J0', 'cycleSecond') # 周期内的时间
   print(f"周期内的执行时间：{tls_cycle_second}")
   tls_offset = traci.trafficlight.getParameter('J0', 'offset') # 相位差
   print(f"相位差：{tls_offset}")
   tls_type = traci.trafficlight.getParameter('J0', 'typeName') # 控制类型
   print(f"控制类型：{tls_type}")

# 关闭仿真
traci.close()
```


## 3. 修改状态（State Changing）

### 3.1 调整车辆状态

- [调整车辆状态变量表](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html)
- [调整车辆类型变量表](https://sumo.dlr.de/docs/TraCI/Change_VehicleType_State.html)

- 示例代码
```python
changeLane(self, vehID, laneIndex, duration)
    changeLane(string, int, double) -> None
    Forces a lane change to the lane with the given index; The lane change
    will be attempted for the given duration (in s) and if it succeeds,
    the vehicle will stay on that lane for the remaining duration.

moveTo(self, vehID, laneID, pos, reason=0)
    moveTo(string, string, double, integer) -> None
     
    Move a vehicle to a new position along its current route.

setSpeed(self, vehID, speed)
    setSpeed(string, double) -> None
     
    Sets the speed in m/s for the named vehicle within the last step.
    Calling with speed=-1 hands the vehicle control back to SUMO.

slowDown(self, vehID, speed, duration)
    slowDown(string, double, double) -> None
     
    Changes the speed smoothly to the given value over the given amount
    of time in seconds (can also be used to increase speed).
```

### 3.2 调整信号灯控制策略

- [调整信号灯状态变量表](https://sumo.dlr.de/docs/TraCI/Change_Traffic_Lights_State.html)

- 示例代码
```python
setPhase(self, tlsID, index)
    setPhase(string, integer) -> None
     
    Switches to the phase with the given index in the list of all phases for
    the current program.

setPhaseDuration(self, tlsID, phaseDuration)
    setPhaseDuration(string, double) -> None
     
    Set the remaining phase duration of the current phase in seconds.
    This value has no effect on subsquent repetitions of this phase.

setPhaseName(self, tlsID, name)
    setPhaseName(string, string) -> None
     
    Sets the name of the current phase within the current program

setProgram(self, tlsID, programID)
    setProgram(string, string) -> None
     
    Switches to the program with the given programID. The program must have
    been loaded earlier. The special value 'off' can always be used to
    switch off the traffic light.
```

## 4. 获取周期长度

- 方式一
```python
def get_cycle_time_by(tlsID, pID):
    """根据tlsID和program ID统计信号周期长度"""
    program_logics = traci.trafficlight.getAllProgramLogics(tlsID) #获取logic结构参数

    for program in program_logics: # 遍历logic参数
        if program.programID == pID: # 判断是否相等
            the_program = program
            break
    the_phases = the_program.getPhases() # 取出相位logic
    cycle_time = 0
    for ph in the_phases: # duration求和
        cycle_time += ph.duration
    return cycle_time # 返回周期时长
```

- 方式二
```python
    ct = traci.trafficlight.getParameterWithKey('J1','cycleTime')
    print(ct)
```

## 5. 信号配时方案ProgramLogic相关操作

```python
    # 获取J1路口的信号配时logics
    all_programs = traci.trafficlight.getAllProgramLogics("J1")

    the_p = all_programs[0] # 信号配时方案

    ct = the_p.getType()
    ct0 = the_p.getSubID()
    ct1 = the_p.getPhases() # 信号配时方案tuple
    
    ct1 = list(ct1) # 转换为list
    ct1[0].duration = 108 # 可任意修改值
    
    # 各相位基本信息
    phase_num = len(ct1)
    for i in range(phase_num):
        print(ct1[i].duration)
        print(ct1[i].minDur)
        print(ct1[i].maxDur)
        print(ct1[i].state)
    
    # 生成新的信号配时方案logic
    the_logic = traci.trafficlight.Logic('0', 0, 0, ct1, {})

    # 更新路口控制方案
    traci.trafficlight.setProgramLogic('J1', the_logic)
```