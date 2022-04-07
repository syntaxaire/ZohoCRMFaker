"""Unit tests for fakers.py"""
from fakers import FakeCustomer


def test_name():
    """Test fake customer name generation"""
    _ = FakeCustomer()
    assert isinstance(_.name, str)
    assert len(_.name) > 5


def test_address():
    """Test fake customer address generation"""
    _ = FakeCustomer()
    assert isinstance(_.address, str)
    assert len(_.address) > 5


def test_phone():
    """Test fake customer address generation"""
    _ = FakeCustomer()
    assert isinstance(_.phone, str)
    assert len(_.phone) > 5
