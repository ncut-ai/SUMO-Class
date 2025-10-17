#教育机构：
#开发时间：2022/7/21 10:23

import numpy as np
from xml.sax import parse, handler

class DetectorParse(handler.ContentHandler):
    def __init__(self):
        self.lanes = {}
    def startElement(self, name, attrs):
        if name == 'interval':
            det_id = attrs['id']
            lane_id = det_id[0:]
            if lane_id not in self.lanes:
                self.lanes[lane_id] = {}
                self.lanes[lane_id]['speed'] = []
            if float(attrs['end']) < 3600:
                self.lanes[lane_id]['speed'].append(
                    float(attrs['meanSpeed'])
                )
    def endDocument(self):
        print(self.lanes)
if (__name__ == "__main__"):
    detector_output = DetectorParse()
    parse('.\\OUTPUT-E2.xml', detector_output)

    c=12
    list=[]
    for key, value in detector_output.lanes.items():
        a=np.mean(value['speed'])
        list.append(a)

    print(sum(list)/c)

