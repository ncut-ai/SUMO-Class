import traci
import numpy as np  # 被导入的块命名为np
import matplotlib.pyplot as plt
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[np.random.randint(0,14)]
    return "#"+color
sumoBinary = "sumo-gui"  #
traci.start([sumoBinary, "-c", "../../sumo_class-2022fall/example_rand.sumocfg", "--start"])  # 启动的绝对路径
plt.axis([0, 1000, 0, 500])
plt.ion()
xs = [0, 0]
ys = [1, 1]
step = 0  # 计数器
# while traci.simulation.getMinExpectedNumber() > 0:
color=randomcolor()
print(color)
while step < 1000:  # 运行时间小于3600s
    traci.simulationStep()  # 执行一步仿真

    y = traci.lane.getLastStepVehicleNumber('E0_1')
    print(y)
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = step
    ys[1] = y
    plt.plot(xs, ys, color=color)
    plt.pause(0.1)

    step += 1  # 计数器加1

traci.close()
