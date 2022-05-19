import pygame

class Tile:
    pixelSize = 10
    tileType = 0 #0-air 1-solid block 2-able to jump through, hit down button to go down through
    x = 0
    y = 0
    def __init__(self, xCoord, yCoord, width, height, pixelSize = 10, tileType = 0):
        self.x = xCoord
        self.y = yCoord
        self.width = width
        self.height = height
        self.pixelSize = pixelSize
        self.tileType = tileType
        self.drawRect = (self.x*self.pixelSize, self.y*self.pixelSize, self.width * self.pixelSize, self.height * self.pixelSize)
        self.rect = (self.x, self.y, self.width, self.height)
    
    def getType(self):
        return self.tileType

    def setType(self, newType):
        self.tileType = newType

    def draw(self, screen):
        if self.tileType == 1:
            pygame.draw.rect(screen, (0, 255,100), self.drawRect)
        elif self.tileType == 2:
            pygame.draw.rect(screen, (139, 69, 19), self.drawRect)
        # pygame.draw.rect(screen, (50, 50, 50), (self.x*self.pixelSize, self.y*self.pixelSize, self.pixelSize, self.pixelSize), 1)

