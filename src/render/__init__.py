import pygame
from pygame import Surface
from render.card import CardRenderer
from card import Card, Suite, Value

_black = 0, 0, 0
_screen: Surface = None
_cardRenderer: CardRenderer = None
_card_back_image: Surface = None

_card_size = _card_width, _card_height = (120, 168)
_card_spacing = 10
_board_size = (_card_width * 5 + _card_spacing * 4, _card_height)


def init():
    global screen_size, screen_width, screen_height, _screen, _cardRenderer, _card_back_image

    screen_size = screen_width, screen_height = 800, 800
    _screen = pygame.display.set_mode(screen_size)
    _cardRenderer = CardRenderer(
        pygame.image.load("res/default-card.png").convert_alpha()
    )
    _card_back_image = pygame.image.load("res/default-card-back.png").convert_alpha()


def render_screen(hand, board):
    card_to_render = Card(suite=Suite.SPADES, value=Value.JACK)
    card_back_rect = _card_back_image.get_rect()
    _screen.fill(_black)
    _screen.blit(_card_back_image, card_back_rect)
    _screen.blit(_cardRenderer.render_card(card_to_render), card_back_rect.topright)
    _screen.blit(render_board(board), board_position())
    pygame.display.flip()


def board_position():
    x_pos = (screen_width / 2) - (_board_size[0] / 2)
    y_pos = (screen_height / 2) - (_card_height / 2)
    return x_pos, y_pos


def render_board(board):
    board_surface = Surface(_board_size)
    for card_number, board_card in enumerate(board[:5]):
        board_surface.blit(
            _cardRenderer.render_card(board_card),
            (card_number * (_card_width + _card_spacing), 0),
        )
    return board_surface
