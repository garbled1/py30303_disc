"""Performs general tests."""
# import amodule
# from src.py30303_disc.libs import py30303_disc
from py30303_disc.libs import py30303_disc

# def test_amodule():
#     """Test amodule.hello()."""
#     amodule.hello()


def test_true():
    """Just asserts True."""
    assert True

    
def test_py30303_disc():
    """Very basic testing."""
    s = py30303_disc.d30303()

    s.send_discovery()
    s.end_discovery()
