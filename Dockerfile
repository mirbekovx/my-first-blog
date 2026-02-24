FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем зависимости (минимум Django)
RUN pip install --no-cache-dir "django>=6.0.2" psycopg2-binary

# Копируем проект внутрь контейнера
COPY . /app

# По умолчанию будем запускать dev-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]