from prod.model.entity import *


class Chocolate(Sweet):
    def __init__(self, name, price, mass, calories, type=""):
        super().__init__(name, price, mass, calories)
        self.type = type
