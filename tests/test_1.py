"""Performs general tests."""
# import amodule
from py30303_disc.libs import py30303_disc as d30303


# def test_amodule():
#     """Test amodule.hello()."""
#     amodule.hello()


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    s = d30303.SampleClass()
    assert s.true() is True


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    assert d30303.SampleClass.false() is False
