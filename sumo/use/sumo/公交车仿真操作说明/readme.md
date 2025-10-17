# �������������

## ������վ����

�����ù���������֮ǰ��Ҫ�Ƚ���������վ���½�һ��.add.xml�ļ�,����������ʾ

```xml
<additional>
    <!-- StoppingPlaces -->
    <busStop id="station1" lane="-E5_1" startPos="120.00" endPos="140.00">
        <access lane="-E5_1" pos="130.00"/>
    </busStop>
    <busStop id="station2" lane="E3_1" startPos="120.00" endPos="140.00">
        <access lane="E3_1" pos="130.00"/>
    </busStop>
    <busStop id="station3" lane="E4_1" startPos="120.00" endPos="140.00">
        <access lane="E4_1" pos="130.00"/>
    </busStop>
    <busStop id="station4" lane="E5_1" startPos="904.00" endPos="924.00">
        <access lane="E5_1" pos="914.00"/>
    </busStop>
    <busStop id="station5" lane="-E3_1" startPos="173.00" endPos="193.00">
        <access lane="-E3_1" pos="183.00"/>
    </busStop>
    <busStop id="station6" lane="-E4_1" startPos="730.00" endPos="750.00">
        <access lane="-E4_1" pos="740.00"/>
    </busStop>
</additional>
```

�������ͣ�
- idΪ���ţ��������ơ�
- laneΪ������վ���õĳ���λ�á�
- startPosΪ������վ��ʼλ�ã�endPosΪ������վ����λ�á�
- access laneΪ����������ĳ�����posΪ������ͣ����λ�á�
�����Լ�����������ü��ɡ�

������ɺ���ͼ��ʾ

<img src="������վ�������.png" width=50% align=top>

## �������������

���úù�����վ֮��������й������������
�½�һ��.flow.xml�ļ�����������

```xml

<routes>
	<!--������أ�������վ��.net.xml�ж���-->
	<vType id="BUS_A" personCapacity="40" personNumber="3" accel="2.6" decel="4.5" sigma="0" vClass="bus" length="12" minGap="3" maxSpeed="19" color="1,1,1" guiShape="bus"/>
	<vType id="BUS_B" personCapacity="40" personNumber="4" maxSpeed="8" vClass="bus" Length="14.63" guiShape="bus" />


    <flow id="brt1" color="1,1,1"  begin="0" end= "3600" period="300" line="bus_brt1" type="BUS_B" from="-E5" to="E4"> 
      <stop busStop="station1" duration="30"/>
    </flow>


    <flow id="brt2" color="1,1,0"  begin="0" end= "3600" period="300" line="bus_brt2" type="BUS_A" from="-E4" to="E5"> 
      <stop busStop="station2" duration="30"/>
    </flow>    

</routes>
```

���������Ͷ���������ͣ�
- idΪ���ţ��������ơ�
- personCapacityΪ����������������ޡ�
- personNumberΪ�Ѿ�ռ�ݵ�λ�ã����������������Ѿ��趨��ȡֵ��ΧΪ[0,personCapacity]��
- maxSpeedΪ����������ٶ�
- colorΪRGB��ɫѡ��
- LengthΪ�������������á�
- accel��decelΪ���ٶ�����ٶȡ�
- minGapΪ��С�������롣
- ���������������ͣ�����Ȥ�������˽⡣

�������������ɲ������ͣ�
- begin��endΪ����ʱ����
- periodΪ�೤ʱ�䷢һ�γ���
- lineΪ��������id���������ơ�
- colorΪRGB��ɫѡ��
- typeΪѡ��Ĺ��������ͣ�ʹ��֮ǰ������Ĺ��������͡�
- from to Ϊ�����ıߵ������ıߡ�
- busStopΪ������վid���������ơ�
- durationΪͣ��ʱ�䡣


����Ϊ���ɹ���������ȫ������,��ȷ����ͼʾ����

<img src="�������������ͣ��.png" width=50% align=top>