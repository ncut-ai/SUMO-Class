# ���˷���˵��

## ���е�����

<img src="���е�����ģ��ѡ��.png" width=50% align=top>

ѡ������೵������೵�������е��allow

<img src="����ѡ��.png" width=50% align=top>

�������֮�󣬽����г�����ֹͨ�У�ֻ��������

## ����������

<img src="����������.png" width=50% align=top>

�������֮��ѡ�����ð�����ģʽ���������㣬���Կ������г����߱�ɰ���ɫ����ͼ��ʾ

<img src="�����߳���ѡ��.png" width=50% align=top>

��������������Կ����������ɫ���ٵ��ͬһ����Ľ��ڳ��������»س������������ɻ�ɫ�����ߣ���ͼ��ʾ

<img src="����������.png" width=50% align=top>

�������ϲ����������ĸ�����İ����ߣ������ͬѧ���ְ��������ɱ�ɺ�ɫ�����ҳ������±����������·�ʽ��������ɰ�����û�������ͬѧ���Խ���������������

<img src="����ͼƬ.png" width=50% align=top>

�����ϴ����ͬѧ��Ҫ�ѻ���������������ȫ����Ϊ���˳��⣬ÿһ��������������Ҫ�޸ģ���ͼ��ʾ

<img src="������.png" width=50% align=top>

�޸�֮���ٴ����ɰ����߼���˳������

## ������������

���������赥���½�.add.xml�ļ�

�������¸�ʽ��д��
```xml
<routes>
<!-- ���� -->
    <!-- �Ͻ��� -->
	<personFlow id="p1" begin="0" end="3600" period="18">
       <walk from="S1" to="W1"/>
	   <walk from="S1" to="-N1"/>
	   <walk from="S1" to="-E1"/>
    </personFlow>
	<!-- ������ -->
	<personFlow id="p2" begin="0" end="3600" period="18">
       <walk from="N1" to="E1"/>
	   <walk from="N1" to="-S1"/>
	   <walk from="N1" to="-W1"/>
    </personFlow>
	<!-- ������ -->
	<personFlow id="p3" begin="0" end="3600" period="18">
       <walk from="W1" to="N1"/>
	   <walk from="W1" to="-E1"/>
	   <walk from="W1" to="-S1"/>
    </personFlow>
	<!-- ������ -->
	<personFlow id="p4" begin="0" end="3600" period="18">
       <walk from="E1" to="S1"/>
	   <walk from="E1" to="-W1"/>
	   <walk from="E1" to="-N1"/>
    </personFlow>
</routes>
```


����˵����
- idΪ��ţ��������ơ�
- begin��endΪ���濪ʼ�����ʱ�䣬���������ļ���һ�¡�
- periodΪʱ���������೤ʱ������һ���ˡ�
- walk from to ��Ϊ�����ı���Ŀ��ߡ�
����ʵ��·�ڵ������д����



ȫ������Ժ���.sumocfg�����ļ������fl_person.add.xml,�����´���
```python
<additional-files value="fl_person.add.xml"/>
```
