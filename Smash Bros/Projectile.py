import pygame

class Projectile:
    def __init__(self, direction, x, y, vx, pixelSize=20,  color = (255,0,0)):
        self.direction = direction
        self.x = x*pixelSize
        self.y = y*pixelSize
        self.vx = vx * direction
        self.pixelSize = pixelSize
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,pixelSize, pixelSize/2)
    
    def update(self,dt):
        self.rect.move_ip(self.vx*dt*self.pixelSize,0)
        if(self.x>900 or self.y >1000):
            del self
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
