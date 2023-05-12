import time
from model.user import User
from service.crud_service import CrudService
from db.user_db import user_db


class UserService(CrudService):
    def get(self, username: str):
        for user in user_db:
            if user.username == username:
                return user
        print(f"User with username: {username} not found")

    def persist(self, user: User):
        user_db.append(user)

    def delete(self, user: User):
        user_db.remove(user)

    def update(self, id, user: User):
        user_to_update: User = None
        user_index: int = None

        for index, u in enumerate(user_db):
            if u.id == id:
                user_to_update = u
                user_index = index

        if user_to_update is None:
            print(f"User with id: {id} not found")
            return

        user_to_update.username = user.username
        user_to_update.password = user.password
        user_to_update.update_date = time.ctime(time.time())

        user_db[user_index] = user_to_update


