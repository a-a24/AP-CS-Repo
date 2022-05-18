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
level.addObstacle(5, 10, 1, 10, 2)

players = [Player(1,20, 3, (255, 0, 255)), Player(2,30, 3, (255, 255, 0))]


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
            if event.key == pygame.K_x:
                p.shoot()
            if event.key == pygame.K_z:
                p.attack(players)
                           
            # if event.key == pygame.K_LEFT:
            #     p.goLeft()
                
        #     if event.key == pygame.K_RIGHT:
        #        p.goRight()
                
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         p.stop()
        if event.type == pygame.QUIT:
            exit()

    level.draw(screen)
    projectiles = []
    for p in players:
        projectiles += p.projectiles

    dt = time.time() - lastUpdate
    lastUpdate = time.time()
    for i in range(len(players)):
        p = players[i]
        for proj in p.projectiles:
            proj.checkPlayerCollisions(players)
        # p.checkCollisions(projectiles)
        p.update(level, dt)
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


