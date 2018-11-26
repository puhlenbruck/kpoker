import pygame
from render.card import CardRenderer

_black = 0, 0, 0
_screen = None
_cardRenderer = None


def init():
    size = width, height = 800, 800

    global _screen, _cardRenderer
    _screen = pygame.display.set_mode(size)
    _cardRenderer = CardRenderer()


def render_screen():
    card_back = pygame.image.load("res/default-card-back.png")
    card = pygame.image.load("res/default-card.png")

    card_back_rect = card_back.get_rect()

    _screen.fill(_black)
    _screen.blit(card_back, card_back_rect)
    _screen.blit(_cardRenderer.render_card(card), card_back_rect.topright)
    pygame.display.flip()
