import pygame
import Level

class Projectile:
    def __init__(self, direction, x, y, vx, pixelSize=20,  color = (255,0,0)):
        self.direction = direction
        self.x = x
        self.y = y
        self.vx = vx * direction
        self.pixelSize = pixelSize
        self.color = color
        self.alive = True
        self.rect = pygame.Rect(self.x*pixelSize,self.y*pixelSize,pixelSize, pixelSize/2)
        self.collisionCheckCounter = 0
    
    def checkCollision(self, level):
        self.collisionCheckCounter += 1
        if self.collisionCheckCounter % 3 > 0:
            return
        if(self.x < 0 or self.x > 900 or self.y >1000):
            self.alive = False
        for tangible in level.getTangible(): #this code lags a fuck ton 
            if self.rect.colliderect(tangible):
                self.alive = False


    def update(self,level,dt):
        self.rect.move_ip(self.vx*dt*self.pixelSize,0)
        self.checkCollision(level)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
