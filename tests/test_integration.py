# tests/test_integration.py
from src.math_utils import mean, variance, descriptive_stats

def test_importable():
    assert callable(mean)
    assert callable(variance)
    assert callable(descriptive_stats)

def test_mean_basic():
    data = [1, 2, 3, 4, 5]
    assert mean(data) == 3.0

def test_variance_basic():
    data = [1, 2, 3, 4, 5]
    # дисперсия по генеральной совокупности: 2.0
    assert variance(data) == 2.0