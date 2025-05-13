FROM python:3.9-slim

# Копіювання файлу requirements.txt до Docker
COPY requirements.txt requirements.txt

# Запуск бібліотеки Flask, вказаного у файлі requirements.txt
RUN pip install -r requirements.txt

# Копіювання додатку в Docker
COPY app.py app.py

# Використання порту 5000
EXPOSE 5000

# Команда для запуску додатку (мова - python, app.py - назва файлу з додатком)
CMD ["python", "app.py"]