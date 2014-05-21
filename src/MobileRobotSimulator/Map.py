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
    Singleton implements the singleton pattern
    
    Map implements the obstacle map of the environment 
'''
import numpy as np
import Image

class Singleton(object):
    _instance = None
    _initialised = False
    def __new__(self):
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance 

class Map(Singleton):
    def __init__(self):
        if not self._initialised:
            self._initialised = True
            self.image = None
            self.image_size = None
            self.state_range = None
    
    def setObstacles(self, obstacles):
        self.image = np.array(Image.open(obstacles).convert('L'))
        self.image_size = np.shape(self.image)
        self.state_range = [self.image_size[1]-2, self.image_size[0]-2, 2*np.pi, 0]
    
    def inCollision(self,(x,y)):  
        if x < self.image_size[1]-1 and y < self.image_size[0]-1 and x > 5 and y > 5:    
            return self.image[y,x] < 128
        else:
            return True
    
    def getSize(self):
        return reversed(self.image.shape)
    
    def getRandomCollisionFreeState(self):
        p = np.random.random(4)*self.state_range
        while self.inCollision((p[0], p[1])) :
            p = np.random.random(4)*self.state_range
        return p
        