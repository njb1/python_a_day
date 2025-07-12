import pytest
import random


@pytest.fixture(scope="session")
def return_ages():
    underage = 15
    age = 21
    overage = 30
    return underage, age, overage


@pytest.fixture(scope="session")
def return_scores():
    fail_score = 49
    hit_score = 50
    pass_score = 51
    return fail_score, hit_score, pass_score


@pytest.fixture(scope="session")
def return_random_credit_card():
    cc_dict = {
        "4444-4444-4444-4444": "************4444",
        "1234-5678-9012-3456": "************3456",
        "1234-5678-9012-345": "***********345",
    }
    key = random.choice(list(cc_dict.keys()))
    value = cc_dict.get(key)
    return key, value