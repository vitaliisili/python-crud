from model.base import Base


class User(Base):
    def __init__(self, id, username: str, password: str):
        super().__init__(id)
        self.__username: str = username
        self.__password: str = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    def __repr__(self):
        return f"User({super().id}, {self.__username}, {self.__password})"

