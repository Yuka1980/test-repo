import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitilize():
    """POSITIVE"""
    assert utils.capitilize("skypro") == "skypro"
    assert utils.capitilize("hello world") == "hello world"
    assert utils.capitilize("123") == "123"
    """NEGATIVE"""

    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12345тест") == "12345тест"