import pytest


def test_plus_operator():
    a = 3
    b = 4
    correct_sum = 7
    assert(correct_sum == a+b)


def test_multiply_operator():
    a = 3
    b = 4
    correct_product = 12
    assert(correct_product == a+b)


@pytest.mark.parametrize("subtraction_term_1, subtraction_term_2, expected_result",
                         [
                             (1, 3, -2),
                             (4, 3, 1),
                             (7, 0, 7),
                             (-1, -1, 0),
                             (0, 0, 1)
                         ]
                        )
def test_subract_operator(subtraction_term_1, subtraction_term_2, expected_result):
    assert(expected_result == subtraction_term_1 - subtraction_term_2)