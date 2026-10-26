from abc import ABC, abstractmethod
from typing import Any, Iterable


class FleetFormation(ABC):
    """Define o contrato para posicionar uma frota de aliens."""

    @abstractmethod
    def positions(self, game: Any) -> Iterable[tuple[int, int]]:
        """Retorna as posições iniciais dos aliens."""
        raise NotImplementedError


class GridFleetFormation(FleetFormation):
    """Formação padrão em linhas e colunas."""

    def positions(self, game: Any) -> Iterable[tuple[int, int]]:
        alien_width = game.settings.alien_width
        alien_height = game.settings.alien_height
        available_space_x = game.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        available_space_y = game.settings.screen_height - (3 * alien_height) - game.ship.rect.height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                yield (
                    alien_width + 2 * alien_width * alien_number,
                    alien_height + 2 * alien_height * row_number,
                )
