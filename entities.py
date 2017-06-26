
import pygame
import random
from Constants import *

sprites = {
    CLOUD : pygame.image.load('cloud.png')
    }
    
def updateCloudPosition(dx,dy,objects,renderedMap):
    if (renderedMap.x + dx) >= 0 and (renderedMap.y + dy) >= 0:
        for item in objects:
            item.move(-dy*TILESIZE,-dx*TILESIZE) #the coordinates are the other way around lol

   
class Cloud():
    #static variables, to simulate wind
    randomx = random.uniform(-1, 1)
    randomy = random.uniform(-1, 1)
    b = -TILESIZE/4
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        sprites[CLOUD].set_colorkey((   0,   0,   0))
        
    def render(self,screen):
        screen.blit(sprites[CLOUD].convert_alpha(),(self.x,self.y))
        
        
    def move(self,dx,dy):
        value1 = (self.x + dx)/TILESIZE
        value2 = (self.y + dy)/TILESIZE
        value3 = (self.y + dy + RENDERED_MAP_WIDTH)
        value4 = (self.x + dx + RENDERED_MAP_HEIGHT)
        #respawn the cloude outside of the screen
        if (self.x < -5*TILESIZE):
            self.x = RENDERED_MAP_WIDTH + 4*TILESIZE
            self.y = random.random()*RENDERED_MAP_WIDTH
        elif (self.y < -5*TILESIZE):
            self.y = RENDERED_MAP_HEIGHT + 4*TILESIZE
            self.x = random.random()*RENDERED_MAP_HEIGHT
        elif (self.x > RENDERED_MAP_WIDTH + 5*TILESIZE):
            self.x = -4*TILESIZE
            self.y = random.random()*RENDERED_MAP_HEIGHT
        elif (self.y > RENDERED_MAP_HEIGHT + 5*TILESIZE):
            self.y = -4*TILESIZE 
            self.x = random.random()*RENDERED_MAP_WIDTH
        else:
            self.x += dx
            self.y += dy
        
    def randomMovement(self):
        self.move(5*random.random()*Cloud.randomx,5*random.random()*Cloud.randomy)
