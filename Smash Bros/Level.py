import pygame

red = (255,0,0)
class Level:
    pixelSize = 0
    cGrid = []
    def __init__(self, pSize, xMax, yMax):
        pixelSize = pSize
        for i in range(0, yMax):
            row = []
            for j in range(0, xMax):
                row.append(0)
            self.cGrid.append(row)

    def turnOn(self,x,y):
        self.cGrid[y][x] = 1
    def draw(self,screen):
        for r in range(0,len(self.cGrid)):
            for c in range(0,len(self.cGrid[r])):
                if self.cGrid[r][c]>0:
                    pygame.draw.rect(screen, (0, 0,255), (c, r, 10, 10))
