from abc import ABC, abstractmethod

class Coffee(ABC):

    @abstractmethod
    def prepare(self):
        pass

class Espresso(Coffee):

    def prepare(self):
        print("Готується еспресо")


class Latte(Coffee):

    def prepare(self):
        print("Готується латте")