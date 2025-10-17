## ͣ��������

�½�һ��.add.xml�ļ���ͣ�������õĴ�������

```xml
<additional>
  <!-- StoppingPlaces -->
  <parkingArea id="ParkAreaA" lane="E2_1" startPos="250" endPos="300" roadsideCapacity="5" angle="45" length="30"/>
  <parkingArea id="ParkAreaB" lane="-E3_1" startPos="240" endPos="460" roadsideCapacity="0" width="105" length="120" angle="30">
    <space x="-450" y="20" width="4" length="8" angle="120"/>
    <space x="-450" y="30" width="4" length="8" angle="120"/>
    <space x="-250" y="20"/>
  </parkingArea>
</additional>
```

����˵����
- idΪͣ�������ţ��������ơ�
- laneΪͣ�������ڵĵ�·
- startPos��endPosΪͣ�������ڵ�·�Ŀ�ʼλ�������λ�á�
- roadsideCapacityΪ·��ͣ��ͣ������������
- width��lengthΪͣ�����ĳ�����������ú��ʵ���ֵ��
- angleΪͣ����б�ǣ���ȡ30��45��60��

����Ƕ��ͣ��������idΪParkAreaA�Ĳ������ü��ɣ������������ͼ

<img src="���ͣ��������.png" width=50% align=top>


�������һ������ͣ��������Ҫ����idΪParkAreaB�����÷���

```python
<parkingArea id="ParkAreaB" lane="-E3_1" startPos="240" endPos="460" roadsideCapacity="0" width="105" length="120" angle="30">
```

����Ķ�����ͣ����Χ�Ļ������������Ĵ�Сͣ������Ӧ���ڴ˷�Χ��,���Ҵ�ͣ����Ҳֻ��ͣһ����
�������Ҫ����С��ͣ��������������д��

```python
<space x="-450" y="30" width="4" length="8" angle="120"/>
```

��ͣ�����Ľ�����������д��

```python
<space x="-250" y="20"/>
```

�������ͼ

<img src="����ͣ��������.png" width=50% align=top>

## ����ͣ�����ĳ���������

��ͣ�����Ѿ������õĻ���֮����Ҫ���ؽ���ͣ�����ĳ���

�½�.flow.xml�ļ�,��������

```xml
<routes>
	<vehicle id="p0" depart="0">
    <route edges="E2 -E1"/>
    <stop parkingArea="ParkAreaA" duration="120"/>
	</vehicle>
	<vehicle id="p1" depart="0">
    <route edges="E2 -E3"/>
    <stop parkingArea="ParkAreaB" duration="120"/>
	</vehicle>
	<flow id="pp0" from="E2" begin="0" end="7200" period="100">
		<stop parkingArea="ParkAreaA" duration="120"/>
	</flow>
	<flow id="pp1" from="E2" begin="0" end="7200" period="100">
		<stop parkingArea="ParkAreaB" duration="120"/>
	</flow>
</routes>
```

vehicle����������ͣ�
- route egdesΪ�����ߵ�Ŀ���
- stop parkingAreaΪͣ����ͣ����id
- durationΪͣ��ʱ��

flow����������ͣ�
- fromΪ������
- begin��endΪ����ʱ��
- periodΪ�೤ʱ�䷢һ��Ҫͣ���ĳ�

���֮����Կ�������ͣ��ͣ�����ڣ�����ͼ

<img src="ͣ�����.png" width=50% align=top>
