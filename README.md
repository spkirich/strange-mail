# Странная почта

Telegram-бот для непредсказуемого обмена сообщениями между двумя
людьми.

## Установка

Клонируйте репозиторий:

```
$ git clone https://github.com/spkirich/strange-mail.git
```

Установите зависимости:

```
$ pip install -r requirements.txt
```

Настройте окружение:

```
$ export SM_TOKEN=<Токен Telegram-бота>
$ export SM_USER1=<ID пользователя № 1>
$ export SM_USER2=<ID пользователя № 2>
```

ID пользователя можно получить с помощью
[этого бота](https://t.me/getmyid_bot).

## Запуск

**После настройки окружения** выполните следующую команду:

```
$ python bot.py
```

Готово!
