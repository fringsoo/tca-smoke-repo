from tca_smoke import greeting


def test_greeting() -> None:
    assert greeting("team") == "Hello from A1, team!"
