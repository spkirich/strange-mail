import json
import os
import random


class Box:
    """Почтовый ящик."""

    def __init__(self, path: str):
        """Инициализировать почтовый ящик.

        path: str
            Путь к файлу почтового ящика.
        """

        self.path = path

        if not os.path.exists(self.path):
            with open(self.path, "w") as file:
                json.dump([], file)

    def get(self):
        """Взять случайное сообщение."""

        with open(self.path, "r") as file:
            mail = json.load(file)

        # Идентификатор выбранного сообщения
        message_id = random.randrange(len(mail))

        # Выбранное сообщение
        message = mail[message_id]

        del mail[message_id]

        with open(self.path, "w") as file:
            json.dump(mail, file)

        return message

    def put(self, message: str):
        """Положить сообщение.

        message: str
            Сообщение.
        """

        with open(self.path, "r") as file:
            mail = json.load(file)

        mail.append(message)

        with open(self.path, "w") as file:
            json.dump(mail, file)
