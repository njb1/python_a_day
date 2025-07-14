import pytest

from src.hard import is_disarium_number, ginortS, move_zeroes_to_end, coin_change

def test_is_disarium_number():
    assert is_disarium_number(123) == False
    assert is_disarium_number(175) == True
    assert is_disarium_number(518) == True
    assert is_disarium_number(100) == False


def test_is_ginortS():
    my_string = "123ABCcde"
    my_sorted_string = "cdeABC123"

    assert ginortS(my_string) == my_sorted_string


def test_move_zeroes_to_end():
    assert move_zeroes_to_end(10203) == "12300"

def test_coin_change():
    coins = [1, 5, 10, 25]
    amount = 63
    assert coin_change(coins, amount) == 6  # 2x25 + 1x10 + 3x1
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3  # 5 + 5 + 1