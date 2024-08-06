import pytest
from praktikum.bun import Bun


class TestBun:
    data = [['engl_test', 100], ['русс_тест', 200]]

    @pytest.mark.parametrize('name, price', data)
    def test_get_price_bun(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name, price', data)
    def test_get_name_bun(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
