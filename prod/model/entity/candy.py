from prod.model.entity import *


class Candy(Sweet):
    def __init__(self, name, price, mass, calories, filling=""):
        super().__init__(name, price, mass, calories)
        self.filling = filling
