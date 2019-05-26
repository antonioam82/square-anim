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
#direction = 'right'

#CONTROLAR ELEMENTO POR PANTALLA.
while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==K_LEFT:
                sqx-=5
            elif event.key==K_RIGHT:
                sqx+=5
            elif event.key==K_UP:
                sqy-=5
            elif event.key==K_DOWN:
                sqy+=5
    DISPLAYSURF.blit(sqImg, (sqx, sqy))
    pygame.display.update()
