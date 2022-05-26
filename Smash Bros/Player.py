from asyncio import shield
import time
from Tile import Tile
import pygame
from Projectile import Projectile

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 48)

class Player:
    def __init__(self, num, x, y, color):
        self.num = num
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.facing = 1
        self.name = "Temporary"
        self.jumps = 0
        self.radius = 1
        self.health = 100
        self.left = False
        self.right = False
        self.jumps = 0
        self.health = 100
        self.color = color
        self.lastShot = 0
        self.projectiles = []
        self.onObstacle = Tile(0,0,0,0,0,0)
        self.goingDown = False
        self.shielded = False
        self.shieldHealth = 50
        self.joyAxisJump = True
        self.stopping = False

    def update(self, level, players, dt):
        print(self.onObstacle.tileType)
        if self.health <= 0:
            return
        if self.stopping:
            if self.onObstacle.tileType == 3:
                self.vx *= 0.95
            else:
                self.vx *= 0.8
        if 0 < self.vx < 1 or -1 < self.vx < 0:
            self.vx = 0
            self.stopping = False
        if self.goingDown:
            self.vy = 6
            #self.checkOnObstacle (level, players, dt)
            if not self.onObstacle.tileType == 2:
                self.goingDown = False
        if self.shielded:
            self.shieldHealth -= 10 * dt
        else:
            self.shieldHealth += 5 * dt
            if self.shieldHealth > 50:
                self.shieldHealth = 50
        if self.shieldHealth <= 0:
            self.shielded = False

        for projectile in self.projectiles:
            if projectile.alive == True:
                projectile.update(level,players,dt)

        self.vy += 12 * dt
        # self.onObstacle = Tile(0,0,0,0,0,0)
        self.checkOnObstacle (level, players, dt)
                


        self.y += self.vy * dt
        self.x += self.vx * dt
        

    def checkCollisions(self, projectiles):
        otherProjectiles = list(set(projectiles) - set(self.projectiles)) + list(set(self.projectiles) - set(projectiles))
        for projectile in otherProjectiles:
                yMatch = projectile.y + .4 > (self.y + self.radius) > projectile.y - .4
                xMatch = projectile.x <= self.x <= projectile.x + 1
                if yMatch and xMatch:
                    print("hit")
                    self.health -= 10
                    projectile.alive = False
                    self.vx += .5 * projectile.direction * projectile.vx
        
    def checkOnObstacle (self, level, players, dt):
        counter = 0
        for obstacle in level.obstacles:
            if self.vy > 0.0 and obstacle.tileType > 0:
                yMatch = obstacle.y + .4 > (self.y + self.radius) > obstacle.y - .4
                xMatch = obstacle.x <= self.x <= obstacle.x + obstacle.width
                yMatch2 = obstacle.y + 2 > (self.y + self.radius) > obstacle.y - 2
                
                if yMatch and xMatch:
                    if self.goingDown:
                        self.onObstacle = obstacle
                    else:
                        self.jumps = 2
                        self.vy = 0
                        self.y = obstacle.y - self.radius
                        self.onObstacle = obstacle
                else:
                    counter += 1
        if counter % len(level.obstacles) == 0:
            self.onObstacle = Tile(0,0,0,0,0,0)
                

    def goLeft(self):
        self.stopping = False
        self.vx = -8
        self.facing = -1
      
    def goRight(self):
        self.stopping = False
        self.vx = 8
        self.facing = 1

    def goDown(self):
        print(self.onObstacle.tileType)
        if self.onObstacle.tileType == 2:
            self.goingDown = True
        print(self.goingDown)


    def getRect(self):
        return pygame.Rect(self.x,self.y, 2, 2)
    
    def move(self, dir):
        self.stopping = True
        if (dir == -1):
            self.goLeft()
        elif (dir == 1):
            self.goRight()
        else:
            self.stop()
    def setVX(self, dir):
        self.stopping = False
        self.vx = dir * 8
        if (dir > 0.1):
            self.facing = 1
        elif(dir < -0.1):
            self.facing = -1
        else:
            self.stop()
    
    def stop(self):
        self.stopping = True
    
    def stopDown(self):
        self.goingDown = False

    def jump(self):
        if self.jumps > 0 and self.joyAxisJump:
            self.vy = -8
            self.jumps -=1

    def shoot(self):
        now = time.time()
        if now - self.lastShot > .5:
            self.lastShot = now
            self.projectiles.append(Projectile(self.num, self.facing, self.x, self.y, 20))
            if len(self.projectiles) > 10:
                self.projectiles.pop(0)

    def attack(self, players):
        for player in players:
            if (player != self):
                if abs(player.x - self.x) < 10 and abs(player.y - self.y) < 10:
                    if not player.shielded:
                        player.health -= 10
                    else:
                        player.shieldHealth -= 10

    def hit(self, damage):
        self.health -= damage
    def shield(self, dt):
        self.shielded = True

        

        

    def draw(self, screen, pixelSize, playerIndex):
        if self.health<=0:
            #print(self.health)
            pass
            #pygame.draw.circle(screen, (0,0,0),(self.x * pixelSize,self.y * pixelSize), self.radius * pixelSize)
        else:
            if self.shielded:
                pygame.draw.circle(screen, (0,0,255),(self.x * pixelSize,self.y * pixelSize), self.radius * pixelSize)
            else:
                pygame.draw.circle(screen, self.color,(self.x * pixelSize,self.y * pixelSize), self.radius * pixelSize)
        for projectile in self.projectiles:
            if projectile.alive == True:
                projectile.draw(screen)
        if self.health > 0:
            text = str(self.health)
        else:
            text = "DEAD"
        text_surface = my_font.render(text, False, self.color)
        screen.blit(text_surface, (playerIndex * 100,0))