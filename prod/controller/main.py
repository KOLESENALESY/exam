from prod.model.entity import *
from prod.model.logic.shop_assistance import *

# 1. some sweets

def main():
    compositions = []
    compositions.append(Fruit("Orange", 0.25, 147, 50, "citrus"))
    compositions.append(Fruit("Apple", 0.15, 130, 52, "fruits"))
    compositions.append(Chocolate("Alpen_Gold", 1.50, 90, 357, "dark"))
    compositions.append(Chocolate("Milka", 1.90, 85, 410, "milk"))
    compositions.append(Candy("Barkleys", 7.20, 95, 450, "ledinets"))
    compositions.append(Candy("Toxic_waste", 5.90, 80, 304, "ledinets"))
    compositions.append(Candy("Chupa_Chups", 1.50, 30, 350, "ledinets"))
    compositions.append(Candy("Milky_Way", 0.50, 15, 500, "chocolate"))
    compositions.append(Candy("M&M", 2.20, 150, 550, "chocolate"))
    compositions.append(Candy("Twix", 0.90, 10, 400, "chocolate"))

    print("We have such sweets:")
    count = 1
    for i in compositions:
        print(f"{count}: {i}")
        count += 1

# 2. gift shaping

    print(f"\nWhat sweets do you want to collect a gift from?",
          f"\nList their numbers separated by a space,",
          f"\nfor example: 1 3 3 7\n")
    selected_list = [int(i) for i in input().split()]

    new_year_gift = Gift()

    for i in selected_list:
        new_year_gift.add(compositions[i-1])

    print(f"\nYour gift's composition: {new_year_gift}")

# 3. netto, sum ...

    print(f"Total price: {round(ShopAssistance.calculate_total_price(new_year_gift), 2)} BYN")
    print(
        f"Total weight: {ShopAssistance.calculate_total_weight(new_year_gift)} gr.")
    print(f"Maximum calories in {ShopAssistance.max_cal(new_year_gift)}")
    print(f"Maximum price is for the {ShopAssistance.max_price(new_year_gift)}")

# 4. sort by name

    new_year_gift.sort_by_name()
    print(f"\nSorted by name: {new_year_gift}")

if __name__ == "__main__":
    main()