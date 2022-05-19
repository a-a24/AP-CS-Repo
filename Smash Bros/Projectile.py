import pygame
import Util

class Projectile:
    def __init__(self, playerNum, direction, x, y, vx, pixelSize=20,  color = (255,0,0)):
        self.direction = direction
        self.vx = vx * direction
        self.pixelSize = pixelSize
        self.color = color
        self.alive = True
        self.x = x
        self.y = y
        self.radius = .3
        self.collisionCheckCounter = 0
        self.dmg = 5
        self.playerNum = playerNum
    
    def checkCollision(self, level, players):
        self.collisionCheckCounter += 1
        if self.collisionCheckCounter % 3 > 0:
            return
        if(self.x < 0 or self.x > 900 or self.y >1000):
            self.alive = False

        for t in level.getTangible():
            xCollision = (self.x > t.rect[0]) and (self.x < (t.rect[0] + t.rect[2]))
            yCollision = (self.y > t.rect[1]) and (self.y < (t.rect[1] + t.rect[3]))
            if xCollision and yCollision:
                self.alive = False

        for p in players:
            if p.num != self.playerNum:
                if Util.distance(p.getRect(), self) < self.radius + p.radius:
                    p.health -= self.dmg
                    self.alive = False


    def update(self,level, players, dt):
        self.x += self.vx * dt * 1.5
        self.checkCollision(level, players)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x * self.pixelSize,self.y * self.pixelSize), self.radius * self.pixelSize)
