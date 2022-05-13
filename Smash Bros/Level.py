import pygame
from Tile import Tile
from pprint import pprint

red = (255,0,0)
class Level:
    pixelSize = 0
    cGrid = []
    def __init__(self, pSize, xMax, yMax):
        self.pixelSize = pSize
        self.cGrid = [[Tile(j,i,pSize) for j in range(xMax)] for i in range(yMax)]

    def getGrid(self):
        return self.cGrid

    def setTile(self,x,y,type):
        self.cGrid[y][x].setType(type)

    def draw(self,screen):
        for r in range(0,len(self.cGrid)):
            for c in range(0,len(self.cGrid[r])):
                self.cGrid[r][c].draw(screen)
