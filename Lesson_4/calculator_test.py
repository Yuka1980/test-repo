from calculator import Calculator


calculator = Calculator()

@pytest.mark.skip

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -15)
    assert res == -21

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-5, 5)
    assert res == 0        


def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9  

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_dive_positive_nums():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

#def test_dive_by_zero():
    #alculator = Calculator()
    #res = calculator.sum(10, 0)
    #assert res == None



