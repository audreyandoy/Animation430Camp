import pygame
import random
from pygame.locals import *
from sprite_loader import Spritesheet
from cat import Cat

pygame.init()

screen_info = pygame.display.Info()

size = (width, height) = (800, 600)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (0, 147, 255)

cat_images = []


def get_cat_images():
    cat_sheet = Spritesheet("cat.png")
    cat_sheet_width = cat_sheet.sprite_sheet.get_rect().width
    cat_sheet_height = cat_sheet.sprite_sheet.get_rect().height
    nrows = 4
    ncols = 2
    cat_width = cat_sheet_width / ncols
    cat_height = cat_sheet_height / nrows

    for row in range(nrows):
        for col in range(ncols):
            cat_images.append(cat_sheet.get_image(
               col * cat_width,
               row * cat_height,
               cat_width,
               cat_height))
            scale = 0.5
            cat_images[-1] = pygame.transform.smoothscale(
             cat_images[-1],
             (int(cat_width*scale), int(cat_height*scale))
            )


def main():
    get_cat_images()
    cat = Cat((-90, random.randint(50, height-50)), cat_images)
    while True:
        clock.tick(60)
        cat.update()
        screen.fill(color)
        cat.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
