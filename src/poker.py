from collections import deque
import pygame
import sys

import render


def run():
    clock = pygame.time.Clock()
    rolling_window_size = 10
    rolling_render_time_window = deque(maxlen=10)
    while 1:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        start = pygame.time.get_ticks()
        render.render_screen()
        render_time = pygame.time.get_ticks() - start
        rolling_render_time_window.append(render_time)
        print(
            "Current frame rendered in {}ms. Average render time (last {} frames): {}ms".format(
                render_time, rolling_window_size, average(rolling_render_time_window)
            )
        )


def average(items):
    total = 0
    for x in items:
        total += x
    return total / len(items)


if __name__ == "__main__":
    pygame.init()
    render.init()
    run()
