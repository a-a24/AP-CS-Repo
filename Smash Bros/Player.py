import pygame

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.name = "Temporary"
        self.jumps = 0
        self.height = 1
        self.health = 100
        self.left = False
        self.right = False
        self.jumps = 0
        self.health = 100
        self.color = color

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
    
    def move(self, dir):
        if (dir == -1):
            self.goLeft()
        elif (dir == 1):
            self.goRight()
        else:
            self.stop()
    
    def stop(self):
        self.vx *= 0.9

    def jump(self):
        print(self.jumps)
        if self.jumps > 0:
            self.vy = -8
            self.jumps -=1

    def attack(self, players):
        for player in players:
            if (player != self):
                if abs(player.x - self.x) < 10 and abs(player.y - self.y) < 10:
                    player.health -= 10
        
    def draw(self, screen, pixelSize):
        pygame.draw.circle(screen, self.color,(self.x * pixelSize,self.y * pixelSize), self.height * pixelSize)
        # pygame.draw.rect(screen, (255,0,0),(100,650,800,10))
        # pygame.draw.rect(screen, (255,0,0),(300,400,400,10))
