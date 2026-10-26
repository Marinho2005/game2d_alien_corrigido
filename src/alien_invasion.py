from typing import Any

import pygame

from bullet import Bullet
from collision_manager import CollisionManager
from event_handler import EventHandler
from fleet_formation import GridFleetFormation
from fleet_manager import FleetManager
from game_components import (
    CollisionService,
    EventProcessor,
    FleetService,
    RendererService,
)
from renderer import Renderer
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Coordena os componentes do jogo e seu laço principal."""

    def __init__(
        self,
        event_handler: EventProcessor | None = None,
        fleet_manager: FleetService | None = None,
        collision_manager: CollisionService | None = None,
        renderer: RendererService | None = None,
    ) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.event_handler = event_handler or EventHandler()
        self.fleet_manager = fleet_manager or FleetManager(GridFleetFormation())
        self.collision_manager = collision_manager or CollisionManager()
        self.renderer = renderer or Renderer()

    def fire_bullet(self) -> None:
        """Cria um projétil respeitando o limite configurado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(Bullet(self.screen, self.settings, self.ship))

    def run_game(self) -> None:
        """Executa o fluxo principal delegando cada responsabilidade."""
        self.fleet_manager.create(self)
        while True:
            self.event_handler.process(self)
            self.ship.update()
            self.collision_manager.update_bullets(self)
            self.collision_manager.check_bullet_alien(self)
            self.fleet_manager.update(self)
            self.collision_manager.check_ship_alien(self)
            self.renderer.draw(self)


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
