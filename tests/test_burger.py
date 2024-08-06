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

    def test_create_burger_check_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()

        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = 'black bun'

        sauce_mock = Mock()
        sauce_mock.get_price.return_value = 100
        sauce_mock.get_name.return_value = 'hot sauce'
        sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        cutlet_mock = Mock()
        cutlet_mock.get_price.return_value = 100
        cutlet_mock.get_name.return_value = 'cutlet'
        cutlet_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.set_buns(bun=bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(cutlet_mock)
        assert burger.get_receipt() == ('(==== black bun ====)\n'
                                        '= sauce hot sauce =\n'
                                        '= sauce cutlet =\n'
                                        '(==== black bun ====)\n'
                                        '\n'
                                        'Price: 400')

    def test_create_burger_check_move_ingredient(self):
        burger = Burger()
        bun_mock = Mock()

        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = 'black bun'

        sauce_mock = Mock()
        sauce_mock.get_price.return_value = 100
        sauce_mock.get_name.return_value = 'hot sauce'
        sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        cutlet_mock = Mock()
        cutlet_mock.get_price.return_value = 100
        cutlet_mock.get_name.return_value = 'cutlet'
        cutlet_mock.get_type.return_value = INGREDIENT_TYPE_FILLING

        chill_mock = Mock()
        chill_mock.get_price.return_value = 100
        chill_mock.get_name.return_value = 'chili sauce'
        chill_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

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

    def test_create_burger_remove_ingredient(self):
        burger = Burger()
        bun_mock = Mock()

        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = 'black bun'

        sauce_mock = Mock()
        sauce_mock.get_price.return_value = 100
        sauce_mock.get_name.return_value = 'hot sauce'
        sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

        cutlet_mock = Mock()
        cutlet_mock.get_price.return_value = 100
        cutlet_mock.get_name.return_value = 'cutlet'
        cutlet_mock.get_type.return_value = INGREDIENT_TYPE_FILLING

        chill_mock = Mock()
        chill_mock.get_price.return_value = 100
        chill_mock.get_name.return_value = 'chili sauce'
        chill_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE

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
    # def test_create_burger_add_ingredient(self):
    #     burger = Burger()
    #     bun_mock = Mock()
    #
    #     bun_mock.get_price.return_value = 100
    #     bun_mock.get_name.return_value = 'black bun'
    #
    #     sauce_mock = Mock()
    #     sauce_mock.get_price.return_value = 100
    #     sauce_mock.get_name.return_value = 'hot sauce'
    #     sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    #
    #     cutlet_mock = Mock()
    #     cutlet_mock.get_price.return_value = 100
    #     cutlet_mock.get_name.return_value = 'cutlet'
    #     cutlet_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    #
    #     chill_mock = Mock()
    #     chill_mock.get_price.return_value = 100
    #     chill_mock.get_name.return_value = 'chili sauce'
    #     chill_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    #
    #     burger.set_buns(bun=bun_mock)
    #     burger.add_ingredient(sauce_mock)
    #     burger.add_ingredient(cutlet_mock)
    #     burger.add_ingredient(chill_mock)
    #
    #     burger.move_ingredient(index=0, new_index=1)
    #     burger.remove_ingredient(2)
    #     assert burger.get_receipt() == ('(==== black bun ====)\n'
    #                                     '= sauce hot sauce =\n'
    #                                     '= filling cutlet =\n'
    #                                     '= sauce chili sauce =\n'
    #                                     '(==== black bun ====)\n'
    #                                     '\n'
    #                                     'Price: 400')
#########

# class MockBun(Bun):
#     def __init__(self, name: str, price: float):
#         self.name = name
#         self.price = price
#
#     def get_name(self) -> str:
#         return self.name
#
#     def get_price(self) -> float:
#         return self.price
#
#
# class MockIngredient(Ingredient):
#     def __init__(self, name: str, price: float, ingredient_type: str):
#         self.name = name
#         self.price = price
#         self.ingredient_type = ingredient_type
#
#     def get_name(self) -> str:
#         return self.name
#
#     def get_price(self) -> float:
#         return self.price
#
#     def get_type(self) -> str:
#         return self.ingredient_type
#
#
# def test_burger():
#     # Создание бургер
#     burger = Burger()
#
#     # Установка булочки
#     bun = MockBun(name='Sesame Bun', price=2.5)
#     burger.set_buns(bun)
#
#     # Добавление ингредиентов
#     lettuce = MockIngredient(name='Lettuce', price=0.5, ingredient_type='Vegetable')
#     cheese = MockIngredient(name='Cheese', price=1.0, ingredient_type='Dairy')
#     bacon = MockIngredient(name='Bacon', price=1.5, ingredient_type='Meat')
#
#     burger.add_ingredient(lettuce)
#     burger.add_ingredient(cheese)
#     burger.add_ingredient(bacon)
#
#     burger.get_price()
#     # Проверка стоимости
#     expected_price = 2 * bun.get_price() + lettuce.get_price() + cheese.get_price() + bacon.get_price()
#     assert burger.get_price() == expected_price
#
#     # Проверка чека
#     expected_receipt = (
#         '(==== Sesame Bun ====)\n'
#         '= vegetable Lettuce =\n'
#         '= dairy Cheese =\n'
#         '= meat Bacon =\n'
#         '(==== Sesame Bun ====)\n'
#         f'Price: {expected_price}'
#     )
#     assert burger.get_receipt() == expected_receipt