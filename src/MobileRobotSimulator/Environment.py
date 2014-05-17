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
    Environment implements the concept of an environment aggregating map, agents and visualiser. 
'''
import numpy as np
from MobileRobotSimulator.Map import Map
from MobileRobotSimulator.Visualiser import Visualiser

class Environment(object):
    def __init__(self):
        self.map = Map()
        self.agents = []
        self.visualiser = Visualiser()
        self.visualise = True
        self.stepsize = 0.1 # TODO: magic number...
    
    def setSensorNoise(self, mean, variance):
        self.sensor_noise.mean = mean
        self.sensor_noise.variance = variance
    
    def setActuatorNoise(self, mean, variance):
        self.actuator_noise.mean = mean
        self.actuator_noise.variance = variance

    def takeStep(self):
        for agent_index in range(len(self.agents)):
            self.agents[agent_index].update()
            if not self.map.inCollision((self.agents[agent_index].state.position.x, self.agents[agent_index].state.position.y)) :
                if not self.agentCollision(agent_index) :
                    self.agents[agent_index].state.position.x = self.agents[agent_index].state.position.x + ( self.agents[agent_index].state.velocity.linear * np.cos(self.agents[agent_index].state.orientation) * self.stepsize * self.agents[agent_index].pixels_per_meter)
                    self.agents[agent_index].state.position.y = self.agents[agent_index].state.position.y + ( self.agents[agent_index].state.velocity.linear * np.sin(self.agents[agent_index].state.orientation) * self.stepsize * self.agents[agent_index].pixels_per_meter)
                    self.agents[agent_index].state.orientation = self.agents[agent_index].state.orientation + (self.agents[agent_index].state.velocity.angular * self.stepsize)
            if self.visualise :
                self.visualiser.plotAgent(agent_index, self.agents[agent_index])
        self.visualiser.draw()
    
    def run(self, max_iterations):
        iterations = 0
        while iterations < max_iterations :
            iterations += 1
            self.takeStep()
        self.visualiser.figure.savefig('last_run.png')
        print 'Completed ' + str(iterations) + ' iterations'
        
    def agentCollision(self, index):  
        out = False       
        for agent_index in range(len(self.agents)):
            if agent_index != index:
                if np.abs(self.agents[agent_index].state.position.x - self.agents[index].state.position.x) < 5 and np.abs(self.agents[agent_index].state.position.y - self.agents[index].state.position.x) < 5 :
                    out = True
        return out
        