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
    Controller implements the concept of an agent controller mapping sensor data to motor output
    
    NeuralNetwork extends Controller to facilitate a 2-recurrent artificial neural network 
'''
import numpy as np

class Controller(object):
    def __init__(self):
        self.latest_sensor_data = []
        
    def setPerception(self, data):
        self.latest_sensor_data = data
        
    def getAction(self):
        return self.latest_motor_action
    
    def convertWheelSpeedsToTwist(self, (left, right)):
        return ((left + right) / 2, np.arctan2(right-left,1))
    
class NeuralNetwork(Controller):
    def __init__(self, gain=[0.05, 0.5, -0.9]):
        super(NeuralNetwork, self).__init__()
        self.prev_activation_n1 = 0.0
        self.prev_activation_n2 = 0.0  
        self.gain = gain
        
    def activationFunction(self, u):
        return (2/(1 + np.exp(-2*u)))-1
        #return u
    
    def getOutput(self, in1, in2):
        activation_n1 = self.activationFunction( in1*self.gain[0] + self.prev_activation_n1*self.gain[1] + self.prev_activation_n2*self.gain[2] )
        activation_n2 = self.activationFunction( in2*self.gain[0] + self.prev_activation_n2*self.gain[1] + self.prev_activation_n1*self.gain[2] )
        self.prev_activation_n1 = activation_n1
        self.prev_activation_n2 = activation_n2
        return (activation_n1, activation_n2)
    
    def getAction(self):
        return self.convertWheelSpeedsToTwist( self.getOutput( self.latest_sensor_data[0], self.latest_sensor_data[1] ))
          

    
    
    