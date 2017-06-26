import pygame, sys
from pygame.locals import *
import random
import time
import numpy as np

#other files.
import Render
from Constants import *
import PerlinNoise
import SpriteSheet
from entities import *

'''
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
'''

def handleInput(dx,dy,tilemap,clouds,MapRendererInstance):
    MapRendererInstance.UpdateMap(tilemap,dx,dy)
    renderedmap = MapRendererInstance.renderedmap
    updateCloudPosition(dx,dy,clouds,MapRendererInstance)
    
    return renderedmap 

#TODO: FIX SO THAT CLOUD POSITION IS RELATIVE TO THE SCREEN AND CHECK HOW TO FIND UPPER BOUNDARY
# WHEN CLOUD LEAVES THE SCREEN, THAT IS THE BOTTOM AND RIGHT SIDES OF THE SCREEN.

random.seed(1337)
          
resources = [DIRT,GRASS,WATER,COAL]

#tilemap = [[0,1,2,3,4,5,6,7,8,9,10]]
         
#use list comprehension to create our tilemap
#tilemap = [ [random.choice(resources) for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]
        
tilemap = PerlinNoise.GeneratePerlinNoise(MAPWIDTH,MAPHEIGHT,10)
tilemap = PerlinNoise.convertValuesToInt(tilemap)
    
MapRendererInstance = Render.MapRenderer(tilemap)

#create entities.
clouds = []
for i in range(100):
    clouds.append(Cloud(random.random()*i*50,random.random()*i*50))


#set up the display
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#Get textures from spritesheet.
SpriteSheetInstance = SpriteSheet.SpriteSheet('Change later', 'roguelikeSheet_transparent.png')
textures = SpriteSheetInstance.loadTextures()
renderedmap = MapRendererInstance.renderedmap


#create fpsClock
fpsClock = pygame.time.Clock()
while True:

    #get all the user events
    for event in pygame.event.get():
        #print(pygame.mouse.get_pos())
        xmouse,ymouse = pygame.mouse.get_pos()

        try:
            print((int(ymouse/TILESIZE),int(xmouse/TILESIZE)),
                renderedmap[int(ymouse/TILESIZE)][int(xmouse/TILESIZE)])
        except IndexError:
            print('void')

        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
            
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            print("Space!")
            
        elif key[pygame.K_w]:
            renderedmap = handleInput(-1,0,tilemap,clouds,MapRendererInstance)

            
        elif key[pygame.K_a]:
            renderedmap = handleInput(0,-1,tilemap,clouds,MapRendererInstance)
            
        elif key[pygame.K_d]:
            renderedmap = handleInput(0,1,tilemap,clouds,MapRendererInstance)
            
        elif key[pygame.K_s]:
            renderedmap = handleInput(1,0,tilemap,clouds,MapRendererInstance)

    #loop through each row
    #start_time = time.time()
    it = np.nditer(renderedmap, flags=['multi_index'])
    while not it.finished:
        SCREEN.blit(textures[np.asscalar(it[0])], (it.multi_index[1]*TILESIZE,it.multi_index[0]*TILESIZE))
        it.iternext()
        
    #display and update entities
    for cloud in clouds:
        cloud.randomMovement()
        cloud.render(SCREEN)
        
    #update the display
    pygame.display.update()
    fpsClock.tick(60)
    #print("UpdateMap: --- %s seconds ---" % (time.time() - start_time))
    
    
    

    
    
    