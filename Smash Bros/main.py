import pygame
from pygame.locals import JOYBUTTONDOWN, JOYBUTTONUP, JOYAXISMOTION, JOYHATMOTION
from Player import Player

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(len(joysticks) " controllers detected.")

screen = pygame.display.set_mode((1000, 800))
players = [Player(50, 50), Player(10, 10)]

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == JOYBUTTONDOWN:
            print('button', event.joy, event.button)
        if event.type == JOYAXISMOTION:
            print('axis motion', event.joy, event.axis)
            if event.axis < 2:
                pass
        if event.type == JOYHATMOTION:
            print('hat motion', event.joy, event.value)
            pass
        if event.type == pygame.QUIT:
            exit()

    for p in players:
        p.update()
        p.draw(screen)

    pygame.display.update()


