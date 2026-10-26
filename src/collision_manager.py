import sys
from typing import Any

import pygame


class CollisionManager:
    """Aplica as regras de colisão entre os elementos do jogo."""

    def update_bullets(self, game: Any) -> None:
        game.bullets.update()
        for bullet in game.bullets.copy():
            if bullet.rect.bottom <= 0:
                game.bullets.remove(bullet)

    def check_bullet_alien(self, game: Any) -> None:
        pygame.sprite.groupcollide(game.bullets, game.aliens, True, True)

    def check_ship_alien(self, game: Any) -> None:
        if pygame.sprite.spritecollideany(game.ship, game.aliens):
            print("A nave foi atingida!")
            sys.exit()
