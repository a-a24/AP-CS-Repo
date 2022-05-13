import pygame

class Tile:
    pixelSize = 10
    tileType = 0 #0-air 1-solid block 2-able to jump through, hit down button to go down through
    x = 0
    y = 0
    def __init__(self, xCoord, yCoord, pixelSize = 10, tileType = 0):
        self.x = xCoord
        self.y = yCoord
        self.pixelSize = pixelSize
        self.tileType = tileType
    
    def getType(self):
        return self.tileType

    def setType(self, newType):
        self.tileType = newType

    def draw(self, screen):
        if self.tileType == 1:
            pygame.draw.rect(screen, (0, 255,100), (self.x*self.pixelSize, self.y*self.pixelSize, self.pixelSize, self.pixelSize))
        elif self.tileType == 2:
            pygame.draw.rect(screen, (139, 69, 19), (self.x*self.pixelSize, self.y*self.pixelSize, self.pixelSize, self.pixelSize))
        # pygame.draw.rect(screen, (50, 50, 50), (self.x*self.pixelSize, self.y*self.pixelSize, self.pixelSize, self.pixelSize), 1)

