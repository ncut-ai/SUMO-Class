echo off
echo Let's Roll
@echo off
@echo please wait a minite...


Rem 注释...
::这也是注释。。。

Rem 生成网络-3种（grid网、spider网、随机网）
call="%SUMO_HOME%\bin\netgenerate" --grid --grid.number=4 --grid.length=400 --output-file=MySUMOFile_grid3.net.xml
::call = "%SUMO_HOME%\bin\netgenerate" --spider --spider.arm-number=10 --spider.circle-number=10 --spider.space-radius=100 --output-file=MySUMOFile_spider.net.xml
::call = "%SUMO_HOME%\bin\netgenerate" --rand -o MySUMOFile_rnd.net.xml --rand.iterations=200

Rem 根据路网生成随机路径
Python "%SUMO_HOME%\tools\randomTrips.py" -n MySUMOFile_grid3.net.xml -o map3.rou.xml -e 3600 -l

::Python "%SUMO_HOME%\tools\randomTrips.py" -n simpleTest.net.xml -o simpleTest.rou.xml -e 100 -l
pause