import pygame
from Player import Player

pygame.init()

screen = pygame.display.set_mode((1000, 800))
players = [Player(50, 50), Player(10, 10)]

while True:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("CLICK!")
        if event.type == pygame.QUIT:
            exit()

    for p in players:
        p.update()
        p.draw(screen)

    pygame.display.update()


