# ���˻���

�½�һ��.flow.xml�ļ�����������

```xml
<routes>
  <personFlow id="person0" depart="0" number="400">
    <walk from="E2" busStop="station5" arrivalPos="random"/>
    <ride busStop="station2" lines="bus_test"/>
    <walk to="-E0" arrivalPos="random"/>
    <walk from="-E0" trainStop="ts_2" arrivalPos="random"/>
    <ride trainStop="ts_2" lines="K405"/>
  </personFlow>
  <personFlow id="person1" depart="1" number="1000">
    <walk from="Eperson"  trainStop="ts_1" arrivalPos="random"/>
    <ride trainStop="ts_3" lines="train_test"/>
    <walk to="E2" busStop="station4" arrivalPos="random"/>
    <ride busStop="station4" lines="bus_test"/>
    <walk to="-E0" arrivalPos="random"/>
  </personFlow>
</routes>
```

�������ͣ�

idΪ���ţ���������
departΪ����������·����ʱ�䲽��
numberΪ������������
arrivalPosΪ���﷽ʽ����ѡrandom,best,free��

```python
walk from="E2" busStop="station5
```

Ϊ��������E2���ɣ���E2����������idΪstation5�Ĺ�����վ

```python
ride busStop="station2" lines="bus_test"
```

Ϊ���˴�˹�����������idΪbus_test��lines�ĵ�·����󵽴�idΪstation2�Ĺ�����վ��

```python
walk to="-E0" arrivalPos="random"
```

������idΪstation2�Ĺ�����վ�³���station2��-E0�ϣ���󵽴�ı�Ϊ-E0�����﷽ʽ���

```python
walk from="-E0" trainStop="ts_2" arrivalPos="random"
```

���˴�-E0����������idΪts_2�Ļ�վ(trainStop),���﷽ʽ���

```python
ride trainStop="ts_2" lines="K405"
```

������ts_2��վ��˻�����idΪK405��lines(·��)ǰ��

Ч�����ͼ����:

<img src="���˻������1.png" width=50% align=top>

---


<img src="���˻������2.png" width=50% align=top>