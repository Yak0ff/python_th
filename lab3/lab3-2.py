import pygame
import sys
from pygame.draw import *
import random

def cloud (num_cloud, scr):
    x = 100; y = 100; i = 1
    for i in range(num_cloud):
        circle(scr, 'black', (x, y), 31, 1)
        circle(scr, 'white', (x, y), 30, 0)
        x = random.randint (100, 200)
        y = random.randint (100, 120)
    return




pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
#r = pygame.Rect(50, 50, 100, 200)
#pygame.draw.rect(screen, (255, 0, 0), r, 0)
#circle(screen, 'yellow', (500, 400), 100)
rect(screen, 'lightblue', (0, 0, 800, 400))
rect(screen, 'blue', (0, 400, 800, 600))
rect(screen, 'yellow', (0, 600, 800, 800))
cloud(10, screen)


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()