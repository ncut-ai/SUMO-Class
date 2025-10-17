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
