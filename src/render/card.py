import pygame
from pygame import Surface, transform

_icon_size = _icon_width, _icon_height = (15, 20)
_icon_position = _icon_position_x, _icon_position_y = (10, 5)


class CardRenderer:
    def __init__(self, base_image):
        self._card_base = base_image
        self._spade_image = transform.scale(
            pygame.image.load("res/spade.png"), _icon_size
        )
        self._heart_image = transform.scale(
            pygame.image.load("res/heart.png"), _icon_size
        )
        self._card_font = pygame.font.SysFont("Arial", 30)
        self._icon_vertical_spacing = -5

    def render_card(self, card):
        rendered_card = self._card_base.copy()
        card_rect = rendered_card.get_rect()
        value_and_suite_icon = self.render_value_and_suite("2", "spades")
        rendered_card.blit(value_and_suite_icon, _icon_position)
        rendered_card.blit(
            transform.rotate(value_and_suite_icon, 180),
            (
                card_rect.right - _icon_position_x - value_and_suite_icon.get_width(),
                card_rect.bottom - _icon_position_y - value_and_suite_icon.get_height(),
            ),
        )
        return rendered_card

    def render_value_and_suite(self, value, suite):
        text_width, text_height = self._card_font.size(value)
        required_surface_size = (
            max(text_width, _icon_width),
            text_height + _icon_height + self._icon_vertical_spacing,
        )
        suite_icon_offset = (required_surface_size[0] - _icon_width) / 2
        icon_surface = Surface(required_surface_size, pygame.SRCALPHA, 32)
        value_icon = self._card_font.render(value, True, (0, 0, 0))
        suite_icon = self._spade_image
        icon_surface.blit(value_icon, (0, 0))
        icon_surface.blit(
            suite_icon,
            (suite_icon_offset, value_icon.get_height() + self._icon_vertical_spacing),
        )
        return icon_surface
