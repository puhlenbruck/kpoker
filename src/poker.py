import pygame
import sys

import render


def run():
    clock = pygame.time.Clock()
    while 1:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        start = pygame.time.get_ticks()
        render.render_screen()
        print("rendered in {}ms".format(pygame.time.get_ticks() - start))


if __name__ == "__main__":
    pygame.init()
    render.init()
    run()
