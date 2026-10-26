from settings import Settings


def test_settings_define_screen_dimensions() -> None:
    settings = Settings()

    assert settings.screen_width == 1200
    assert settings.screen_height == 800
    assert settings.bg_color == (230, 230, 230)


def test_settings_define_bullet_limit() -> None:
    settings = Settings()

    assert settings.bullet_allowed == 1
    assert settings.bullet_width > 0
    assert settings.bullet_height > 0
