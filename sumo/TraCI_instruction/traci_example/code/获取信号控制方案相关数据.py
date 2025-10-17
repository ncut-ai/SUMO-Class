import os
import traci
import traci.constants as tc


os.chdir(os.path.dirname(__file__)) # 切换至当前文件所在目录

# 初始化仿真信息
sumoCmd = ["sumo", "-c", "../现状仿真/3.4晚高峰/4_zhangkai.sumocfg", '--start']
print(type(sumoCmd) )
# 启动仿真
traci.start(sumoCmd)

# 运行至仿真结束
while traci.simulation.getMinExpectedNumber() > 0:
   
   traci.simulationStep() # 执行一步仿真

   s_time = traci.simulation.getTime() # 当前仿真时间
   tls_ryg_state = traci.trafficlight.getRedYellowGreenState('J0') # J0路口当前相位的设置
   tls_phase_duation = traci.trafficlight.getPhaseDuration('J0') # J0当前相位时长
   tls_phase = traci.trafficlight.getPhase('J0') # 当前相位序号
   tls_program = traci.trafficlight.getProgram('J0') # 当前配时方案序号
   tls_next_switch = traci.trafficlight.getNextSwitch('J0') # J0下一个相位切换时间


   print(s_time) # 输出仿真时间
   print(f"J0信号配时方案： {tls_ryg_state}") 
   print(f"J0当前相位时长： {tls_phase_duation}") 
   print(f"J0当前相位： {tls_phase}") 
   print(f"J0当前信号配时方案： {tls_program}") 
   print(f"J0下一相位切换时间： {tls_next_switch}") 

   tls_phase_passed = s_time - (tls_next_switch - tls_phase_duation) # J0当前相位已执行时间 = 当前仿真时间 - (J0下一相位切换时间 - J0当前相位时长)
   tls_phase_remain = tls_phase_duation - tls_phase_passed # J0当前相位剩余时间 = J0当前相位时长 - J0当前相位已执行时间

   print(f"J0当前相位已执行时间： {tls_phase_passed}") 
   print(f"J0当前相位剩余时间： {tls_phase_remain}") 

   tls_cycle_time = traci.trafficlight.getParameter('J0', 'cycleTime') # J0周期长度
   print(f"周期长度：{tls_cycle_time}")
   tls_cycle_second = traci.trafficlight.getParameter('J0', 'cycleSecond') # 周期内的时间
   print(f"周期内的执行时间：{tls_cycle_second}")
   tls_offset = traci.trafficlight.getParameter('J0', 'offset') # 相位差
   print(f"相位差：{tls_offset}")
   tls_type = traci.trafficlight.getParameter('J0', 'typeName') # 控制类型
   print(f"控制类型：{tls_type}")

# 关闭仿真
traci.close()
