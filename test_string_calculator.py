from string_calculator import StringCalculator
import pytest


def test_when_empty_string_return_zero():
    assert StringCalculator().add("") == 0


def test_when_one_numbers_then_return_same_number():
    assert StringCalculator().add("1") == 1


def test_when_two_numbers_then_return_sum():
    assert StringCalculator().add("1,2") == 3


def test_when_numbers_divided_by_new_line_then_return_sum():
    assert StringCalculator().add("1\n2,3") == 6


def test_when_different_delimiter_then_return_sum():
    assert StringCalculator().add("//;\n1;2;3") == 6


def test_when_negative_then_throw_not_allowed():
    with pytest.raises(RuntimeError) as exception_info:
        StringCalculator().add("1,4,-1")
    assert 'negatives not allowed: -1' in str(exception_info.value)


def test_when_big_number_then_ignore_it():
    assert StringCalculator().add("1001,2") == 2
