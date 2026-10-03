import pytest

from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("Moscow", "Moscow"),
    ("s", "S"),
    ("london is a capital of Great Britain", "London is a capital of great britain"),
    ("sTadiuM", "Stadium"),
    ("PYTHON", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("     ", "     "),
    ("?!", "?!"),
    ("30.09.1998", "30.09.1998"),
    ("p1Leer", "P1leer"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("Skypro", "Skypro"),
    (" Moscow ", "Moscow "),
    (" 123", "123"),
    ("London is a capital of Great Britain", "London is a capital of Great Britain")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (None, None)
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Moscow", "o", True),
    ("Python", "i", False),
    ("Spartak Moscow", " ", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (None, "a", False),
    ("SkyPro", None, False),
    ("Spartak", "", False),
    ("Moscow", "1", False),
    ("Season", "ea", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Study", "dy", "Stu"),
    ("Attention", "t", "Aenion"),
    ("Moscow", "X", "Moscow")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (None, "a", None),
    ("SkyPro", None, None),
    ("Moscow", "", "Moscow"),
    ("SkyPro", 123, None)
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected