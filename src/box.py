import json
import os
import random


class Box:
    """Почтовый ящик."""

    def __init__(self, data: str, path: str):
        """Инициализировать почтовый ящик.

        data: str
            Путь к директории почтовых ящиков.

        path: str
            Относительный путь к файлу почтового ящика.
        """

        self.data = data
        self.path = path

        if not os.path.exists(self.data):
            os.mkdir(self.data)

        if not os.path.exists(os.path.join(self.data, self.path)):
            with open(os.path.join(self.data, self.path), "w") as file:
                json.dump([], file)

    def get(self):
        """Взять случайное сообщение."""

        with open(os.path.join(self.data, self.path), "r") as file:
            mail = json.load(file)

        if len(mail) == 0:
            return "К сожалению, пока ящик пуст..."

        # Идентификатор выбранного сообщения
        message_id = random.randrange(len(mail))

        # Выбранное сообщение
        message = mail[message_id]

        del mail[message_id]

        with open(os.path.join(self.data, self.path), "w") as file:
            json.dump(mail, file)

        return message

    def put(self, message: str):
        """Положить сообщение.

        message: str
            Сообщение.
        """

        with open(os.path.join(self.data, self.path), "r") as file:
            mail = json.load(file)

        mail.append(message)

        with open(os.path.join(self.data, self.path), "w") as file:
            json.dump(mail, file)
