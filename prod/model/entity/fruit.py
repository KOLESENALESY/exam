from prod.model.entity import *


class Fruit(Sweet):
    def __init__(self, name, price, mass, calories, kind_of_fruit=""):
        super().__init__(name, price, mass, calories)
        self.kind_of_fruit = kind_of_fruit
