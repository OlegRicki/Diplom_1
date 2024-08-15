import pytest
from unittest.mock import patch
from unittest.mock import Mock

from praktikum.database import Database


class TestDatabase:
    @patch('praktikum.database.Bun')
    def test_available_buns(self, mock_bun):
        bun_black = Mock()
        bun_black.name = 'black bun'
        bun_black.price = 100

        bun_white = Mock()
        bun_white.name = 'white bun'
        bun_white.price = 200

        bun_red = Mock()
        bun_red.name = 'red bun'
        bun_red.price = 300

        mock_bun.side_effect = [bun_black, bun_white, bun_red]

        # Создание экземпляра Database
        database = Database()
        available_buns = database.available_buns()
        assert len(available_buns) == 3
        assert available_buns[0].name == 'black bun'
        assert available_buns[0].price == 100
        assert available_buns[1].name == 'white bun'
        assert available_buns[1].price == 200
        assert available_buns[2].name == 'red bun'
        assert available_buns[2].price == 300

    @patch('praktikum.database.Ingredient')
    def test_available_ingredients(self, ingredient_mock):
        mock_sauce_hot = Mock()
        mock_sauce_hot.type = 'sauce'
        mock_sauce_hot.name = 'hot sauce'
        mock_sauce_hot.price = 100

        mock_sauce_sour = Mock()
        mock_sauce_sour.name = "sour cream"
        mock_sauce_sour.type = "sauce"
        mock_sauce_sour.price = 200

        mock_sauce_chili = Mock()
        mock_sauce_chili.name = "chili sauce"
        mock_sauce_chili.type = "sauce"
        mock_sauce_chili.price = 300

        mock_filling_cutlet = Mock()
        mock_filling_cutlet.name = "cutlet"
        mock_filling_cutlet.type = "filling"
        mock_filling_cutlet.price = 100

        mock_filling_dinosaur = Mock()
        mock_filling_dinosaur.name = "dinosaur"
        mock_filling_dinosaur.type = "filling"
        mock_filling_dinosaur.price = 200

        mock_filling_sausage = Mock()
        mock_filling_sausage.name = "sausage"
        mock_filling_sausage.type = "filling"
        mock_filling_sausage.price = 300

        ingredient_mock.side_effect = [mock_sauce_hot, mock_sauce_sour, mock_sauce_chili,
                                       mock_filling_cutlet, mock_filling_dinosaur, mock_filling_sausage]

        # Создание экземпляра Database
        database = Database()
        available_ingredients = database.available_ingredients()

        assert len(available_ingredients) == 6
        assert available_ingredients[0].name == 'hot sauce'
        assert available_ingredients[0].type == 'sauce'
        assert available_ingredients[0].price == 100

        assert available_ingredients[1].name == 'sour cream'
        assert available_ingredients[1].type == 'sauce'
        assert available_ingredients[1].price == 200

        assert available_ingredients[2].name == 'chili sauce'
        assert available_ingredients[2].type == 'sauce'
        assert available_ingredients[2].price == 300

        assert available_ingredients[3].name == 'cutlet'
        assert available_ingredients[3].type == 'filling'
        assert available_ingredients[3].price == 100

        assert available_ingredients[4].name == 'dinosaur'
        assert available_ingredients[4].type == 'filling'
        assert available_ingredients[4].price == 200

        assert available_ingredients[5].name == 'sausage'
        assert available_ingredients[5].type == 'filling'
        assert available_ingredients[5].price == 300


