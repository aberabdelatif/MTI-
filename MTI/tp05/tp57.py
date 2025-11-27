
class Sandwich:
    def __init__(self):
        self.parts = []

    def add(self, ingredient):
        self.parts.append(ingredient)

    def show(self):
        print("Sandwich:", self.parts)



class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        pass

    def add_meat(self):
        pass

    def add_sauce(self):
        pass

    def add_extras(self):
        pass



class ShawarmaBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add("Arab Bread")

    def add_meat(self):
        self.sandwich.add("Shawarma Chicken")

    def add_sauce(self):
        self.sandwich.add("Garlic Sauce")

    def add_extras(self):
        self.sandwich.add("Pickles")


class GroundMeatBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add("Baguette")

    def add_meat(self):
        self.sandwich.add("Ground Meat")

    def add_sauce(self):
        self.sandwich.add("Harissa")

    def add_extras(self):
        self.sandwich.add("Salad")


class OmeletteFriesBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add("French Bread")

    def add_meat(self):
        self.sandwich.add("Omelette")

    def add_sauce(self):
        self.sandwich.add("Mayonnaise")

    def add_extras(self):
        self.sandwich.add("Fries")


# -------------------------
#         DIRECTOR
# -------------------------
class SandwichDirector:
    def construct(self, builder: SandwichBuilder):
        builder.add_bread()
        builder.add_meat()
        builder.add_sauce()
        builder.add_extras()



def main():
    director = SandwichDirector()

    # Shawarma
    shawarma = ShawarmaBuilder()
    director.construct(shawarma)
    shawarma.sandwich.show()

    # Ground meat
    meat = GroundMeatBuilder()
    director.construct(meat)
    meat.sandwich.show()

    # Omelette + Fries
    omelette = OmeletteFriesBuilder()
    director.construct(omelette)
    omelette.sandwich.show()


if __name__ == "__main__":
    main()
