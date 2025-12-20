class Plant:
    """Represents the base class for all plant types."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes common plant traits."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a specialized plant (Flower)."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes a special plant characteristics (color)."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Simulates the flower blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a specialized plant (Tree)."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initializes a special plant characteristics (trunk diameter)."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Displays shade coverage"""
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)}"
              " square meters of shade")


class Vegetable(Plant):
    """Represents a specialized plant (Vegetable)."""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initializes a special plant characteristics
        (harvest season, nutritional value).
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        """Displays nutritional value"""
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
