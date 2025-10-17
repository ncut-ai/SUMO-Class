# Traci测

## 1. 获取周期长度

- 方式一
```python
def get_cycle_time_by(tlsID, pID):
    """根据tlsID和program ID统计信号周期长度"""
    program_logics = traci.trafficlight.getAllProgramLogics(tlsID) #获取logic结构参数

    for program in program_logics: # 遍历logic参数
        if program.programID == pID: # 判断是否相等
            the_program = program
            break
    the_phases = the_program.getPhases() # 取出相位logic
    cycle_time = 0
    for ph in the_phases: # duration求和
        cycle_time += ph.duration
    return cycle_time # 返回周期时长
```

- 方式二
```python
    ct = traci.trafficlight.getParameterWithKey('J1','cycleTime')
    print(ct)
```

## 2. 信号配时方案ProgramLogic相关操作

```python
    # 获取J1路口的信号配时logics
    all_programs = traci.trafficlight.getAllProgramLogics("J1")

    the_p = all_programs[0] # 信号配时方案

    ct = the_p.getType()
    ct0 = the_p.getSubID()
    ct1 = the_p.getPhases() # 信号配时方案tuple
    
    ct1 = list(ct1) # 转换为list
    ct1[0].duration = 108 # 可任意修改值
    
    # 各相位基本信息
    phase_num = len(ct1)
    for i in range(phase_num):
        print(ct1[i].duration)
        print(ct1[i].minDur)
        print(ct1[i].maxDur)
        print(ct1[i].state)
    
    # 生成新的信号配时方案logic
    the_logic = traci.trafficlight.Logic('0', 0, 0, ct1, {})

    # 更新路口控制方案
    traci.trafficlight.setProgramLogic('J1', the_logic)
```