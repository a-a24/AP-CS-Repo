import pygame
from pygame.locals import JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION, JOYHATMOTION
from Player import Player
from Level import Level
import time

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
# print(len(joysticks) " controllers detected.")

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 800))

pixelSize = 20

level = Level(pixelSize, 100, 80)

for i in range(20):
    level.setTile(i + 10, 25,1)

players = [Player(20, 3)]


lastUpdate = time.time()

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:

        if event.type == JOYBUTTONDOWN:
            print('button', event.joy, event.button)
        if event.type == JOYAXISMOTION:
            print('axis motion', event.joy, event.axis, event.value)
            if event.axis < 2:
                pass
        if event.type == JOYHATMOTION:
            print('hat motion', event.joy, event.value)
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                players[0].Jump()
           
            if event.key == pygame.K_LEFT:
                players[0].goLeft()
                
            if event.key == pygame.K_RIGHT:
               players[0].goRight()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                players[0].stop()
        if event.type == pygame.QUIT:
            exit()

    level.draw(screen)
    for p in players:
        dt = time.time() - lastUpdate
        p.update(level, dt)
        p.draw(screen, pixelSize)

    lastUpdate = time.time()
    pygame.display.update()
    clock.tick(30)


