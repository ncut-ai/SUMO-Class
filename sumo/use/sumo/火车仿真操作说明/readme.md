# �𳵷������


## ����·����

����.net�ļ���ѡ�񴴽���·ģʽ������ͼ����

<img src="ģʽѡ��.png" width=50% align=top>

Ȼ����ѡ����ɽ����·�ĳ�����������ͼ�����е����ݽ���ѡ��

<img src="��·ͨ�г���ѡ��.png" width=50% align=top>

����·��Ҫ�󻭳��𳵹��������ͼ��Ϊ���

<img src="�𳵹���������.png" width=50% align=top>

## ��վ����

�½�һ��.add.xml�ļ�,��վ������������

```xml
<additional>
    <!-- StoppingPlaces -->
    <trainStop id="ts_4" name="���ƴ�վ" lane="E-R210_0" startPos="200.80" endPos="250.80" lines="K405">
        <access lane="E2_0" pos="100.00"/>
    </trainStop>
    <!-- Wires -->
    <tractionSubstation id="tr_0" pos="606.62,-85.88" voltage="600.00" currentLimit="400.00"/>
</additional>
```

��վ�������ͣ�
- id��name���Ǵ��ţ�����������ã��������ơ�
- laneΪ�𳵵�����
- startPos��endPosΪ��վ��ʼ�����λ��
- linesΪ��վ����
- access lane Ϊ�����������վ�ĵ�·��Ϊ���е��ĵ�·id
- posΪ�����������վ��λ�ã�����ʵ��������������˴���ȥ����վ

ǣ��������������ͣ�
- idΪ���ţ���������
- posΪ�����λ��
- voltageΪ���ṩ��ѹ��С
- currentLimitΪ���ṩ������С

���ļ���������п��ܻ�������´���
==Error: invalid byte '?' at position 2 of a 2-byte sequence==

��ͨ�����ļ�ͷ������´�����
```python
<?xml version="1.0" encoding="gbk"?>
```
��վ�ɹ���������ͼ��
<img src="��վ�������.png" width=50% align=top>

## ����������

�½�һ��.flow.xml�ļ�����������

```xml
<routes>
	<vType id="train_A" vClass="rail" carFollowModel="Rail"/>
	<vType id="train_B"  length="50" vClass="rail" />

  <flow id="trtype3" line="train_test" color="1,1,1"  begin="0" end= "7200" period="900" type="train_B" from="E-R111" to="E-R211"> 
      <stop trainStop="ts_1" duration="300"/>
      <stop trainStop="ts_3" duration="300"/>
  </flow>

</routes>
```
�������Ͳ�������:
- idΪ���ţ��������ơ�
- vclassΪsumo�г������͵��ࡣ
- carFollowModelΪ����ģ�ͣ�ѡ��Rail���ɡ�
- lengthΪ�������ȣ��������ü�ΪĬ��ֵ��

���������������ͣ�
- idΪ���ţ��������ơ�
- lineΪ����
- colorΪRGB��ɫ����������
- begin��endΪ����ʱ����periodΪ�೤ʱ�䷢һ�γ�
- typeѡ��һ��֮ǰ������Ļ����ͼ���
- from toΪ�����ıߵ�Ŀ���
- stop trainStopΪ��ͣ��վ,==˳�����Ⱥ��Ⱦ�����վ��ǰ����ͣ����վ�ں�==
- durationΪͣ��ʱ��


��ɺ�ɿ�����ͣ��������ͼ

<img src="��ͣ�����2.png" width=50% align=top>
