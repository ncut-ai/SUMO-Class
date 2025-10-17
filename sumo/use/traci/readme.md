# traci实例

```python

import traci  # 被导入的块
from matplotlib import pyplot as plt
import numpy as np  #被导入的块命名为np
import matplotlib as mpl
mpl.rcParams["font.family"] = "SimHei"  # 添加中文字体名称
mpl.rcParams["axes.unicode_minus"]=False # 由于更改了字体导致显示不出负号，此设置用来正常显示负号
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
sumoBinary = "sumo-gui"  #
traci.start([sumoBinary, "-c", "../../sumo_class-2022fall/example_rand.sumocfg","--start"])  # 启动的绝对路径
s=0.0  # traci中车的速度
c=[]  # traci中车的编号
sums=[]  # 定义一个新列表
step=0  # 计数器
# while traci.simulation.getMinExpectedNumber() > 0:
while step<1000:  # 运行时间小于3600s
    list1 = []  # 定义一个列表收集车速
    traci.simulationStep()  # 执行一步仿真
    step += 1  # 计数器加1
    for veh_id in traci.vehicle.getIDList():  # 遍历当前仿真中的每一辆车
        s = traci.vehicle.getSpeed(veh_id)  # 获取指定车辆的速度
        list1.append(s)   # 把这辆车的车速添加到列表中
    sums.append(np.mean(list1))
x = np.arange(1,1001)
y = sums
plt.title('仿真车辆平均速度')#添加图表标题
plt.plot(x, y, marker='p', color='salmon', linestyle='--', label='平均速度')
plt.ylabel('速度')#添加y轴标题
plt.xlabel('仿真时间')#添加x轴标题

plt.legend()#设置图例
plt.show()
traci.close()

```

以上是提供的traci实例，其他可调用的traci函数都可在其他md文件中找到，自行查找即可

E1检测器:[E1](Induction_Loop_Value_Retrieval.md)
--
E2检测器:[E2](Lane_Area_Detector_Value_Retrieval.md)
--
E3检测器:[E3](Lane_Area_Detector_Value_RetrievalMulti-Entry-Exit_Detectors_Value_Retrieval.md)
--
lane_value:[lane_value](Lane_Value_Retrieval.md)
--
edge_value:[edge_value](Edge_Value_Retrieval.md)
--
traffic_light:[traffic_light](Traffic_Lights_Value_Retrieval.md)
--
simulation_value:[simulation_value](Simulation_Value_Retrieval.md)
--
vehicle_value:[vehicle_value](Vehicle_Value_Retrieval.md)
--
Available_Vehicle_attributesvehicle_:[Available_Vehicle_attributes](Available_Vehicle_attributes.md)
--
Available_vType_Attributes:[Available_vType_Attributes](Available_vType_Attributes.md)
--
Visualization:[Visualization](Visualization.md)
--
Car_Following_Models:[Car_Following_Models](Car_Following_Models.md)
--
Lane_Changing_Models:[Lane_Changing_Models](Lane_Changing_Models.md)