import pygame
from pygame.locals import *

pygame.init()

def key_down(key):
    print("down", key)
    pass

def key_up(key):
    print("up", key)
    pass

while True:
    for event in pygame.event.get():
        ###if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        if event.type == pygame.KEYDOWN:
            key_down(event.key)
        elif event.type == pygame.KEYUP:
            key_up(event.key)


