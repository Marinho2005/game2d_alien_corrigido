from typing import Any

from alien import Alien
from fleet_formation import FleetFormation, GridFleetFormation


class FleetManager:
    """Cria e atualiza a frota de alienígenas."""

    def __init__(self, formation: FleetFormation | None = None) -> None:
        self.formation = formation or GridFleetFormation()

    def create(self, game: Any) -> None:
        for x_position, y_position in self.formation.positions(game):
            fleet_alien = Alien(game.screen, game.settings)
            fleet_alien.x = x_position
            fleet_alien.rect.x = x_position
            fleet_alien.y = y_position
            fleet_alien.rect.y = y_position
            game.aliens.add(fleet_alien)

    def update(self, game: Any) -> None:
        game.aliens.update()
        for alien in game.aliens.sprites():
            if alien.check_edges():
                for fleet_alien in game.aliens.sprites():
                    fleet_alien.rect.y += game.settings.fleet_drop_speed
                game.settings.fleet_direction *= -1
                break
