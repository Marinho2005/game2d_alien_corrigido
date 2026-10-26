from typing import Any

from alien import Alien


class FleetManager:
    """Cria e atualiza a frota de alienígenas."""

    def create(self, game: Any) -> None:
        alien = Alien(game.screen, game.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = game.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = game.ship.rect.height
        available_space_y = game.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                fleet_alien = Alien(game.screen, game.settings)
                fleet_alien.x = alien_width + 2 * alien_width * alien_number
                fleet_alien.rect.x = fleet_alien.x
                fleet_alien.y = alien_height + 2 * alien_height * row_number
                fleet_alien.rect.y = fleet_alien.y
                game.aliens.add(fleet_alien)

    def update(self, game: Any) -> None:
        game.aliens.update()
        for alien in game.aliens.sprites():
            if alien.check_edges():
                for fleet_alien in game.aliens.sprites():
                    fleet_alien.rect.y += game.settings.fleet_drop_speed
                game.settings.fleet_direction *= -1
                break
