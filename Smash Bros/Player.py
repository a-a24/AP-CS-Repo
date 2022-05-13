
import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.name = "Temporary"
        self.left = False
        self.right = False
        self.jumps = 0

    def update(self):
        if self.left == True:
            self.x -= 1
        if self.right == True:
            self.x += 1

        self.vy +=.12
        if self.vy > 0.0:
            if 650> self.y > 630:
                if 100< self.x <900:
                    self.jumps = 2
                    self.vy = 0
        if self.vy > 0.0:
            if 395>self.y > 385:
                if 300<self.x<700:
                    self.jumps = 2
                    self.vy = 0



    

        self.y += self.vy
        

    def goLeft(self):
        self.left = True
        self.right = False
      
    def goRight(self):
        self.right = True
        self.left = False
    
    def stopRight(self):
        self.right = False
    def stopLeft(self):
        
        
        
        self.left = False
    def Jump(self):
        print(self.jumps)
        if self.jumps > 0:
            self.vy -= 5
            self.jumps -=1
        


    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0),(self.x,self.y),10)
        pygame.draw.rect(screen, (255,0,0),(100,650,800,10))
        pygame.draw.rect(screen, (255,0,0),(300,400,400,10))
