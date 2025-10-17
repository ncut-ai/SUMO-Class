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