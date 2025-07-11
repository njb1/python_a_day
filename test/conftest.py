import pytest

@pytest.fixture(scope="session")
def return_ages():
    underage = 15
    age = 21
    overage = 30
    return underage, age, overage

@pytest.fixture(scope="session")
def return_scores():
    return [49, 50, 51]