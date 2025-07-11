import pytest
from src.easy import can_enter_club, pass_fail

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