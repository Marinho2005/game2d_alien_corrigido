from typing import Any, Protocol


class EventProcessor(Protocol):
    def process(self, game: Any) -> None:
        ...


class FleetService(Protocol):
    def create(self, game: Any) -> None:
        ...

    def update(self, game: Any) -> None:
        ...


class CollisionService(Protocol):
    def update_bullets(self, game: Any) -> None:
        ...

    def check_bullet_alien(self, game: Any) -> None:
        ...

    def check_ship_alien(self, game: Any) -> None:
        ...


class RendererService(Protocol):
    def draw(self, game: Any) -> None:
        ...
