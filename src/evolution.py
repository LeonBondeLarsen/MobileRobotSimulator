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
    Convenience functions for evolutionary programming
'''
import numpy as np
from MobileRobotSimulator import Agent, NeuralNetwork, RangeSensor

def spawnAgent(color, sensor_range, angles, gain):
    out = Agent(2,0,color)
    out.controller = NeuralNetwork(gain)
    out.sensor = RangeSensor(sensor_range, 2, angles)
    return out

def generateRandomAgent(color):
    sensor_range = np.random.randint(0,41) + 10 # Range 10;50
    angles = np.random.rand(2) * [-np.pi, np.pi]
    gain = np.random.rand(3) * [0.1, 1, -1] # Range 0;0.1, 0;1, 0;-1
    return spawnAgent(color, sensor_range, angles, gain)

def getMutated(color, agent):
    random_percentage = np.random.rand() * 100
    sensor_range = agent.getSensorRange()
    sensor1_angle = agent.getSensor1()
    sensor2_angle = agent.getSensor2()
    gain = agent.getGain()
    
    if(random_percentage < 10):
        sensor_range += np.random.randint(-1,2)
    elif(random_percentage < 20):
        sensor1_angle += (np.random.rand() - 0.5) / 10
    elif(random_percentage < 30):
        sensor2_angle += (np.random.rand() - 0.5) / 10
    elif(random_percentage < 40):
        gain[0] += (np.random.rand() - 0.5) / 10
    elif(random_percentage < 50):
        gain[1] += (np.random.rand() - 0.5) / 5
    elif(random_percentage < 60):
        gain[1] += (np.random.rand() - 0.5) / 5
    elif(random_percentage < 80):
        sensor_range = np.random.randint(0,41) + 10 # Range 10;50
        sensor1_angle, sensor2_angle = np.random.rand(2) * [-np.pi, np.pi]
        gain = np.random.rand(3) * [0.1, 1, -1] # Range 0;0.1, 0;1, 0;-1
    return spawnAgent(color, sensor_range, [sensor1_angle, sensor2_angle], gain)

def runGenerationTrial(environment, turns):
    # Save start positions
    start_positions = []
    for i in range(len(environment.agents)):
        start_positions.append([environment.agents[i].state.position.x, environment.agents[i].state.position.y]) 
    
    # Run some trials
    collisions = []
    for i in range(turns):
        collisions.append( environment.takeStep() )
    collisions = sum(collisions,[])
    
    # Save end positions
    end_positions = []
    for i in range(len(environment.agents)):
        end_positions.append([environment.agents[i].state.position.x, environment.agents[i].state.position.y]) 
        
    # Calculate straight line distance traveled
    distance = []
    for i in range(len(start_positions)):
        distance.append(np.sqrt( (end_positions[i][0] - start_positions[i][0])**2 + (end_positions[i][1] - start_positions[i][1])**2 ))
    
    # Count turns in collision
    collision_count = []
    for i in range(len(environment.agents)):
        collision_count.append( collisions.count(i) )
        
    return distance, collision_count