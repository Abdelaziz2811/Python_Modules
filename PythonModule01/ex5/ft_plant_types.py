class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)}"
              " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(f"\n{rose.name} (Flower): {rose.height}cm, {rose.age} days,"
          f" {rose.color} color")
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days,"
          f" {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days,"
          f" {tomato.harvest_season} harvest")
    tomato.nutritional()
