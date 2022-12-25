from prod.model.entity import *


class ShopAssistance:
    @staticmethod
    def calculate_total_price(gift):
        if not isinstance(gift, Gift):
            return -1

        total = 0
        for i in range(gift.size()):
            sweet = gift.get(i)
            if isinstance(sweet, Sweet):
                total += sweet.price

        return total

    @staticmethod
    def calculate_total_weight(gift):
        if not isinstance(gift, Gift):
            return -1

        total = 0
        for i in range(gift.size()):
            sweet = gift.get(i)
            if isinstance(sweet, Sweet):
                total += sweet.mass

        return total

    @staticmethod
    def max_cal(gift):
        if not isinstance(gift, Gift):
            return -1

        max_res = 0
        res_name = ""
        for i in range(gift.size()):
            sweet = gift.get(i)
            if isinstance(sweet, Sweet):
                if max_res < sweet.calories:
                    max_res = sweet.calories
                    res_name = sweet.name

        return res_name

    @staticmethod
    def max_price(gift):
        if not isinstance(gift, Gift):
            return -1

        max_res = 0
        res_name = ""
        for i in range(gift.size()):
            sweet = gift.get(i)
            if isinstance(sweet, Sweet):
                if max_res < sweet.price:
                    max_res = sweet.price
                    res_name = sweet.name

        return res_name
