from model.base import Base
from model.user import User


class Order(Base):
    def __init__(self, id, name: str, date: str):
        super().__init__(id)
        self.__name = name
        self.__date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    def __repr__(self):
        return f"Order({super().id}, {self.__name}, {self.__date})"
