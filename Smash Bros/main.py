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
for i in range(pygame.joystick.get_count() + 1):
    players.append(Player(i+1, i*5 + 10, 3, (255, 0, 255)))
    #players = [Player(1, 20, 3, (255, 0, 255)), Player(2, 30, 3, (255, 255, 0))]


lastUpdate = time.time()


while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    p = players[pygame.joystick.get_count()]
    
    
    # Keybinds
    
    for event in events:
        
        # Keyboard

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.goLeft()        
            if event.key == pygame.K_RIGHT:
                p.goRight()
            if event.key == pygame.K_UP:
                p.jump()
            if event.key == pygame.K_x:
                p.shoot()
            if event.key == pygame.K_z:
                p.attack(players)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p.stop()

        # Controller
    
        if event.type == JOYAXISMOTION:
            #print('axis motion', event.joy, event.axis, event.value)
            if event.axis == 0:
                players[event.joy].setVX(event.value)
            if event.axis == 1 and event.value < -0.75:
                players[event.joy].jump()
                players[event.joy].joyAxisJump = False
            if event.axis == 1 and event.value >= -0.75:
                players[event.joy].joyAxisJump = True
        if event.type == JOYBUTTONDOWN:
            if event.button == 0:
                players[event.joy].attack(players)
            if event.button == 1:
                players[event.joy].shoot()
            if event.button == 2:
                players[event.joy].jump()
            if event.button == 3:
                players[event.joy].jump()
            if event.button == 4:
                players[event.joy].shield(dt)
                print(players[event.joy].shieldHealth)
                print(players[event.joy].shielded)
            if event.button == 5:
                #players[event.joy].grab()
                pass
        if event.type == JOYBUTTONUP:
            if event.button == 4:
                players[event.joy].shielded = False
                print(players[event.joy].shieldHealth)
                print(players[event.joy].shielded)
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



