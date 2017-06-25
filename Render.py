import numpy as np
from Constants import *
import time

class MapRenderer():
    def __init__(self,tilemap):
        self.x = 0
        self.y = 0
        self.height = int(RENDERED_MAP_HEIGHT/TILESIZE)
        self.width = int(RENDERED_MAP_WIDTH/TILESIZE)
        self.renderedmap = self.CreateRenderedMap(tilemap)
        
        
    def CreateRenderedMap(self,tilemap):
        #get subset of tilemap which is used to render.
        renderedmap = np.zeros((self.height,self.width),dtype = int)
        for i in range(self.height):
            for j in range(self.width):
                try:
                    value = tilemap[i][j]
                except IndexError: #make this a void tile, or whatever
                    value = VOID
                    
                renderedmap[i][j] = value
        
        return renderedmap
        
        
    def UpdateMap(self,tilemap,dx,dy):
        start_time = time.time()
        self.x = self.x + dx
        self.y = self.y + dy
        
        it = np.nditer(self.renderedmap, flags=['multi_index'])
        while not it.finished:
            try:
                value = tilemap[self.x + it.multi_index[0]][self.y + it.multi_index[1]]
            except IndexError: #make this a void tile, or whatever
                value = VOID
            self.renderedmap[it.multi_index[0]][it.multi_index[1]] = value
            it.iternext()

        print("UpdateMap: --- %s seconds ---" % (time.time() - start_time))
       
                
    def printMap(self):
        for i in range(len(self.renderedmap)):
            print(self.renderedmap[i])
        
        
        
