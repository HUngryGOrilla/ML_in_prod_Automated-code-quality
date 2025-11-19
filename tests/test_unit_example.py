from app import create_app


def test_normalize_item_name_strips_spaces_and_lowercases():
    app = create_app()
    func = app.normalize_item_name

    assert func("  Hello World  ") == "hello world"


def test_normalize_item_name_handles_none():
    app = create_app()
    func = app.normalize_item_name

    assert func(None) == ""