import pygame
from pygame.locals import JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION, JOYHATMOTION
from Player import Player
from Level import Level

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
# print(len(joysticks) " controllers detected.")

screen = pygame.display.set_mode((1000, 800))


level = Level(20, 100, 80)
players = [Player(400, 50)]

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:

        print('button', event.joy, event.button)
        if event.type == JOYAXISMOTION:
            print('axis motion', event.joy, event.axis)
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
            if event.key == pygame.K_LEFT:
                players[0].stopLeft()
            if event.key == pygame.K_RIGHT:
                players[0].stopRight()
        if event.type == pygame.QUIT:
            exit()

    for p in players:
        p.update()
        p.draw(screen)
    level.setTile(25,25,1)
    level.setTile(26,25,2)
    level.draw(screen)
    pygame.display.update()


