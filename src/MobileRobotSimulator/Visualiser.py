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
    Posterior implements the concept of posterior over an agents states
    
    Visualiser interfaces the MobileRobotSimulator to pyplot
'''
import numpy as np
import matplotlib.cm as cm
from matplotlib import pyplot as plt
from MobileRobotSimulator.Map import Map

class Posterior(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.agent_type = 'r'
    
    def push(self, x, y, agent_type):
        self.x.append(x)
        self.y.append(y)
        self.agent_type = agent_type

class Visualiser(object):
    def __init__(self):
        self.map = Map()
        plt.ion()
        self.figure = plt.figure(num='Robot simulator', figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
        self.figure.canvas.draw()
        self.agent_posteriors = []
        self.sensors_x = []
        self.sensors_y = []
    
    def plotAgent(self, index, agent):
        while len(self.agent_posteriors) <= index:
            self.agent_posteriors.append(Posterior())
        
        self.agent_posteriors[index].push(agent.state.position.x, agent.state.position.y, agent.type)
        self.figure.gca().plot(agent.state.position.x, agent.state.position.y, agent.type+'o')
        self.plotSensor(agent)
        
    def resetAgentPosterior(self, index):
        while len(self.agent_posteriors) <= index:
            self.agent_posteriors.append(Posterior())
        self.agent_posteriors[index] = Posterior()
    
    def plotSensor(self, agent):
        for i in range(agent.sensor.range) :
            self.sensors_x.append( agent.state.position.x  + (i * np.cos(agent.state.orientation + agent.sensor.scan_angles[0])) )
            self.sensors_y.append( agent.state.position.y + (i * np.sin(agent.state.orientation+ agent.sensor.scan_angles[0])) )       
            self.sensors_x.append( agent.state.position.x  + (i * np.cos(agent.state.orientation + agent.sensor.scan_angles[1])) )
            self.sensors_y.append( agent.state.position.y + (i * np.sin(agent.state.orientation+ agent.sensor.scan_angles[1])) )       
        
        
    def draw(self):
        for agent_index in range(len(self.agent_posteriors)):
            self.figure.gca().plot(self.agent_posteriors[agent_index].x, self.agent_posteriors[agent_index].y,self.agent_posteriors[agent_index].agent_type)
        self.figure.gca().plot(self.sensors_x, self.sensors_y,',k')
        self.figure.canvas.draw()
        self.figure.clf()
        self.figure.gca().imshow(self.map.image, cmap = cm.Greys_r)
        self.sensors_x = []
        self.sensors_y = []
        