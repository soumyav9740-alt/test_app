def test_basic():
    assert 1 + 1 == 2

def test_app_import():
    from app import app
    assert app is not None