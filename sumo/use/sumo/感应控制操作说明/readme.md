# ��Ӧ���Ʒ������

�½�.add.xml�ļ�����������

```xml
<additional>
    <tlLogic id="J7" type="actuated" programID="pid010" offset="0">
        <param key="max-gap" value="50.0"/>
        <param key="detector-gap" value="15.0"/>
        <param key="passing-time" value="2.0"/>
        <param key="vTypes" value=""/>
        <param key="show-detectors" value="true"/>
        <param key="file" value="tsl-actuated-output.xml"/>
        <param key="freq" value="300"/>
        <param key="jam-threshold" value="100"/>
        <param key="detector-length" value="350"/>

        <phase duration="50" name="�ϱ�ֱ��"         state="gGrgrrgGrgrr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="�Ƶƣ��ϱ�ֱ�У�"  state="gyrgrrgyrgrr"   />
        <phase duration="1"  name="ȫ�죨�ϱ�ֱ�У�"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="�ϱ���ת"         state="grGgrrgrGgrr"   minDur="10" maxDur="50"/>
        <phase duration="3"  name="�Ƶƣ��ϱ���ת��"  state="grygrrgrygrr"   />
        <phase duration="1"  name="ȫ�죨�ϱ���ת��"  state="rrrrrrrrrrrr"   />
        <phase duration="50" name="����ֱ��"         state="grrgGrgrrgGr"   minDur="15" maxDur="90"/>
        <phase duration="3"  name="�Ƶƣ�����ֱ�У�"  state="grrgyrgrrgyr"   />
        <phase duration="1"  name="ȫ�죨����ֱ�У�"  state="rrrrrrrrrrrr"   />
        <phase duration="20" name="������ת"         state="grrgrGgrrgrG"   minDur="10" maxDur="50"/>
        <phase duration="3"  name="�Ƶƣ�������ת��"  state="grrgrygrrgry"   />
        <phase duration="1"  name="ȫ�죨������ת��"  state="rrrrrrrrrrrr"   />
    </tlLogic>
</additional>

```

�������ͣ�

- tlLogic id��programIDΪ���ţ���������

- typeΪ��ͨ�źŵƿ������ͣ��У�static(�̶���ʱ),actuated(��Ӧ����),delay_based(����ʱ����ʧ����)

- offsetΪ��λ��

- max-gapΪ���µ�ǰ�׶��ӳ�����������֮������ʱ����(���ͷʱ��)
- detector-gapΪ���µ�ǰ��λ�ӳ�����������֮������ʱ����������(�Զ����ɵ�)�������ͣ����֮���ʱ�����(����Ϊ��λ)
- passing-timeΪ����ʱ���������ʱʱ�䲻�㣬�������warning
- ���ڸ�Ӧ�����ǻ���E1��������п��ƣ�vTypes��file,freq�ɲ������壬������E1������Ķ����ж��弴��
- show-detectorsΪ�Ƿ���sumo-gui�пɿ��������
- jam-thresholdΪ�������λ�ڼ�����ϣ�ͨ��·�ڱȸ�����ʱ��������ɺ�����Щ����
- detector-lengthΪ���������������Ϊ������ֵ����ȷ���ڲ�ͬ��϶�ͳ���λ���½����Ƚ���������

��λ���ã�
��λ����netedit�����ã���ͼ��ʾ��

<img src="netedit��Ӧ��������.png" width=50% align=top>

�ȵ�����̵ƴ���ģʽ��Ȼ��ѡ������Ϊactuated��Ȼ�����·������������С��ʱ��

Ҳ�������ϴ�����ʾ����.add.xml������
