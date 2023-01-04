# Странная почта

Telegram-бот для непредсказуемого обмена сообщениями между двумя
людьми.

## Установка и запуск

Установка и запуск приложения могут быть выполнены как с помощью Docker, так и
без этих новомодных штучек. На всякий случай рассмотрим оба способа.

### Docker Way

Клонируйте репозиторий:

``` bash
git clone https://github.com/spkirich/strange-mail.git
```

Соберите образ:

``` bash
docker build -t strange-mail strange-mail
```

Создайте том для хранения сообщений:

``` bash
docker volume create sm-data
```

Запустите контейнер:

``` bash
docker run -d --mount type=volume,src=sm-data,target=/app/data strange-mail
```

### Без использования Docker

Клонируйте репозиторий:

``` bash
git clone https://github.com/spkirich/strange-mail.git
```

Установите зависимости:

``` bash
pip install -r strange-mail/requirements.txt
```

Настройте окружение:

``` bash
export SM_TOKEN=<Токен Telegram-бота>
export SM_USER1=<ID пользователя № 1>
export SM_USER2=<ID пользователя № 2>
```

ID пользователя можно получить с помощью
[этого бота](https://t.me/getmyid_bot).

Для запуска просто выполните следующую команду:

``` bash
python strange-mail/bot.py
```
