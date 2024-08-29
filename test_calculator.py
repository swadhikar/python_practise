from app import calculator
from app.calculator import InvalidUserDataException
import math
import pytest

def test_addition():
    assert calculator.add(1, 2) == 3

def test_square_root():
    assert int(calculator.square_root(9)) == 3 

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_dict():
    data_dict = {
        "name": "swadhikar",
        "age": 34
    }
    return data_dict

def test_multiply(sample_list):
    assert calculator.multiply_numbers(sample_list) == 120

def test_add_numbers(sample_list):
    assert calculator.add_numbers(sample_list) == 15

# @pytest.fixture
# def text_substring_fixture():
    
#     return list_of_strings
list_of_strings = [
        ('Hello world', 'world'),
        ('rain rain go away', 'Rain go'),
        ('cook with comali (cwc) season-5', 'cwc')
    ]

@pytest.mark.parametrize("text, sub_text", list_of_strings)
def test_is_substring(text, sub_text):
    assert calculator.is_substring(text, sub_text)


test_fixture = [
    ('name', 'swadhikar'),
    ('age', 34),
    ('salary', None)
]

@pytest.mark.parametrize("key, value", test_fixture)
def test_dictionary(sample_dict, key, value):
    assert sample_dict.get(key) == value


def test_process_user_data():
    data = {"age": 34, "name": "swadhikar"}
    assert calculator.process_user_data(data) == True

def test_process_user_data_invalid_age():
    invalid_user = {"name": "swadhikar", "age": -30}
    with pytest.raises(InvalidUserDataException, match="Invalid age"):
        calculator.process_user_data(invalid_user)

def test_process_user_data_0_age():
    invalid_user = {"name": "swadhikar", "age": 0}
    with pytest.raises(InvalidUserDataException, match="Invalid age"):
        calculator.process_user_data(invalid_user)


def test_process_user_data_invalid_username():
    invalid_user = {"age": 34}
    with pytest.raises(InvalidUserDataException, match="User name is required"):
        calculator.process_user_data(invalid_user)