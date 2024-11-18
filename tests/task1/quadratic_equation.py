import pytest
import math


# Раздел "Функции - использование встроенных и создание собственных"
# Задание «Квадратное уравнение»
def discriminant(a, b, c):
    d = math.pow(b, 2) - 4 * a * c
    return d

def solution(a, b, c):
    d = discriminant(a, b, c)
    if d == 0 and a != 0:
        return -b / (2 * a)
    elif d > 0 > a != 0:
        return (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)
    elif d > 0 and a != 0 and a > 0:
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
    else:
        return "корней нет"


@pytest.mark.parametrize(
        'a,b,c,expected',
        (
            (1, 8, 15, 4.0),
            (1, -13, 12, 121.0),
            (-4, 28, -49, 0.0),
            (1, 1, 1, -3.0)
        )
)
def test_discriminant(a, b, c, expected):
    result = discriminant(a, b, c)
    assert result == expected


@pytest.mark.parametrize(
        'a,b,c,expected',
        (
            (1, 8, 15, (-3.0, -5.0)),
            (1, -13, 12, (12.0, 1.0)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет')
        )
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected
