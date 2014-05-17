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
            self.image = np.array(Image.open('maze.png').convert('L')) # TODO: make mutator
    
    def inCollision(self,(x,y)):         
        return self.image[y,x] < 128
    
    def getSize(self):
        return reversed(self.image.shape)