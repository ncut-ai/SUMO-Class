import traci
import numpy as np  # 被导入的块命名为np

sumoBinary = "sumo-gui"  #
traci.start([sumoBinary, "-c", "../../sumo_class-2022fall/example_rand.sumocfg", "--start"])  # 启动的绝对路径
step = 0  # 计数器
# while traci.simulation.getMinExpectedNumber() > 0:
while step < 1000:  # 运行时间小于3600s
    traci.simulationStep()  # 执行一步仿真
    step += 1  # 计数器加1
step = 0  # 计数器
    # while traci.simulation.getMinExpectedNumber() > 0:
while step < 1800:  # 运行时间小于3600s
    traci.simulationStep()  # 执行一步仿真
    step += 1  # 计数器加1

    print(traci.inductionloop.getLastStepOccupancy('North_1'))
traci.close()
