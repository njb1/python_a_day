import pytest
from src.easy import (
    can_enter_club,
    pass_fail,
    is_divisible_by_five,
    replace_smiley,
    convert_to_titlecase,
    number_to_dashes,
    add_ends,
)

def test_can_enter_club(return_ages):
    underage, age, overage = return_ages
    assert can_enter_club(underage) == False
    assert can_enter_club(age) == True
    assert can_enter_club(overage) == True

def test_pass_fail(return_scores):
    fail_score, hit_score, pass_score = return_scores
    assert pass_fail(fail_score) == "Fail"
    assert pass_fail(hit_score) == "Pass"
    assert pass_fail(pass_score) == "Pass"

def test_is_divisible_by_five():
    assert is_divisible_by_five(10) == True
    assert is_divisible_by_five(11) == False
    assert is_divisible_by_five(15) == True
    assert is_divisible_by_five(0) == True
    assert is_divisible_by_five(-5) == True

def test_replace_smiley():
    assert replace_smiley("Hello :)") == "Hello 😊"
    assert replace_smiley("No smiley here") == "No smiley here"
    assert replace_smiley("Multiple :) smileys :)") == "Multiple 😊 smileys 😊"
    assert replace_smiley("") == ""
    assert replace_smiley("Just a text without smiley") == "Just a text without smiley"

def test_convert_to_titlecase():
    assert convert_to_titlecase("hello world") == "Hello World"
    assert convert_to_titlecase("python programming") == "Python Programming"
    assert convert_to_titlecase("a day in the life") == "A Day In The Life"
    assert convert_to_titlecase("") == ""
    assert convert_to_titlecase("123 numbers and symbols !@#") == "123 Numbers And Symbols !@#"

def test_number_to_dashes():
    assert number_to_dashes(0) == ""
    assert number_to_dashes(1) == "-"
    assert number_to_dashes(5) == "-----"
    assert number_to_dashes(10) == "----------"
    assert number_to_dashes(3) == "---"

def test_add_ends():
    assert add_ends([1, 2, 3, 4]) == 5
    assert add_ends([2, 3, 4, 5]) == 7
    assert add_ends([]) == 0
    assert add_ends([10]) == 20
    with pytest.raises(TypeError):
        add_ends("not a list")
