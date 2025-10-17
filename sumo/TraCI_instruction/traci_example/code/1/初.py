import traci
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.axis([0, 1000, 0, 10])
plt.ion()
dict_plotdata = {}
light_IDs = ['J0']
for light in light_IDs:
    dict_plotdata[light] = {}
    dict_plotdata[light]["xs"] = [0, 0]
    dict_plotdata[light]["ys"] = [0, 0]
    dict_plotdata[light]["y"] = 0
    for dict_plotdata[light]["y"] in range(0, 8):
        if dict_plotdata[light]["y"] == 0:
            dict_plotdata["color"] = 'green'
        elif dict_plotdata[light]["y"] == 1:
            dict_plotdata[light]["color"] = 'yellow'
        elif 1 < dict_plotdata[light]["y"] < 4:
            dict_plotdata[light]["color"] = 'red'
        elif dict_plotdata[light]["y"] == 4:
            dict_plotdata["color"] = 'green'
        elif dict_plotdata[light]["y"] == 5:
            dict_plotdata[light]["color"] = 'yellow'
        else:
            dict_plotdata[light]["color"] = 'red'
sumoBinary = "sumo-gui"
traci.start([sumoBinary, "-c", r"D:\sumo_class-2022fall\example_rand.sumocfg"])
step = 0

while step < 1000:
    traci.simulationStep()
    for light in light_IDs:
        dict_plotdata[light]['y'] = traci.trafficlight.getPhase(light)
        dict_plotdata[light]['xs'][0] = dict_plotdata[light]['xs'][1]
        dict_plotdata[light]['ys'][0] = dict_plotdata[light]['y']
        dict_plotdata[light]['xs'][1] = step
        dict_plotdata[light]['ys'][1] = dict_plotdata[light]['y']
        plt.plot(dict_plotdata[light]['xs'], dict_plotdata[light]['ys'], color=dict_plotdata[light]["color"],
                 linewidth=2.5)
        plt.xlabel('仿真时间')
        plt.ylabel('信号灯相位序号')
        plt.title('信号灯序号与仿真时间的关系图')
    plt.pause(0.1)
    step += 1
traci.close()