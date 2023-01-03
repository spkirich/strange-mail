FROM python:latest

WORKDIR /app

# Перенесём файлы.
COPY requirements.txt *.py .

# Установим зависимости.
RUN pip install -r requirements.txt

# Установим точку входа.
ENTRYPOINT ["python", "bot.py"]
