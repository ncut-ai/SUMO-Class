![Image](http://www.ncut.edu.cn/images/logo.png)
旧版
# 北方工业大学 交通仿真技术课程资料

- SUMO教学相关

## 软件下载、安装与环境配置

- 详见[“Python、VSCODE、VS-Codium、PyCharm、Sumo详细安装步骤”](下载安装PythonPycharmSumo.md)
- 配置有GPU显卡需要安装CUDA，详见[CUDA安装流程](CUDA安装程序.md)
- [安装Anaconda](../install_anaconda/README.md)
- [注册ChatGPT](../registerchatgpt/readme.md)

## Commonly Asked Questions

- [常见问题及解答](CommonlyAskedQuestions.md)

## Sumo简介

SUMO是一个微观的，空间上连续，时间上离散的交通仿真软件，采用c++语言开发，其宏观特征包括带变道的多车道道路，基于道路交叉口的靠右侧行驶规则，支持动态路由，可以管理超过10000条街道的网络。其微观特征包括允许碰撞自由的车辆移动模式，支持单车路由。该软件特点是具有快速的OpenGL图形界面，支持多种网络格式输入，缺点是sumo本身不能提供网络仿真器所需要的轨迹文件。  
SUMO可去官网下载（<https://www.eclipse.org/sumo/>），解压后就可以使用，图形界面软是在解压后bin文件夹下的sumo-gui.exe。使用前最好设置环境变量SUMO_HOME。其实不设置似乎也可以使用，但是会有警告。SUMO_HOME的内容就是安装文件的位置，也就是bin文件夹的上一级目录。  
SUMO解压之后，作重要的是bin文件夹下的程序和tools文件夹下的程序。bin文件夹下大部分是可执行文件，但是并不像普通的可执行文件一样打开，而是需要用命令行打开，换句话说，整个功能程序并没有被包装起来，这是出于可裁剪和可维护性角度考虑的。tools下的工具则更多的是用phyton写的。

### sumo工程结构

SUMO的仿真至少需要3个文件：  

1. 道路文件，或者叫路网文件（net.xml），就是对行车道路的描述文件；  

2. 车流文件(rou.xml)，或者叫做车量行驶文件，用来描述车流量的行为。当然，更加高级的仿真可以加入别的文件，比如车辆描述文件，地形文件。  
这个很容易理解，想要做仿真，最起码要有地图吧，这就是路网文件net,xml;有了地图后是不是还要产生几辆车呢，不管你怎么产生，总之得有车，产生车的规则随意定，这就是rou.xml文件的功能。

3. 仿真配置文件（.sumocfg）

### 技术文档

如果想要了解更多的话，请参考sumo官方文档<https://sumo.dlr.de/docs/>

## 第1章 入门操作介绍

1. [快速做一个SUMO仿真](networkbuilding(nohand)/快速做一个sumo仿真.md)
2. [三种抽象网络SUMO仿真](networkbuilding(nohand)/Abstractnetworksgeneration.md)
3. [从OpenStreetMap获取数据实现SUMO仿真](networkbuilding(nohand)/Importingnon-SUMOnetworks.md)
   
## 第2章 基本操作介绍

### 2.1 [使用NetEdit创建路网并实现SUMO仿真](networkbuilding(netedit)/sumo仿真教程.md)

#### 2.1.1 [加载背景图](networkbuilding(netedit)/sumo仿真教程.md#1-加载背景图)

#### 2.1.2 [创建/绘制/编辑路网](networkbuilding(netedit)/sumo仿真教程.md#2-使用netedit创建绘制编辑路网netxml)
1. [绘制路段](networkbuilding(netedit)/sumo仿真教程.md#绘制路段)
1. [修改属性](networkbuilding(netedit)/sumo仿真教程.md#修改属性)
1. [调整路段](networkbuilding(netedit)/sumo仿真教程.md#调整路段)
1. [设置连接流向](networkbuilding(netedit)/sumo仿真教程.md#设置连接流向)
1. [添加信号灯](networkbuilding(netedit)/sumo仿真教程.md#添加信号灯)

#### 2.1.3 [生成车辆路径rou.xml](networkbuilding(netedit)/sumo仿真教程.md#3-生成车辆路径rouxml)
1. [jtrrouter方式](networkbuilding(netedit)/sumo仿真教程.md#a-jtrrouter方式)
1. [直接构造rou.xml](networkbuilding(netedit)/sumo仿真教程.md#b-直接构造rouxml文件)
1. [duarouter方式](networkbuilding(netedit)/sumo仿真教程.md#c-duarouter方式)

#### 2.1.4 [仿真数据采集](networkbuilding(netedit)/sumo仿真教程.md#4-仿真数据采集)
1. [E1检测器](networkbuilding(netedit)/sumo仿真教程.md#e1检测器)
1. [E2检测器](networkbuilding(netedit)/sumo仿真教程.md#e2检测器)
1. [E3检测器](networkbuilding(netedit)/sumo仿真教程.md#e3检测器)
1. [edge-dump、lane-dump、summary、emission、排队](networkbuilding(netedit)/sumo仿真教程.md#其他)

## 第3章 基本操作示例

1. [单交叉口仿真示例](example414243/example41/readme.md)
1. [主干路仿真示例](example414243/example42/readme.md)
1. [路网仿真示例](example414243/example43/readme.md)

## 第4章 高级操作

1. [SUMO模型参数影响分析资料](./use/sumo/SUMO模型参数影响分析/readme.md)
1. [SUMOCFG配置文件参数说明](./use/sumo/sumocfg配置文件参数说明/readme.md)
1. [行人仿真操作说明](./use/sumo/行人仿真操作说明/readme.md)
1. [公交车仿真操作说明](./use/sumo/公交车仿真操作说明/readme.md)
1. [停车场设置操作说明](./use/sumo/停车场设置操作说明/readme.md)
1. [轨道交通仿真操作说明](./use/sumo/火车仿真操作说明/readme.md)
1. [行人换乘操作说明](./use/sumo/行人换乘操作说明/readme.md)
1. [感应控制操作说明](./use/sumo/感应控制操作说明/readme.md)
1. [智能车添加操作说明](./use/sumo/智能车添加操作说明/readme.md)
1. [隔离带、路口形状修改说明](./use/sumo/路口形状修改说明/readme.md)
1. [发车、跟驰、换道模型](use/sumo/发车跟驰换道模型/readme.md)
1. [节点类型、交叉口模型等](use/sumo/节点类型+路口内的行为参数/readme.md)
1. [od2trips：从OD矩阵生成车辆路径](use/sumo/od2trips示例/readme.md)
1. [SUMO输出结果对比图绘制(python实现)](仿真输出结果绘图/readme.md)

## 第6章 [traci二次开发](./TraCI_instruction/TraCI4Traffic_tutorial.md)
