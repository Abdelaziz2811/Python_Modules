class Plant:
    """
    Represents a plant in the garden with basic attributes.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant.
        """
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """
        Prints plant info
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.display_info()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.display_info()
    cactus = Plant("Cactus", 15, 120)
    cactus.display_info()
