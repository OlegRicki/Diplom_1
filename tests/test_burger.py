import pytest

from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    @pytest.mark.parametrize('price_bun, price_sauce, price_cutlet', [[100, 100, 100], [200, 100, 100], [1, 1, 1]])
    def test_create_burger_check_price(self, price_bun, price_sauce, price_cutlet):
        burger = Burger()
        bun_mock = Mock()

        bun_mock.get_price.return_value = price_bun
        bun_mock.get_name.return_value = 'black bun'

        sauce_mock = Mock()
        sauce_mock.get_price.return_value = price_sauce
        sauce_mock.get_name.return_value = 'hot sauce'
        sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        cutlet_mock = Mock()
        cutlet_mock.get_price.return_value = price_cutlet
        cutlet_mock.get_name.return_value = 'cutlet'
        cutlet_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.set_buns(bun=bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(cutlet_mock)
        assert burger.get_price() == (price_bun * 2 + price_sauce + price_cutlet)

    def test_create_burger_check_get_receipt(self, bun_mock, sauce_mock, cutlet_mock):
        burger = Burger()

        burger.set_buns(bun=bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(cutlet_mock)
        assert burger.get_receipt() == ('(==== black bun ====)\n'
                                        '= sauce hot sauce =\n'
                                        '= filling cutlet =\n'
                                        '(==== black bun ====)\n'
                                        '\n'
                                        'Price: 400')

    def test_create_burger_check_move_ingredient(self, bun_mock, sauce_mock, cutlet_mock, chill_mock):
        burger = Burger()


        burger.set_buns(bun=bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(cutlet_mock)
        burger.add_ingredient(chill_mock)

        burger.move_ingredient(index=0, new_index=1)
        assert burger.get_receipt() == ('(==== black bun ====)\n'
                                        '= filling cutlet =\n'
                                        '= sauce hot sauce =\n'
                                        '= sauce chili sauce =\n'
                                        '(==== black bun ====)\n'
                                        '\n'
                                        'Price: 500')

    def test_create_burger_remove_ingredient(self,  bun_mock, sauce_mock, cutlet_mock, chill_mock):
        burger = Burger()


        burger.set_buns(bun=bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(cutlet_mock)
        burger.add_ingredient(chill_mock)

        burger.move_ingredient(index=0, new_index=1)
        burger.remove_ingredient(2)
        assert burger.get_receipt() == ('(==== black bun ====)\n'
                                        '= filling cutlet =\n'
                                        '= sauce hot sauce =\n'
                                        '(==== black bun ====)\n'
                                        '\n'
                                        'Price: 400')
