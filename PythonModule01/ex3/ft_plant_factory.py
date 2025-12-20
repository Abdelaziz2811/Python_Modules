class Plant:
    """
    Represents a factory-style plant that tracks total creations.
    """
    count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant and prints its creation with its info.
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)

    print(f"\nTotal plants created: {Plant.count}")
