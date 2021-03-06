import pygame
from pygame import Surface

import render.color
from render.card import CardRenderer

_screen: Surface = None
_cardRenderer: CardRenderer = None
_card_back_image: Surface = None

_card_size = _card_width, _card_height = (120, 168)
_card_spacing = 10
_board_size = (_card_width * 5 + _card_spacing * 4, _card_height)

_hand_area_size = (_card_width * 2 + _card_spacing, _card_height)


def init():
    global screen_size, screen_width, screen_height, _screen, _cardRenderer, _card_back_image

    screen_size = screen_width, screen_height = 800, 800
    _screen = pygame.display.set_mode(screen_size)
    _cardRenderer = CardRenderer(
        pygame.image.load("res/default-card.png").convert_alpha()
    )
    _card_back_image = pygame.image.load("res/default-card-back.png").convert_alpha()


def render_screen(hand, board):
    _screen.fill(color.BLACK)
    _screen.blit(render_board(board), board_position())
    _screen.blit(render_hand(hand), hand_position())
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


def hand_position():
    x_pos = (screen_width / 2) - (_hand_area_size[0] / 2)
    y_pos = (screen_height - 25) - _card_height
    return x_pos, y_pos


def render_hand(hand):
    hand_surface = Surface(_board_size)
    for card_number, hand_card in enumerate(hand[:2]):
        hand_surface.blit(
            _cardRenderer.render_card(hand_card),
            (card_number * (_card_width + _card_spacing), 0),
        )
    return hand_surface
