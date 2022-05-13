
import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.name = "Temporary"
<<<<<<< HEAD
        self.left = False
        self.right = False
        self.jumps = 0
<<<<<<< HEAD
        self.height = 1
=======
=======
        self.health = 100
>>>>>>> 9481c79 (Added health)
>>>>>>> 62af223 (Attacking)

    def update(self, level, dt):
        self.vy += 12 * dt

        for row in level.cGrid:
            for tile in row:
                if self.vy > 0.0 and tile.tileType > 0:
                    yMatch = tile.y + .4 > (self.y + self.height) > tile.y - .4
                    xMatch = tile.x <= self.x <= tile.x + 1
                    if yMatch and xMatch:
                        self.jumps = 2
                        self.vy = 0
                        self.y = tile.y - self.height

        self.y += self.vy * dt
        self.x += self.vx * dt
        

    def goLeft(self):
        self.vx = -8
      
    def goRight(self):
        self.vx = 8
    
    def stop(self):
        self.vx = 0

    def Jump(self):
        print(self.jumps)
        if self.jumps > 0:
            self.vy = -8
            self.jumps -=1
        


    def draw(self, screen, pixelSize):
        pygame.draw.circle(screen, (0,255,0),(self.x * pixelSize,self.y * pixelSize), self.height * pixelSize)
        # pygame.draw.rect(screen, (255,0,0),(100,650,800,10))
        # pygame.draw.rect(screen, (255,0,0),(300,400,400,10))
