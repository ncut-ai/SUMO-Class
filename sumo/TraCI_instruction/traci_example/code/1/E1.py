import traci
import numpy as np  # 被导入的块命名为np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.family"] = "SimHei"  # 添加中文字体名称
mpl.rcParams["axes.unicode_minus"]=False # 由于更改了字体导致显示不出负号，此设置用来正常显示负号
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
sumoBinary = "sumo-gui"  #
traci.start([sumoBinary, "-c", "../../sumo_class-2022fall/example_rand.sumocfg","--start"])  # 启动的绝对路径
occ = []
spe = 0.0
num = []