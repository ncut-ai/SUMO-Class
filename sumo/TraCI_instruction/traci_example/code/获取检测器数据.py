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

    # 获取检测器数据
    # E1
    '''    
    traci.inductionloop.getLastStepVehicleNumber("detID")
    traci.inductionloop.getLastStepMeanSpeed(loopID="e1_det_id")
    traci.inductionloop.getLastStepOccupancy(loopID="e1_det_id")
    traci.inductionloop.getIntervalVehicleNumber("det_id")
    traci.inductionloop.getIntervalMeanSpeed("det_id")
    traci.inductionloop.getIntervalOccupancy("det_id")
    traci.inductionloop.getLastIntervalVehicleNumber("det_id")
    traci.inductionloop.getLastIntervalMeanSpeed("det_id")
    traci.inductionloop.getLastIntervalOccupancy("det_id")
    '''

    # E2
    e2_halting_number = traci.lanearea.getLastStepHaltingNumber(
        'shoutinanlu_N2S_5')  # 停车次数
    e2_mean_speed = traci.lanearea.getLastStepMeanSpeed(
        'shoutinanlu_N2S_5')  # 平均速度
    e2_occupancy = traci.lanearea.getLastStepOccupancy(
        'shoutinanlu_N2S_5')  # 占有率
    e2_veh_num = traci.lanearea.getLastStepVehicleNumber(
        'shoutinanlu_N2S_5')  # 车辆数
    e2_veh_ids = traci.lanearea.getLastStepVehicleIDs(
        'shoutinanlu_N2S_5')  # 车辆ID
    e2_jam_len_veh = traci.lanearea.getJamLengthVehicle(
        'shoutinanlu_N2S_5')  # 排队车辆数
    e2_jam_len_m = traci.lanearea.getJamLengthMeters(
        'shoutinanlu_N2S_5')  # 排队长度

    e2_mean_speed_interval = traci.lanearea.getIntervalMeanSpeed(
        'shoutinanlu_N2S_5')  # 平均速度，时间间隔
    e2_occupancy_interval = traci.lanearea.getIntervalOccupancy(
        'shoutinanlu_N2S_5')  # 占有率，时间间隔
    e2_veh_num_interval = traci.lanearea.getIntervalVehicleNumber(
        'shoutinanlu_N2S_5')  # 车辆数，时间间隔
    e2_jam_len_max_interval = traci.lanearea.getIntervalMaxJamLengthInMeters(
        'shoutinanlu_N2S_5')  # 最大拥堵长度，时间间隔

    e2_mean_speed_interval_last = traci.lanearea.getLastIntervalMeanSpeed(
        'shoutinanlu_N2S_5')  # 平均速度，上个时间间隔
    e2_occupancy_interval_last = traci.lanearea.getLastIntervalOccupancy(
        'shoutinanlu_N2S_5')  # 占有率，上个时间间隔
    e2_veh_num_interval_last = traci.lanearea.getLastIntervalVehicleNumber(
        'shoutinanlu_N2S_5')  # 车辆数，上个时间间隔
    e2_jam_len_max_interval_last = traci.lanearea.getLastIntervalMaxJamLengthInMeters(
        'shoutinanlu_N2S_5')  # 最大拥堵长度，上个时间间隔

    # E3
    e3_halting_num = traci.multientryexit.getLastStepHaltingNumber(
        '首体路整体')  # 停车次数
    e3_mean_speed = traci.multientryexit.getLastStepMeanSpeed('首体路整体')  # 平均速度
    e3_occupancy = traci.multientryexit.getLastStepVehicleNumber(
        '首体路整体')  # 车辆数

    e3_mean_halts_last_interval = traci.multientryexit.getLastIntervalMeanHaltsPerVehicle(
        '首体路整体')  # 平均停车次数
    e3_mean_time_loss_last_interval = traci.multientryexit.getLastIntervalMeanTimeLoss(
        '首体路整体')  # 平均时间损失
    e3_mean_travel_time_last_interval = traci.multientryexit.getLastIntervalMeanTravelTime(
        '首体路整体')  # 平均旅行时间
    e3_veh_num_last_interval = traci.multientryexit.getLastIntervalVehicleSum(
        '首体路整体')  # 车辆数
# 关闭仿真
traci.close()
