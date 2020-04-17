import pygame
import argparse
import skimage

from pygame.locals import *
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("picture_path",  help='Path to picture')
args = parser.parse_args()
img = skimage.color.rgb2gray(skimage.io.imread(Path(args.picture_path)))

GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

display_w, display_h = 640, 240

gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('IScissors')

running = True
moving = False

Img = pygame.surfarray.make_surface(img.T)
rect = Img.get_rect()
rect.center = display_w // 2, display_h // 2

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    gameDisplay.fill(GRAY)
    gameDisplay.blit(Img, rect)
    pygame.draw.rect(gameDisplay, BLACK, rect, 1)
    pygame.display.update()

    Img = pygame.surfarray.make_surface(img.T)
pygame.quit()
