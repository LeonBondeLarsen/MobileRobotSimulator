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
    NormalDistribution is a convenience structure to hold mean and variance
    
    Position is a convenience structure for holding position data
    
    Velocity is a convenience structure for holding velocity data
    
    State implements the concept of agent state consisting of position, orientation and velocities
    
    Agent implements the concept of an agent combining sensors with controller and extrapolating state
'''
import numpy as np
from MobileRobotSimulator.Map import Map
from MobileRobotSimulator.Sensors import Sensor
from MobileRobotSimulator.Controllers import Controller

class NormalDistribution(object):
    def __init__(self, mean=0, variance=0.1):
        self.mean = mean
        self.variance = variance
        
class Position(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity(object):
    def __init__(self, lin=0, ang=0):
        self.linear = lin
        self.angular = ang

class State(object):
    def __init__(self, x=0, y=0, orientation=0, linear=0, angular=0):
        self.position = Position(x,y)
        self.orientation = orientation
        self.velocity = Velocity(linear, angular)

class Agent(object):
    def __init__(self, x=60, y=60, orientation=0, linear=1, angular=0, agent_color='r'):
        self.state = State(x, y, orientation, linear, angular)
        self.map = Map()
        self.pixels_per_meter = 20  # TODO: Make mutator or include in constructor
        self.type = agent_color
        self.sensor = Sensor()
        self.controller = Controller()
        self.sensor_noise = NormalDistribution()
        self.actuator_noise = NormalDistribution()

    def update(self):
        perception = self.sensor.read(self.state)
        noise = np.random.normal(self.sensor_noise.mean,self.sensor_noise.variance,len(perception))
        self.controller.setPerception( perception + noise )

        noise = np.random.normal(self.actuator_noise.mean,self.actuator_noise.variance,2)
        (self.state.velocity.linear,self.state.velocity.angular) = self.controller.getAction() + noise
        
        
        
        