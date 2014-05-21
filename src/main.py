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
    TEK-Space Evolutionary Algorithm workshop
    2014-05-21
'''
from MobileRobotSimulator import Environment
from evolution import runGenerationTrial, getMutated, generateRandomAgent

# Set up simulator
environment = Environment('maze.png')

# Set up initial population with random genome
environment.agents.append( generateRandomAgent('r') )
environment.agents.append( generateRandomAgent('g') )
environment.agents.append( generateRandomAgent('b') )
environment.agents.append( generateRandomAgent('c') )
environment.agents.append( generateRandomAgent('m') )
environment.agents.append( generateRandomAgent('y') )

# Run n generations
for generation in range(100):
    print "Generation " + str(generation)

    # Animate every n generations    
    if generation % 10 :
        environment.visualise = False
    else :
        environment.visualise = True
    
    # Simulate n trials of this generation
    distance, collision_count = runGenerationTrial(environment, 100)
           
    # Evaluate individuals
    best_collision = collision_count.index(min(collision_count))
    worst_collision = collision_count.index(max(collision_count))
    best_distance = distance.index(max(distance))
    worst_distance = distance.index(min(distance))
    
    # Select best and worst based on fitness
    best = best_distance
    worst = best_distance
    
    # Eradicate worst individual and replace with mutation of best individual 
    print environment.agents[worst].type + " was extinct"
    environment.agents[worst] = getMutated(environment.agents[worst].type, environment.agents[best])
    
    # Reset robot states
    for i in range(len(environment.agents)):
        environment.agents[i].generateNewRandomState()
        environment.visualiser.resetAgentPosterior(i)


    
    