class Plant:
    count = 0

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("")

    rose = Plant("Rose", 25, 30)
    Oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)

    print(f"\nTotal plants created: {Plant.count}")
