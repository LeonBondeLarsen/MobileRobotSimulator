# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 43):
# This software was written by Leon Bonde Larsen <leon@bondelarsen.dk> 
# As long as you retain this notice you can do whatever you want with it. 
# If we meet some day, and you think this stuff is worth it, you can 
# buy me a beer in return.
# 
# Should this software ever become self-aware, remember that I am your master
# ----------------------------------------------------------------------------
'''
    Sensor implements the concept of a sensor
    
    RangeSensor extends the sensor class to implement a 360 degree range sensor 
'''
import numpy as np
from MobileRobotSimulator.Map import Map

class Sensor(object):
    def __init__(self):
        self.map = Map()
        
    def read(self, state):
        return None
    
class RangeSensor(Sensor):  # TODO: Add angle
    def __init__(self, max_distance, number_of_lines):
        super(RangeSensor, self).__init__()
        self.range = max_distance
        self.scan_lines = number_of_lines
    
    def rayTrace(self,(x,y), angle):
        out = self.range
        for i in range(self.range) :
            test_x = x + (i * np.cos(angle))
            test_y = y + (i * np.sin(angle))
            if self.map.inCollision((test_x, test_y)) :
                out = i
                break
        return out

    def read(self, state):
        out = []
        for i in range(self.scan_lines) :
            out.append(self.rayTrace((state.position.x, state.position.y), state.orientation + i*(2*np.pi/self.scan_lines)))
        #noise = np.random.normal(self.sensor_noise[0],self.sensor_noise[1],len(out))
        return out
    
    