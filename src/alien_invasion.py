import sys
from typing import Any

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Coordena o jogo sem concentrar todas as regras em um único método."""

    def __init__(self) -> None:
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

    def create_fleet(self) -> None:
        """Cria uma frota de alienígenas distribuída em linhas."""
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                fleet_alien = Alien(self.screen, self.settings)
                fleet_alien.x = alien_width + 2 * alien_width * alien_number
                fleet_alien.rect.x = fleet_alien.x
                fleet_alien.y = alien_height + 2 * alien_height * row_number
                fleet_alien.rect.y = fleet_alien.y
                self.aliens.add(fleet_alien)

    def _check_events(self) -> None:
        """Processa eventos de teclado e encerramento da janela."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: Any) -> None:
        """Atualiza o estado do jogo quando uma tecla é pressionada."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _handle_keyup(self, event: Any) -> None:
        """Atualiza o estado do jogo quando uma tecla é liberada."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """Cria um projétil respeitando o limite configurado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(Bullet(self.screen, self.settings, self.ship))

    def _update_bullets(self) -> None:
        """Move os projéteis e remove os que saíram da tela."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self) -> None:
        """Remove projéteis e aliens atingidos por uma colisão."""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _check_aliens_edges(self) -> None:
        """Desce a frota e inverte sua direção ao alcançar uma borda."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                for fleet_alien in self.aliens.sprites():
                    fleet_alien.rect.y += self.settings.fleet_drop_speed
                self.settings.fleet_direction *= -1
                break

    def _check_ship_alien_collision(self) -> None:
        """Encerra o jogo se um alienígena atingir a nave."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("A nave foi atingida!")
            sys.exit()

    def _update_screen(self) -> None:
        """Desenha o estado atual do jogo na tela."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self) -> None:
        """Executa o laço principal delegando cada responsabilidade."""
        self.create_fleet()
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._check_bullet_alien_collisions()
            self._check_aliens_edges()
            self.aliens.update()
            self._check_ship_alien_collision()
            self._update_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
