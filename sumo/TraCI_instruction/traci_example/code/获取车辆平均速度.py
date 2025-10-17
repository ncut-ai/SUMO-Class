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
