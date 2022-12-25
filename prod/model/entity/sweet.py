class Sweet:

    def __init__(self, name="", price=0, mass=0, calories=0):
        self._name = name
        self._price = price
        self._mass = mass
        self._calories = calories

    def __str__(self):
        return f"{self._name} / {self._price} BYN / {self._mass} gr. / {self._calories} cal."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) >= 0:
            self._name = name
        else:
            if not hasattr(self, "_name"):
                self._name = ""
            else:
                raise ValueError("Sweet name was wrong")

    @name.deleter
    def name(self):
        del self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            if not hasattr(self, "_price"):
                self._price = 0
            else:
                raise ValueError("Sweet price was wrong")

    @price.deleter
    def price(self):
        del self._price

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        if mass >= 0:
            self._mass = mass
        else:
            if not hasattr(self, "_mass"):
                self._mass = 0
            else:
                raise ValueError("Sweet mass was wrong")

    @mass.deleter
    def mass(self):
        del self._mass

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if calories >= 0:
            self._calories = calories
        else:
            if not hasattr(self, "_calories"):
                self._calories = 0
            else:
                raise ValueError("Sweet calories was wrong")

    @calories.deleter
    def calories(self):
        del self._calories


