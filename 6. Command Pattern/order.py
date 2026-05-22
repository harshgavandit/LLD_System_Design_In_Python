from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def execute(self):
        pass
