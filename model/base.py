import time


class Base:
    def __init__(self, id: int):
        self.__id = id
        self.__creation_date = time.ctime(time.time())
        self.__update_date = time.ctime(time.time())

    @property
    def id(self):
        return self.__id

    @property
    def creation_date(self):
        return self.__creation_date

    @property
    def update_date(self):
        return self.__update_date

    @update_date.setter
    def update_date(self, value: str):
        self.__update_date = value
