from types import SimpleNamespace

from fleet_formation import FleetFormation, GridFleetFormation


def make_game() -> SimpleNamespace:
    settings = SimpleNamespace(
        screen_width=1200,
        screen_height=800,
        alien_width=50,
        alien_height=50,
    )
    ship = SimpleNamespace(rect=SimpleNamespace(height=50))
    return SimpleNamespace(settings=settings, ship=ship)


def test_grid_formation_implements_fleet_formation() -> None:
    formation = GridFleetFormation()

    assert isinstance(formation, FleetFormation)


def test_grid_formation_creates_expected_number_of_positions() -> None:
    positions = list(GridFleetFormation().positions(make_game()))

    assert len(positions) == 11 * 6


def test_grid_formation_starts_at_one_alien_spacing() -> None:
    positions = list(GridFleetFormation().positions(make_game()))

    assert positions[0] == (50, 50)
    assert positions[1] == (150, 50)
    assert positions[-1] == (1050, 550)
