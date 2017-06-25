import pygame, os
from Constants import *

class SpriteSheet(object):
    '''
    Class used to get spries from spritesheet.
    '''
    
    def __init__(self,image_directory,file_name):
        '''
        Constructor. Pass name of file.
        '''
        #get path
        #TODO: fix so that you can use any path.
        #file = os.path.join(image_directory, file_name)
        #self.image = pygame.image.load(file_name)
        #Load sprite sheet
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def getImage(self,x,y,width,height):
        '''
        Grabs a single image at position (x,y), needs
        width and height of the sprites.
        '''
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x*16+x, y*16+y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey((   0,   0,   0))
 
        # Return the image
        return image
        
        
    def loadTextures(self):
        #a dictionary linking resources to textures
        textures =   {
                        VOID  : self.getImage(3,22,16,16),
                        1  : self.getImage(0,0,16,16),
                        2 : self.getImage(3,1,16,16),
                        3 : self.getImage(8,0,16,16),
                        4  : self.getImage(8,1,16,16),
                        5  : self.getImage(7,0,16,16),
                        6 : self.getImage(5,0,16,16),
                        7 : self.getImage(7,2,16,16),
                        8  : self.getImage(9,1,16,16),
                        9  : self.getImage(6,0,16,16),
                        10  : self.getImage(9,5,16,16)
                    }
                    
                    
        return textures


