# 交通仿真技术课程设计

## A. 课程简介

本课程为专业教育实践选修课，课时为1周（32学时），开设于本科阶段短2学期，是交通仿真类的设计与实践性课程，课程的主要任务是综合运用交通仿真技术的基础理论和仿真软件（VISSIM或SUMO）的实践基础，针对典型干线进行单交叉口信号配时设计、干线协调设计，掌握VISSIM或SUMO仿真软件的信号控制设计方法，提高对微观交通仿真软件的综合应用能力。考核方式包括课程设计过程及完成情况50%，设计报告50%。

### 课程目标

根据智慧交通专业、交通设备与控制工程专业毕业要求指标点，本课程设置了3个课程知识能力目标（简称：PTST-X）：“PTST-1 目标1： 理解课程任务，并设计实验流程完成数据准备”、“PTST-2 目标2： 熟练运用仿真软件实现仿真建模及数据分析”、“PTST-3 目标3： 掌握优化方案设计方法，能够实现优化方案比选”。另根据教育部和学校要求，课程设置了2个素质目标，不做输出目标考核。

- PTST-1 目标1： 理解课程任务，并设计实验流程完成数据准备

根据课程资料，分析设计任务需求，选择任务题目，设计并实现交通仿真建模与优化，建立协作团队，明确成员分工。在交通仿真技术课程设计开题、结组、完成任务、验收与报告各阶段能够按时间节点要求 积极主动完成任务。积极参与团队组建和讨论，承担团队分工任务（团队行为）。在选定任务工作过程中形成协作团队，明确分工，共同分析任务要求、收集 完成任务所需资料、在工作日志中如实记录各人工作任务及工作成果（团队成 果）。能够进行交通数据调查获取问题分析及交通仿真所需的基础数据，能够进行交通问题分析。

- PTST-2 目标2： 熟练运用仿真软件实现仿真建模及数据分析

针对所选题目，理解交通仿真基本理论，熟练掌握交通仿真技术的基本要素和步骤；掌握软件建模与参数调整技术，完成满足精度要求的交通仿真建模、分析工作。

- PTST-3 目标3： 掌握优化方案设计方法，能够实现优化方案比选

理解影响交通通行效率的因素，运用仿真软件针对交通问题实现仿真建模且满足精度要求，能够进行交通问题分析并在此基础上设计优化方案；能够解决仿真建模过程中的常见问题，通过参数调整提高仿真模型精度和运行稳定性。掌握专业文档写作技巧、团队分工协作，完成立项表、工作日志、研究报告、 成果展示 PPT 等报告文件。在任务演示验收中，用精练、专业的语言阐述项目 的工作目标、工作过程及设计成果。准确回答验收过程中的质疑。

- PTST-4目标4：建立科学世界观
- PTST-5目标5：建立符合社会主义道德要求的价值观

课程思政目标：结合课程特点，挖掘丰富的思政教育案例，潜移默化地实现对学生的思想政治教育，促进学习过程与方法、科学素养与价值引领的统一，坚定理想信念、厚植爱国主义情怀、加强品德修养，培育学生科学精神、创新精神、工匠精神，充分发挥专业课教学的育人功能。

### 课程考核方案

本课程总评成绩由平时成绩和报告考核成绩两部分构成。平时成绩比例 50%。

- 课程考核成绩构成

	- 验机与质询	40%	
	- 	考勤	10%	
	- 报告成绩（50%） 	

- 课程目标与考核方式的关系

	- 本课程指标点	课程目标	考核方式	总评考核成绩中的占比
	- 			报告	考勤与团队	验机
	- 4研究	PTST-1	报告、验机 (50%)	5%	-	5%
	- 	PTST-2		10%		5%
	- 5 使用现代工具	PTST-2	报告、验机 (40%)	10%	-	5%
	- 	PTST-3		5%		5%
	- 11 项目管理	PTST-1	考勤与团队 (10%)	-	5%	-
		PTST-3			5%	
	- 合 计	期末考试100%	50%	10%	40%

## B. 课程实践内容

### 1. 交通调查与仿真建模

#### 1.1 实践内容

- 选取路口（单交叉口、主干路、路网）
- 完成交通调查（静态数据、动态数据）
- 进行现状仿真建模（Vissim或SUMO）
- 优化方案设计（不少于两套）
- 仿真结果对比分析

#### 1.2 实践要求

- 3-5人/组
- 注意交通安全
- [参考示例文档](./resources/清河桥下路口仿真优化报告(简).doc)

#### 1.3 报告大纲

- 1、基本情况介绍（地理位置描述、静态几何调查数据、动态交通调查数据）
- 2、现状仿真及结果说明（建模结果，仿真精度等）
- 3、优化方案设计（明确设计方案，说明设计思路）
- 4、仿真优化对比分析（优化方案SUMO仿真结果，与现状仿真结果对比，结果说明分析）
- 5、TraCI二次开发应用（可选）（使用Python通过TraCI接口实现某种复杂功能）

### 2. SUMO仿真参数分析

#### 2.1 实践流程

- 选取SUMO模型（自建模型、备选模型）
- 选取参数范围
- 确定参数取值
- 设计实验方案
- 实验结果分析

#### 2.2 实践方向

##### 2.2.1 不同跟驰模型对仿真性能的影响
- 选取参数范围：跟驰模型（[参考资料链接](https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#car-following_models)）
- 对比以下跟驰模型：Krauss、KraussOrig1、PWagner2009、KraussPS、KraussAB、SmartSK、Wiedemann、W99、Daniel1、ACC、CACC
- 修改模型
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  carFollowModel="Krauss" maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     carFollowModel="Krauss" maxSpeed="11" color="1,0,0"/>
</routes>
```
##### 2.2.2 不同换道模型对仿真性能的影响
- 选取参数范围：换道模型（[参考资料链接](https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#lane-changing_models)）
- 对比以下换道模型：LC2013、SL2015、DK2008
- 修改仿真参数：
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  laneChangeModel="LC2013" maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     laneChangeModel="LC2013" maxSpeed="11" color="1,0,0"/>
</routes>
```

##### 2.2.3 SUMO仿真平台跟驰模型参数影响分析

- 选取跟驰模型：Krauss、KraussOrig1、PWagner2009、KraussPS、KraussAB、SmartSK、Wiedemann、W99、Daniel1、ACC、CACC。
- 选取跟驰模型参数（不少于3个）：minGap、accel、decel、speedTable、startupDelay、sigma、tau……。
- 修改模型
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  carFollowModel="Krauss" minGap="2.5" accel="2.6" maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     carFollowModel="Krauss" minGap="2.5" accel="2.6" maxSpeed="11" color="1,0,0"/>
</routes>
```

##### 2.2.4 SUMO仿真平台换道模型参数影响分析

- 选择换道模型：LC2013、SL2015、DK2008
- 选择换道模型参数（不少于3个）：lcStrategic、lcCooperative、lcSpeedGain、lcKeepRight、lcStrategicLookahead、lcCooperativeSpeed、minGapLat、lcImpatience、lcTimeToImpatience……。
- 修改模型示例
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  laneChangeModel="LC2013" lcStrategic="1.0" lcCooperative="1.0" maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     laneChangeModel="LC2013" lcStrategic="1.0" lcCooperative="1.0" maxSpeed="11" color="1,0,0"/>
</routes>
```

#### 2.3 报告大纲
- 1、实验目的和意义
	- 简述实验的主要范围和实验基础条件，详细描述实验的主要内容、实验目标和意义。
- 2、实验参数说明
	- 结合实验目标与意义，对实验涉及到的参数进行详细介绍。
- 3、实验方案介绍
	- 实验环境简要介绍，实验方案说明，Python编程开发实现过程介绍。
- 4、实验结果对比分析
	- 根据SUMO仿真结果，进行实验结果绘图及对比分析说明。

### 3. 交叉口交通安全特性分析

#### 3.1 交叉口模型参数影响分析

- 交叉口模型参数，[参考资料链接](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html#junction_model_parameters)
- 模型参数选取：jmCrossingGap、jmIgnoreKeepClearTime、jmDriveAfterRedTime、jmDriveAfterYellowTime、jmDriveRedSpeed、jmIgnoreFoeProb、jmStoplineGap、jmAdvance、jmExtraGap、impatience……

- The parameters are set within the ```<vType>```:
```xml
<!-- vtype_def.xml文件 -->
<vType id="vt_car" jmDriveAfterRedTime="300" jmDriveRedSpeed="5.56"/>
```
- 对比指标：（见文件"output/data_collision.xml"）

#### 3.2 报告大纲
- 1、实验目的和意义
	- 简述实验的主要范围和实验基础条件，详细描述实验的主要内容、实验目标和意义。
- 2、实验参数说明
	- 结合实验目标与意义，对实验涉及到的参数进行详细介绍。
- 3、实验方案介绍
	- 实验环境简要介绍，实验方案说明，Python编程开发实现过程介绍。
- 4、实验结果对比分析
	- 根据SUMO仿真结果，进行实验结果绘图及对比分析说明。

### 4. 自动驾驶模型参数分析

#### 4.1 SUMO仿真平台自动驾驶模型对比分析

- 对比模型列表：IDM、IDMM、EIDM
- 对比不同渗透率：10%, 20%, 50%, 80%……
- （[参考资料链接](https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#car-following_models)）
- 修改模型示例：
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  carFollowModel="Krauss"  maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     carFollowModel="Krauss" maxSpeed="11" color="1,0,0"/>
<vType id="vt_cav"   vClass="passenger"  carFollowModel="IDM"  maxSpeed="15" color="1,1,1"/>
</routes>
```
```xml
<!-- vdistribution_def.xml文件 -->
<!-- 渗透率10% -->
<routes>
    <vTypeDistribution id="vtd_yuanlinlu_east_T1"  vTypes="vt_car vt_truck vt_cav" probabilities="0.813 0.087 0.100"/>
	……
```


#### 4.2 SUMO仿真平台自动驾驶模型参数影响分析

- 模型选取：IDM、IDMM、EIDM
- 不同渗透率：10%, 20%, 50%, 80%……
- 选择换道模型参数（不少于3个）：delta、stepping、adaptFactor、adaptTime、tpreview、tPersDrive、ccoolness、Mbegin……
- （[参考资料链接](https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#car-following_models)）
- 修改模型示例：
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  carFollowModel="Krauss"  maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     carFollowModel="Krauss" maxSpeed="11" color="1,0,0"/>
<vType id="vt_cav"   vClass="passenger"  carFollowModel="IDM"  delta="4" maxSpeed="15" color="1,1,1"/>
</routes>
```
```xml
<!-- vdistribution_def.xml文件 -->
<!-- 渗透率10% -->
<routes>
    <vTypeDistribution id="vtd_yuanlinlu_east_T1"  vTypes="vt_car vt_truck vt_cav" probabilities="0.813 0.087 0.100"/>
	……
```

#### 4.3 不同渗透率下的交通流特性仿真分析

- 选择自动驾驶模型：IDM、IDMM、EIDM
- 不同渗透率：10%, 20%, 50%, 80%……
- 修改模型示例：
```xml
<!-- vtype_def.xml文件 -->
<routes>
<vType id="vt_car"   vClass="passenger"  carFollowModel="Krauss"  maxSpeed="15" color="1,1,0"/>
<vType id="vt_truck" vClass="truck"     carFollowModel="Krauss" maxSpeed="11" color="1,0,0"/>
<vType id="vt_cav"   vClass="passenger"  carFollowModel="IDM"   maxSpeed="15" color="1,1,1"/>
</routes>
```
```xml
<!-- vdistribution_def.xml文件 -->
<!-- 渗透率10% -->
<routes>
    <vTypeDistribution id="vtd_yuanlinlu_east_T1"  vTypes="vt_car vt_truck vt_cav" probabilities="0.813 0.087 0.100"/>
	……
```

#### 4.4 报告大纲
- 1、实验目的和意义
	- 简述实验的主要范围和实验基础条件，详细描述实验的主要内容、实验目标和意义。
- 2、实验参数说明
	- 结合实验目标与意义，对实验涉及到的参数进行详细介绍。
- 3、实验方案介绍
	- 实验环境简要介绍，实验方案说明，Python编程开发实现过程介绍。
- 4、实验结果对比分析
	- 根据SUMO仿真结果，进行实验结果绘图及对比分析说明。

## C. 题目汇总

| 选题类型 | 实践内容 |
|------|----------|
| 1. 交通调查与仿真建模 | ×××路口交通组织优化仿真分析 |
| 2. SUMO仿真参数分析 | 1. 不同跟驰模型对仿真性能的影响 <br> 2. 不同换道模型对仿真性能的影响 <br> 3. SUMO仿真平台跟驰模型参数影响分析 <br> 4. SUMO仿真平台换道模型参数影响分析 |
| 3. 交叉口交通安全特性分析 | 1.交叉口模型参数影响分析 | 
| 4. 自动驾驶模型参数分析 | 1.SUMO仿真平台自动驾驶模型对比分析 <br> 2.SUMO仿真平台自动驾驶模型参数影响分析 <br> 3.不同渗透率下的交通流特性仿真分析|

## D. 课程资料

- [仿真教程](https://gitee.com/itsncut/trafficsimulation)
- [报告格式](./resources/报告（作业）模版.doc)
- [仿真输出数据说明](./resources/仿真输出数据说明.md)

- 仿真案例（sumo模型）
	- [Yuanlinlu仿真模型](./resources/Yuanlinlu仿真模型(SUMO).zip)
	- [亦庄荣华路仿真模型](./resources/亦庄荣华路sumo仿真.zip)
	- [首体南路现状仿真模型](./resources/首体南路现状仿真(SUMO).zip)

- [SUMO输出结果对比图绘制(python实现)](../sumo/仿真输出结果绘图/readme.md)