import sys
from typing import Any

import pygame


class EventHandler:
    """Processa os eventos de entrada do jogo."""

    def process(self, game: Any) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._handle_keydown(game, event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(game, event)

    def _handle_keydown(self, game: Any, event: Any) -> None:
        if event.key == pygame.K_RIGHT:
            game.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            game.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            game.fire_bullet()

    def _handle_keyup(self, game: Any, event: Any) -> None:
        if event.key == pygame.K_RIGHT:
            game.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            game.ship.moving_left = False
