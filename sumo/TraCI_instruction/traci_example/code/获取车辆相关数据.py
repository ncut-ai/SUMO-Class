import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__))  # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']

# 启动仿真
traci.start(sumoCmd)

step = 0  # 计数

# 运行至仿真结束
while step < 3600:

    traci.simulationStep()  # 执行一步仿真
    step += 1  # +1s

    veh_id_list = traci.vehicle.getIDList()  # 当前仿真时刻路网中所有车辆ID
    veh_id_count = traci.vehicle.getIDCount()  # 所有id个数

    for veh_id in veh_id_list:  # 遍历所有id
        # 获取车辆信息
        veh_speed = traci.vehicle.getSpeed(veh_id)  # 车辆速度
        veh_pos = traci.vehicle.getPosition(veh_id)  # (x坐标，y坐标)
        veh_lane_pos = traci.vehicle.getLanePosition(veh_id)  # 在车道上的位置
        veh_edge_id = traci.vehicle.getRoadID(veh_id)  # 所在edge
        veh_lane_id = traci.vehicle.getLaneID(veh_id)  # 所在lane
        veh_distance = traci.vehicle.getDistance(veh_id)  # 车辆行驶距离
        # 车辆类型id：BUS_A, BUS_B, vt_car, vt_truck
        veh_type = traci.vehicle.getTypeID(veh_id)
        # veh_class = traci.vehicle.getVehicleClass(veh_type)  # 车辆类型
        veh_max_speed = traci.vehicletype.getMaxSpeed(veh_type)
        veh_class = traci.vehicletype.getVehicleClass(veh_type)  # 车辆类型
# 关闭仿真
traci.close()
