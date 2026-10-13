# lab4/run_demo.py
from src.math_utils import mean, variance, descriptive_stats

data = [1, 2, 3, 4, 5]
print("mean =", mean(data))
print("variance =", variance(data))

# Проверка descriptive_stats на простом списке (превратим в Series)
import pandas as pd
s = pd.Series(data)
print("descriptive_stats =", descriptive_stats(s))