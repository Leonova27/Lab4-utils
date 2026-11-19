# 1. Базовый образ. 
FROM python:3.11-slim
# 2. Установка системных зависимостей
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends build-essential gcc && \ 
    rm -rf /var/lib/apt/lists/*
# 3. Рабочая директория внутри контейнера. 
WORKDIR /app
# 4. Копируем только файлы зависимостей и устанавливаем их.
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
# 5. Копируем файлы сборки и исходный код.
COPY setup.py . 
COPY src/ ./src/ 
COPY tests/ ./tests/
# 6. Устанавливаем ВАШ пакет в режиме "editable" (-e).
RUN pip install -e .
# 7. Команда по умолчанию.
CMD ["pytest", "-q"]