from typing import Any

import pygame


class Renderer:
    """Desenha o estado atual do jogo na tela."""

    def draw(self, game: Any) -> None:
        game.screen.fill(game.bg_color)
        game.ship.blitme()
        game.aliens.draw(game.screen)
        for bullet in game.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
