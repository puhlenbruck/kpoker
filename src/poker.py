import pygame
import sys

from diagnostics import DiagnosticOutput
from game import PokerGame
import render


diagnostics = None


def run():
    clock = pygame.time.Clock()
    game = PokerGame(1)
    hand, board = game.play_round()

    while 1:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        render_start = pygame.time.get_ticks()
        render.render_screen(hand, board)
        diagnostics.record_frame_time(pygame.time.get_ticks() - render_start)


if __name__ == "__main__":
    pygame.init()
    render.init()
    if len(sys.argv) > 1 and sys.argv[1] == "--frame-times":
        diagnostics = DiagnosticOutput(frame_times=True)
    else:
        diagnostics = DiagnosticOutput()
    run()
