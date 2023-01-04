FROM python:3.10-slim

WORKDIR /app

# Положим файлы в контейнер.
COPY requirements.txt src ./

# Установим указанные зависимости.
RUN pip install -r requirements.txt

# Укажем команду запуска бота.
ENTRYPOINT ["python", "bot.py"]
