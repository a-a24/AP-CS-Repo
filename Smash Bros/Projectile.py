import pygame
import Level

class Projectile:
    def __init__(self, playerNum, direction, x, y, vx, pixelSize=20,  color = (255,0,0)):
        self.playerNum = playerNum
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
        for tangible in level.getTangible(): #this code lags a  
            if self.rect.colliderect(tangible):
                self.alive = False
        
    def checkPlayerCollisions(self, players):
        for player in players:
            if player.num == self.playerNum:
                return
            yMatch = player.y - .4 < (self.y) < self.y + .4

            if not yMatch:
                return    

            predictedProjPos = self.x + self.vx*0.3
            predictedPlayPos = player.x + player.vx*0.3
            predictedDist = predictedProjPos - predictedPlayPos
            currentDist = self.x - player.x
            xMatch = player.x <= self.x <= player.x + 1
            if  currentDist > predictedDist < 2:
                if xMatch:
                    player.hit(10)


    def update(self,level,dt):
        self.rect.move_ip(self.vx*dt*self.pixelSize,0)
        self.checkCollision(level)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
