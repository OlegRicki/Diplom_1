import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    data = [['engl_test_type', 'engl_test', 100], ['engl_test_type', 'русс_тест', 200]]

    @pytest.mark.parametrize('ingredient_type, name, price', data)
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', data)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', data)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_type() == ingredient_type
