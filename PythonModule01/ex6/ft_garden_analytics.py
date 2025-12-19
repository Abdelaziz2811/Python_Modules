class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.points}"


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            old_height = plant.height
            plant.grow()
            print(f"{plant.name} grew {plant.height - old_height}cm")

    def garden_report(self) -> None:
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")

    @classmethod
    def create_garden_network() -> None:
        pass

    class GardenStats:
        pass


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    oak = Plant("Oak Tree", 100, 280)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 40, "yellow", 10)
    alice = GardenManager("Alice")
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    alice.grow_all()
    print("\n=== Alice's Garden Report ===")
    alice.garden_report()
