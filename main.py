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



'''
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
'''

random.seed(1337)
          
resources = [DIRT,GRASS,WATER,COAL]

#tilemap = [[0,1,2,3,4,5,6,7,8,9,10]]
         
#use list comprehension to create our tilemap
#tilemap = [ [random.choice(resources) for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]
        
tilemap = PerlinNoise.GeneratePerlinNoise(MAPWIDTH,MAPHEIGHT,20)
tilemap = PerlinNoise.convertValuesToInt(tilemap)
    
MapRendererInstance = Render.MapRenderer(tilemap)


#set up the display
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#Get textures from spritesheet.
SpriteSheetInstance = SpriteSheet.SpriteSheet('Change later', 'roguelikeSheet_transparent.png')
textures = SpriteSheetInstance.loadTextures()
renderedmap = MapRendererInstance.renderedmap
while True:

    #get all the user events
    for event in pygame.event.get():
        #print(pygame.mouse.get_pos())
        xmouse,ymouse = pygame.mouse.get_pos()
        try:
            print(renderedmap[int(ymouse/TILESIZE)][int(xmouse/TILESIZE)])
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
            MapRendererInstance.UpdateMap(tilemap,-1,0)
            print('')
            renderedmap = MapRendererInstance.renderedmap
            #MapRendererInstance.printMap()
            
        elif key[pygame.K_a]:
            MapRendererInstance.UpdateMap(tilemap,0,-1)
            renderedmap = MapRendererInstance.renderedmap
            
        elif key[pygame.K_d]:
            MapRendererInstance.UpdateMap(tilemap,0,1)
            renderedmap = MapRendererInstance.renderedmap
            
        elif key[pygame.K_s]:
            MapRendererInstance.UpdateMap(tilemap,1,0)
            renderedmap = MapRendererInstance.renderedmap

     
    #loop through each row
    #start_time = time.time()
    it = np.nditer(renderedmap, flags=['multi_index'])
    while not it.finished:
        SCREEN.blit(textures[np.asscalar(it[0])], (it.multi_index[1]*TILESIZE,it.multi_index[0]*TILESIZE))
        it.iternext()
    #update the display
    pygame.display.update()
    #print("UpdateMap: --- %s seconds ---" % (time.time() - start_time))
    
    