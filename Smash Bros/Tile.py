import pygame

class Tile:
    pixelSize = 10
    tileType = 0 #0-empty 1-block
    x = 0
    y = 0
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
    
    # def __init__(self, xCoord, yCoord, tileType):
    #     self.x = xCoord
    #     self.y = yCoord
    #     self.tileType = tileType

    def getType(self):
        return self.tileType

    def setType(self, newType):
        self.tileType = newType

    def draw(self, screen):
        if self.tileType == 1:
            pygame.draw.rect(screen, (0, 0,255), (self.x*10, self.y*10, 10, 10))
        elif self.tileType == 2:
            pygame.draw.rect(screen, (255, 0,0), (self.x*10, self.y*10, 10, 10))

