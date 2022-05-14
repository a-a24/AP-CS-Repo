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

players = [Player(20, 3, (255, 0, 255)), Player(30, 3, (255, 255, 0))]


lastUpdate = time.time()

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    p = players[pygame.joystick.get_count()]
    if keys[pygame.K_LEFT]:
        p.goLeft()
    elif keys[pygame.K_RIGHT]:
        p.goRight()
    else:
        p.stop()
    for event in events:
        if event.type == JOYBUTTONDOWN:
            if event.button == 1:
                players[event.joy].jump()
        if event.type == JOYAXISMOTION:
            print('axis motion', event.joy, event.axis, event.value)
            if event.axis < 2:
                pass
        if event.type == JOYHATMOTION:
            players[event.joy].move(event.value[0])
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK!")
        if event.type == pygame.KEYDOWN:
            p = players[pygame.joystick.get_count()]
            if event.key == pygame.K_UP:
                p.jump()
           
        #     if event.key == pygame.K_LEFT:
        #         p.goLeft()
                
        #     if event.key == pygame.K_RIGHT:
        #        p.goRight()
                
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         p.stop()
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


