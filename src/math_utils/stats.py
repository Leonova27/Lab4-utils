# src/math_utils/stats.py
import numpy as np

def mean(values):
    """Среднее арифметическое"""
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)

def variance(values):
    """Дисперсия (по генеральной совокупности)"""
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)

def descriptive_stats(series):
    """Описательная статистика для pandas Series"""
    s = series.dropna()
    if len(s) == 0:
        return {
            "N": 0, "mean": 0.0, "median": 0.0,
            "min": 0.0, "max": 0.0, "std": 0.0
        }
    return {
        "N": int(len(s)),
        "mean": float(np.round(s.mean(), 1)),
        "median": float(np.round(s.median(), 1)),
        "min": float(np.round(s.min(), 1)),
        "max": float(np.round(s.max(), 1)),
        "std": float(np.round(s.std(), 1)),
    }