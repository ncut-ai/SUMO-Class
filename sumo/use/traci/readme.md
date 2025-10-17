# traciʵ��

```python

import traci  # ������Ŀ�
from matplotlib import pyplot as plt
import numpy as np  #������Ŀ�����Ϊnp
import matplotlib as mpl
mpl.rcParams["font.family"] = "SimHei"  # ���������������
mpl.rcParams["axes.unicode_minus"]=False # ���ڸ��������嵼����ʾ�������ţ�����������������ʾ����
plt.rcParams['font.sans-serif']=['SimHei'] # ����������ʾ���ı�ǩ
sumoBinary = "sumo-gui"  #
traci.start([sumoBinary, "-c", "../../sumo_class-2022fall/example_rand.sumocfg","--start"])  # �����ľ���·��
s=0.0  # traci�г����ٶ�
c=[]  # traci�г��ı��
sums=[]  # ����һ�����б�
step=0  # ������
# while traci.simulation.getMinExpectedNumber() > 0:
while step<1000:  # ����ʱ��С��3600s
    list1 = []  # ����һ���б��ռ�����
    traci.simulationStep()  # ִ��һ������
    step += 1  # ��������1
    for veh_id in traci.vehicle.getIDList():  # ������ǰ�����е�ÿһ����
        s = traci.vehicle.getSpeed(veh_id)  # ��ȡָ���������ٶ�
        list1.append(s)   # ���������ĳ�����ӵ��б���
    sums.append(np.mean(list1))
x = np.arange(1,1001)
y = sums
plt.title('���泵��ƽ���ٶ�')#���ͼ�����
plt.plot(x, y, marker='p', color='salmon', linestyle='--', label='ƽ���ٶ�')
plt.ylabel('�ٶ�')#���y�����
plt.xlabel('����ʱ��')#���x�����

plt.legend()#����ͼ��
plt.show()
traci.close()

```

�������ṩ��traciʵ���������ɵ��õ�traci��������������md�ļ����ҵ������в��Ҽ���

E1�����:[E1](Induction_Loop_Value_Retrieval.md)
--
E2�����:[E2](Lane_Area_Detector_Value_Retrieval.md)
--
E3�����:[E3](Lane_Area_Detector_Value_RetrievalMulti-Entry-Exit_Detectors_Value_Retrieval.md)
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