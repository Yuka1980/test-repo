import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitilize"""

def test_capitilize():
    """POSITIVE"""
    assert utils.capitilize("Skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("123") == "123"
    """NEGATIVE"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12345тест") == "12345тест"




"""trim"""

def test_trim():
    """POSITIVE"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("   hello world  ") == "hello world  "
    assert utils.trim(" SKY ") == "SKY  "
    """NEGATIVE"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_imput():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("  SKY  ") == "  SKY  "



"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
# POSITIVE
("яблоко,банан,апельсин", ", ", ["яблоко", "банан", "апельсин"]),
("1,2,3,4,5", ", ", ["1", "2", "3", "4", "5"]),
("*@#$#$#$", "@", ["*", "#", "@"]),
# NEGATIVE
("", None, []),
("1,2,3,4 5", None, ["1", "2", "3", "4 5"]), 
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result




"""contains"""

@pytest.mark.parametrize("string, symbol, result", [

    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир ", "р", True),
    ("диван-кровать", "-", True),
    ("123", "1", True),
    ("", "", True),
    ("Москва", "м", False),
    ("привет", "з", False),
    ("КОТ", "№", False),
    ("", "3", False),
    ("12345", "h", False),
    ("hello", "", False) # ошибка, некорректная работа со строкой
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result



"""delete_symbol"""

@pytest.mark.parametrize("string, symbol, result", [
    
    ("море", "м", "оре"),
    ("Юля", "л", "Юя"),
    ("54321", "3", "5421"),
    ("Красная Поляна", " ", "КраснаяПоляна"),

    ("ёжик", "р", "ёжик"),
    ("", "", ""),
    ("", "а", ""),
    ("чай", "", "чай"),
    ("конфета ", " ", "конфета"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result




"""starts_with"""

@pytest.mark.parametrize("string, symbol, result", [

   ("перекресток", "п", True), 
   ("", "", True),
   ("Анапа", "А", True),
   ("Cinema  ", "C", True),
   ("Риал-Мадрид", "Р", True),
   ("54321", "5", True),

   ("Юля", "ю", False),
   ("мир", "М", False),
   ("", "$", False),
   ("фонтан", "х", False),
   ("курица", "л", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""and_with"""

@pytest.mark.parametrize("string, symbol, result", [

   ("Юлия", "я", True), 
   ("КЕКС", "С", True),
   ("", "", True),
   ("енот ", "", True),
   ("54321", "1", True),
   ("NEW balance", "e", True),
   ("Екатерина2", "2", True),
   ("МегА", "А", True),

   ("контракт", "к", False),
   ("миротворец", "м", False),
   ("дверь", "Ь", False),
   ("", "*", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""

@pytest.mark.parametrize("string, result", [

   ("", True), 
   (" ", True),
   ("  ", True),
   
   ("не пусто", False),
   ("  не пусто с пробелом в начале строки", False),
   ("54321", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""

@pytest.mark.parametrize("lst, joiner, result", [

    (["s", "o", "s"], ", ", "s, o, s"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
    (["в", "у", "з"], "", "вуз"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result



















   

   





    






