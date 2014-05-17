'''
Created on Apr 20, 2014

@author: leon

agent colors:
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
'''
from MobileRobotSimulator import Environment, Agent, NeuralNetwork, RangeSensor

def sevenAgentTest():
    environment = Environment()
    
    agent1 = Agent(60,50,0.0,2,0,'r')
    agent1.controller = NeuralNetwork()
    agent1.sensor = RangeSensor(25,9)
    environment.agents.append( agent1 )
    
    agent2 = Agent(60,50,0.0,2,0,'g')
    agent2.controller = NeuralNetwork()
    agent2.sensor = RangeSensor(25,9)
    environment.agents.append( agent2 )
    
    agent3 = Agent(60,70,1.0,2,0,'b')
    agent3.controller = NeuralNetwork()
    agent3.sensor = RangeSensor(25,9)
    environment.agents.append( agent3 )
    
    agent4 = Agent(60,80,1.5,2,0,'c')
    agent4.controller = NeuralNetwork()
    agent4.sensor = RangeSensor(25,9)
    environment.agents.append( agent4 )
    
    agent5 = Agent(60,90,2.0,2,0,'m')
    agent5.controller = NeuralNetwork()
    agent5.sensor = RangeSensor(25,9)
    environment.agents.append( agent5 )
    
    agent6 = Agent(60,100,2.5,2,0,'y')
    agent6.controller = NeuralNetwork()
    agent6.sensor = RangeSensor(25,9)
    environment.agents.append( agent6 )
    
    agent7 = Agent(60,110,3.0,2,0,'k')
    agent7.controller = NeuralNetwork()
    agent7.sensor = RangeSensor(25,9)
    environment.agents.append( agent7 )
    
    environment.run(1500)
    
sevenAgentTest()