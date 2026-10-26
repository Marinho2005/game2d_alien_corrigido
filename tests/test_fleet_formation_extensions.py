import pytest

from fleet_formation import FleetFormation, GridFleetFormation


@pytest.mark.parametrize(
    ("screen_width", "expected_columns"),
    [(800, 7), (1200, 11), (1600, 15)],
)
def test_grid_formation_scales_with_screen_width(
    screen_width: int, expected_columns: int
) -> None:
    game = type("Game", (), {})()
    game.settings = type("Settings", (), {})()
    game.settings.screen_width = screen_width
    game.settings.screen_height = 800
    game.settings.alien_width = 50
    game.settings.alien_height = 50
    game.ship = type("Ship", (), {})()
    game.ship.rect = type("Rect", (), {"height": 50})()

    positions = list(GridFleetFormation().positions(game))

    assert len(positions) == expected_columns * 6


def test_alternative_formation_can_follow_the_same_contract() -> None:
    class DiagonalFormation(FleetFormation):
        def positions(self, game: object) -> list[tuple[int, int]]:
            return [(10, 10), (20, 20), (30, 30)]

    formation = DiagonalFormation()

    assert list(formation.positions(object())) == [(10, 10), (20, 20), (30, 30)]
