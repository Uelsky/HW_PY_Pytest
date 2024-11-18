import pytest


# Раздел "Функции - использование встроенных и создание собственных"
# Задание «Голосование»
def vote(votes):
    max_count, res = 0, 0
    for i in votes:
        a = votes.count(i)
        if a > max_count:
            max_count = a
            res = i
    return res


@pytest.mark.parametrize(
    'votes,expected',
    (
        ([1,1,1,2,3], 1),
        ([1,2,3,2,2], 2)
    )
)
def test_vote(votes, expected):
    result = vote(votes)
    assert result == expected
