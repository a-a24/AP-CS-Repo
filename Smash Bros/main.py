from gc import get_count
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


pixelSize = 20
screen = pygame.display.set_mode((50 * pixelSize, 40 * pixelSize))


level = Level(pixelSize)
level.addObstacle(10, 20, 20, 1, 1)
level.addObstacle(10, 13, 15, 1, 2)
level.addObstacle(40,20,20,1,3)
level.addObstacle(10, 15, 2, 10, 2)

players = []
for i in range( pygame.joystick.get_count() + 2):
    players.append(Player(i+1, i*5 + 10, 3, (255, 0, 255)))
    #players = [Player(1, 20, 3, (255, 0, 255)), Player(2, 30, 3, (255, 255, 0))]


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

    if keys[pygame.K_DOWN]:
        p.goDown()
    for event in events:            
        if event.type == JOYBUTTONDOWN:
            if event.button == 2:
                players[event.joy].jump()
            if event.button == 1:
                players[event.joy].shoot()
            if event.button == 0:
                players[event.joy].attack(players)
        if event.type == JOYAXISMOTION:
            print('axis motion', event.joy, event.axis, event.value)
            if event.axis == 0:
                players[event.joy].setVX(event.value)
        if event.type == JOYHATMOTION:
            players[event.joy].move(event.value[0])

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK!")
        if event.type == pygame.KEYDOWN:
            p = players[pygame.joystick.get_count()]
            if event.key == pygame.K_UP:
                p.jump()
            if event.key == pygame.K_x:
                p.shoot()
            if event.key == pygame.K_z:
                p.attack(players)

        if event.type == pygame.QUIT:
            exit()

    level.draw(screen)

    dt = time.time() - lastUpdate
    lastUpdate = time.time()
    for i in range(len(players)):
        p = players[i]
        p.update(level, players, dt)
        p.draw(screen, pixelSize, i)      

    livingPlayers = []
    for i in range(len(players)):
        if players[i].health > 0:
            livingPlayers.append(i)
    if len(livingPlayers) == 1:
        print("Winner: " + str(livingPlayers[0]))
        exit()

    pygame.display.update()
    clock.tick(30)



