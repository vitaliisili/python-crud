from abc import ABC, abstractmethod


class CrudService(ABC):

    @abstractmethod
    def get(self, value):
        ...

    @abstractmethod
    def persist(self, value):
        ...

    @abstractmethod
    def delete(self, value):
        ...

    @abstractmethod
    def update(self, id, value):
        ...
