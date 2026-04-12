import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize( 'num1, num2, result', [ (4,5,9), (-6,-10,-16), (-6, 6, 0), (5.60, 4.40, 10), (10, 0, 10) ] )
def test_sum_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.parametrize( 'nums, result', [ ([], 0), ([1,2,3,4,5,6,7,8,9,], 5),] )
def test_avg_list(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result

def test_div_positive(): #проверка деления чисел
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero(): #проверка деления на ноль
    calculator = Calculator()
    res = calculator.div(10, 0)
    assert res == None

# def test_sum_negative_nums():
#     calculator = Calculator()
#     res = calculator.sum(-6, -10)
#     assert res == -16
#
# def test_sum_positive_and_negative_nums():
#     calculator = Calculator()
#     res = calculator.sum(-6, 6)
#     assert res == 0
#
# @pytest.mark.positive_test
# def test_sum_float_nums(): #проверка сложения десятичных дробей
#     calculator = Calculator()
#     res = calculator.sum(5.6, 4.3)
#     res = round(res, 1)
#     assert res == 9.9

# def test_sum_zero_nums(): #проверка сложения целого числа и нуля
#     calculator = Calculator()
#     res = calculator.sum(10, 0)
#     assert res == 10
#
#
# def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
#     calculator = Calculator()
#     numbers = []
#     res = calculator.avg(numbers)
#     assert res == 0
#
# def test_avg_positive(): #проверка нахождения среднего для списка
#     calculator = Calculator()
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
#     res = calculator.avg(numbers)
#     assert res == 5

print('finish')
