import pytest

from src.medium import (
    mask_credit_card, 
    is_pronic,
    can_type,
    to_spongecase, 
    is_friday_13,
    harmonic_sum
)


def test_mask_credit_card(return_random_credit_card):
    key, value = return_random_credit_card
    assert mask_credit_card(key) == value
    with pytest.raises(ValueError):
        mask_credit_card("1234")

def test_is_pronic():
    assert is_pronic(2) == True
    assert is_pronic(6) == True  # 2 * (2 + 1)
    assert is_pronic(11) == False  # 3 * (3 + 1)
    assert is_pronic(20) == True  # 4 * (4 + 1)
    assert is_pronic(30) == True

def test_can_type():
    assert can_type("abc", "a") == True
    assert can_type("abc", "d") == False
    assert can_type("abc", "ab") == True
    assert can_type("", "") == True  # Empty string case
    assert can_type("abc", "") == True  # Can type an empty word

def test_to_spongecase():
    assert to_spongecase("hello") == "hElLo"
    assert to_spongecase("world") == "wOrLd"
    assert to_spongecase("") == ""  # Empty string case
    assert to_spongecase("a") == "a"  # Single character case
    assert to_spongecase("ABCD") == "aBcD"  # Mixed case input

def test_is_friday_13():
    assert is_friday_13(1, 2023) == True  # January 13, 2023 is a Friday
    assert is_friday_13(2, 2023) == False  # February 13, 2023 is a Monday
    assert is_friday_13(10, 2023) == True  # October 13, 2023 is a Friday
    assert is_friday_13(12, 2023) == False  # December 13, 2023 is a Wednesday
    assert is_friday_13(5, 2024) == False  # May 13, 2024 is a Monday

def test_harmonic_sum():    
    assert harmonic_sum(5) == 2.28