import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "Temporary"
    
    def update(self):
        self.y += .1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0,0), (self.x, self.y, 10, 10))
