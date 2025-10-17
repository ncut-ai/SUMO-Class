# TraCI教程

TRACI (Traffic Control Interface) 是 SUMO (Simulation of Urban MObility) 交通仿真器的一个关键组件，提供了一个用于实时控制和监控仿真的接口。TRACI 使用户能够在仿真运行时与 SUMO 进行交互，以实现动态调整和控制。下面是对 TRACI 的详细介绍。

TRACI 是通过 TCP/IP 连接与 SUMO 进行通信的接口。它允许外部程序控制 SUMO 中的各种仿真元素，如车辆、交通信号灯、道路网络等。

TRACI 是 SUMO 仿真器中非常重要的组件，为用户提供了强大的实时控制和监控能力。通过 TRACI，用户可以动态调整仿真参数、获取仿真数据，从而进行更加灵活和详细的交通仿真研究。

**TRACI 的功能和特点：**

1. 实时控制和监控

- 车辆控制：可以获取和设置车辆的各种属性，如速度、位置、路线等。
- 交通信号控制：可以动态调整交通信号灯的相位和时间。
- 交通流监控：可以监控道路上的交通流量、密度、平均速度等。
- 仿真管理：可以控制仿真启动、停止、步进等操作。

2. 灵活的编程接口

- 多语言支持：TRACI 主要提供 Python 接口，但也支持 C++、Java 等其他编程语言。
- 高效的通信机制：通过 TCP/IP 协议实现高效的消息传递和数据交换。

3. 扩展性

- 插件和扩展：TRACI 支持通过插件和扩展进行功能增强，可以与其他系统和工具集成，如机器学习、数据分析平台等。

**TRACI 的主要模块和方法**
- traci.simulation
- traci.vehicle
- traci.trafficlight
- traci.edge

## 1. [Python相关](python相关.md)

## 2. [TraCI参数汇总](../use/traci/readme.md)

## 3. [TraCI开发教程&示例](./traci_example/readme.md)

## 4. [仿真数据绘图](./traci_example/绘图/readme.md)