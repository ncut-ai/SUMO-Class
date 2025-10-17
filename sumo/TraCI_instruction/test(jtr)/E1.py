import traci
import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np

mlt.rcParams['font.sans-serif'] = ['SimHei']#使中文字体能在图中显示
sumoBinary = "sumo-gui"
traci.start([sumoBinary, "-c", r"E:\gennet\test\test(jtr)\test_detect.sumocfg"])
step =0#计数器
list1=[]#设置三个空列表用于放置仿真得到的平均速度数据
list2=[]
list3=[]
while step < 1000:#运行步长小于1000
    traci.simulationStep()
    a=traci.lanearea.getLastStepMeanSpeed('-E7_1')#分别获取-E7_1，-E9_1，-E6_1三条车道上用E2检测器获取的平均速度
    b=traci.lanearea.getLastStepMeanSpeed('-E9_1')
    c=traci.lanearea.getLastStepMeanSpeed('-E6_1')
    list1.append(a)#将检测到的数据依次附加到设定好的表里
    list2.append(b)
    list3.append(c)
    step += 1#计数器+1
x=np.arange(1,1001)#x轴范围

plt.plot(x, list1,color='steelblue', label='-E7_1')  #list1为y轴的值 label每个plot指定一个字符串标签
plt.plot(x, list2,color='g',label='-E9_1')
plt.plot(x, list3,color='y',label='-E6_1')
plt.legend(loc='best')#将label中的值显示出来
plt.title('车辆平均速度')#设置好图像的标题
plt.ylabel('速度')#设置好y轴的代表含义
plt.xlabel('仿真步长')#设置好x轴的代表含义
plt.savefig('.\\2.png')#将得到的图像保存到当前文件夹之下，并命名为2.png
plt.show()#显示图像
traci.close()



