import pytest


from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize("input_str, output",
[
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),
    ("12 апреля 1961", "12 апреля 1961"),
]
                         )
def test_capitalize_positive(input_str, output):
    assert string_utils.capitalize(input_str) == output

@pytest.mark.parametrize("input_str, output",
[
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
]
                         )

def test_capitalize_negative(input_str, output):
    assert string_utils.capitalize(input_str) == output

@pytest.mark.parametrize("input_str, output",
[
    ("   skypro", "skypro"),
    (" hello", "hello"),
    ("text", "text"),           # негативный
    ("text   ", "text   "),     # негативный
    ("Text   ", "Text   "),     # негативный
])

def test_space_positive_and_negative(input_str, output):

    assert string_utils.trim(input_str)

@pytest.mark.parametrize("string, symbol, expected",
[
    ("SkyPro", "S", True),
    ("SkyPro", "o", True),
]
                         )
def test_contains_positive(string, symbol, expected):

    assert string_utils.contains(string, symbol)

@pytest.mark.parametrize("string, symbol, expected",
[
    ("SkyPro", "U", False),
    ("SkyPro", "s", False),
]
                         )
def test_contains_negative(string, symbol, expected):

    result = string_utils.contains(string, symbol)
    assert result == expected

@pytest.mark.parametrize("input_string, symbol, expected",
[

    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
]
                         )
def test_delete_symbol_positive(input_string, symbol, expected):

    result = string_utils.delete_symbol(input_string, symbol)
    assert result == expected

@pytest.mark.parametrize("input_string, symbol, expected",
[
    ("SkyPro", "x", "SkyPro"),
    ("SkyPro", "s", "SkyPro"),
]
                         )
def test_delete_symbol_negative(input_string, symbol, expected):

    result = string_utils.delete_symbol(input_string, symbol)
    assert result == expected



