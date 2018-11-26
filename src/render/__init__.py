import pygame
from render.card import CardRenderer
from card import Card, Suite, Value

_black = 0, 0, 0
_screen = None
_cardRenderer = None
_card_back_image = None


def init():
    size = width, height = 800, 800

    global _screen, _cardRenderer, _card_back_image
    _screen = pygame.display.set_mode(size)
    _cardRenderer = CardRenderer(
        pygame.image.load("res/default-card.png").convert_alpha()
    )
    _card_back_image = pygame.image.load("res/default-card-back.png").convert_alpha()


def render_screen():
    card_to_render = Card(suite=Suite.SPADES, value=Value.JACK)
    card_back_rect = _card_back_image.get_rect()
    _screen.fill(_black)
    _screen.blit(_card_back_image, card_back_rect)
    _screen.blit(_cardRenderer.render_card(card_to_render), card_back_rect.topright)
    pygame.display.flip()
