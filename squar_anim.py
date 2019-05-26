import pygame, sys
#import os
from pygame.locals import *

#os.chdir(r'')

#INICIAMOS PYGAME.
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#CREAMOS VENTANA
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)

#CARGAMOS Y UBICAMOS ARCHIVO DE IMAGEN.
sqImg = pygame.image.load('anger_square.png')
sqx = 10
sqy = 10
direction = 'right'

#CREAMOS ANIMACION.
while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        sqx += 5
        if sqx == 280:
            direction = 'down'
    elif direction == 'down':
        sqy += 5
        if sqy == 220:
            direction = 'left'
    elif direction == 'left':
        sqx -= 5
        if sqx == 10:
            direction = 'up'
    elif direction == 'up':
        sqy -= 5
        if sqy == 10:
            direction = 'right'

    DISPLAYSURF.blit(sqImg, (sqx, sqy))

    #FINALIZACIÓN DEL PROGRAMA.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
            
