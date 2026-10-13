# math_utils 
Простые утилиты статистики для работы с числовыми последовательностями.
Библиотека math_utils предоставляет базовые статистические функции для работы с числовыми последовательностями: вычисление среднего арифметического и дисперсии
# 2. Создание и активация виртуального окружения 
# Создание python 
-m venv .venv 
# Активация (Windows PowerShell) 
.venv\Scripts\Activate.ps1 
# Активация (Windows CMD) 
.venv\Scripts\activate.bat 
### 3. Обновление pip и установка зависимостей 
pip install --upgrade pip 
pip install -r requirements.txt 
# ИЛИ, если используется Poetry 
# poetry install
# В активированном виртуальном окружении 
pytest -q 
# Покрытие тестами (опционально) 
coverage run -m pytest 
coverage report -m
# Сборка пакета
pip install build 
python -m build 
# Готовые файлы появятся в папке dist/