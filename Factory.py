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

class CoffeeShop(ABC):

    def order_coffee(self):
        coffee = self.create_coffee()
        coffee.prepare()

    @abstractmethod
    def create_coffee(self):
        pass


class ItalianCoffeeShop(CoffeeShop):

    def create_coffee(self):
        return Espresso()


class FrenchCoffeeShop(CoffeeShop):

    def create_coffee(self):
        return Latte()