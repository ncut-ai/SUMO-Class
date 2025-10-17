# 智能车添加

智能车添加是在.flow.xml文件中实现的

原来车辆定义：
```python
<vType id="t02" vClass="truck"  probability="0.1" accel="2.6" decel="4.5" sigma="0.5" laneChangeModel="LC2013" maxSpeed="40" color="1,1,0" minGap="2.5"/>
```

在车辆类型定义中添加如下代码：

```python
carFollowModel="IDMM"
```

智能车模型有IDM,IDMM,EIDM，根据需求更改即可