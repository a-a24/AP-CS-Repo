import time
import pygame
from Projectile import Projectile

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 48)

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.facing = 1
        self.name = "Temporary"
        self.jumps = 0
        self.height = 1
        self.health = 100
        self.left = False
        self.right = False
        self.jumps = 0
        self.health = 100
        self.color = color
        self.lastShot = 0
        self.projectiles = []

    def update(self, level, dt):
        if self.health <= 0:
            return

        for projectile in self.projectiles:
            if projectile.alive == True:
                projectile.update(level,dt)

        self.vy += 12 * dt

        for obstacle in level.obstacles:
            if self.vy > 0.0 and obstacle.tileType > 0:
                yMatch = obstacle.y + .4 > (self.y + self.height) > obstacle.y - .4
                xMatch = obstacle.x <= self.x <= obstacle.x + obstacle.width

                if yMatch and xMatch:
                    self.jumps = 2
                    self.vy = 0
                    self.y = obstacle.y - self.height

        self.y += self.vy * dt
        self.x += self.vx * dt
        

    def checkCollisions(self, projectiles):
        otherProjectiles = list(set(projectiles) - set(self.projectiles)) + list(set(self.projectiles) - set(projectiles))
        for projectile in otherProjectiles:
                yMatch = projectile.y + .4 > (self.y + self.height) > projectile.y - .4
                xMatch = projectile.x <= self.x <= projectile.x + 1
                if yMatch and xMatch:
                    print("hit")
                    self.health -= 10
                    projectile.alive = False
                    self.vx += .5 * projectile.direction * projectile.vx
            

    def goLeft(self):
        self.vx = -8
        self.facing = -1
      
    def goRight(self):
        self.vx = 8
        self.facing = 1
    
    def move(self, dir):
        if (dir == -1):
            self.goLeft()
        elif (dir == 1):
            self.goRight()
        else:
            self.stop()
    
    def stop(self):
        self.vx *= 0.8

    def jump(self):
        print(self.jumps)
        if self.jumps > 0:
            self.vy = -8
            self.jumps -=1

    def shoot(self):
        now = time.time()
        if now - self.lastShot > .8:
            self.lastShot = now
            self.projectiles.append(Projectile(self.facing, self.x, self.y, 20 + abs(self.vx)))
            if len(self.projectiles) > 10:
                self.projectiles.pop(0)

    def attack(self, players):
        for player in players:
            if (player != self):
                if abs(player.x - self.x) < 10 and abs(player.y - self.y) < 10:
                    player.health -= 10

    def draw(self, screen, pixelSize, playerIndex):
        if self.health<=0:
            pygame.draw.circle(screen, (0,0,0),(self.x * pixelSize,self.y * pixelSize), self.height * pixelSize)
        else:
            pygame.draw.circle(screen, self.color,(self.x * pixelSize,self.y * pixelSize), self.height * pixelSize)
        for projectile in self.projectiles:
            if projectile.alive == True:
                projectile.draw(screen)
        if self.health > 0:
            text = str(self.health)
        else:
            text = "DEAD"
        text_surface = my_font.render(text, False, self.color)
        screen.blit(text_surface, (playerIndex * 100,0))