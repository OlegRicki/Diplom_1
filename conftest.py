import pytest
from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_mock():
    bun_mock = Mock()

    bun_mock.get_price.return_value = 100
    bun_mock.get_name.return_value = 'black bun'
    return bun_mock


@pytest.fixture
def sauce_mock():
    sauce_mock = Mock()
    sauce_mock.get_price.return_value = 100
    sauce_mock.get_name.return_value = 'hot sauce'
    sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce_mock


@pytest.fixture
def cutlet_mock():
    cutlet_mock = Mock()
    cutlet_mock.get_price.return_value = 100
    cutlet_mock.get_name.return_value = 'cutlet'
    cutlet_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return cutlet_mock


@pytest.fixture
def chill_mock():
    chill_mock = Mock()
    chill_mock.get_price.return_value = 100
    chill_mock.get_name.return_value = 'chili sauce'
    chill_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return chill_mock
