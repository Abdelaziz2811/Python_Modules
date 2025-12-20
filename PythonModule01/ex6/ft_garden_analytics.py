class Plant:
    """Base plant class representing a generic plant."""
    plant_type = "regular"

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with name and height."""
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        """Grow the plant by specified amount in cm."""
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> str:
        """Return plant information as string."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A flowering plant, inherits from Plant."""
    plant_type = "flowering"

    def __init__(self, name: str, height: int,
                 color: str, is_blooming: bool) -> None:
        """Initialize a flowering plant with color and blooming status."""
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def get_info(self) -> str:
        """Return flowering plant info."""
        blooming = "blooming" if self.is_blooming else "not blooming"
        return f"{super().get_info()}, {self.color} flowers ({blooming})"


class PrizeFlower(FloweringPlant):
    """A prize flowering plant, inherits from FloweringPlant."""
    plant_type = "prize"

    def __init__(self, name: str, height: int, color: str, is_blooming: bool,
                 prize_points: int) -> None:
        """Initialize a prize flower with prize points."""
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """Return prize flower info."""
        return f"{super().get_info()}, Prize points: {self.prize_points}"


class Garden:
    """A garden containing plants with statistics tracking."""
    def __init__(self, owner: str, garden_stats) -> None:
        """Initialize a garden with owner and stats tracker."""
        self.owner = owner
        self.plants = []
        self.garden_stats = garden_stats
        self.score = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and update statistics."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.garden_stats.plants_added += 1
        self.garden_stats.count_plant_types(plant.plant_type)

    def grow_all(self, amount: int) -> None:
        """Grow all plants in the garden by specified amount."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.garden_stats.total_growth += amount

    def count_garden_score(self) -> None:
        """Calculate total score for all plants in garden."""
        self.score = 0
        for plant in self.plants:
            self.score += self.garden_stats.get_plant_points(plant)


class GardenManager:
    """Manages multiple gardens with analytics."""
    garden_count = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics."""
        def __init__(self) -> None:
            """Initialize all statistics counters to zero."""
            self.plants_added = 0
            self.total_growth = 0
            self.flowering = 0
            self.prize = 0
            self.regular = 0

        def count_plant_types(self, plant_type: str) -> None:
            """Increment counter for the given plant type."""
            if plant_type == "flowering":
                self.flowering += 1
            elif plant_type == "prize":
                self.prize += 1
            elif plant_type == "regular":
                self.regular += 1

        def get_plant_types_count(self) -> tuple[int, int, int]:
            """Return counts of regular, flowering, and prize plants."""
            return (self.regular, self.flowering,
                    self.prize)

        def get_plant_points(self, plant: Plant) -> int:
            """Calculate score points for a single plant."""
            score = plant.height
            if plant.plant_type == "flowering":
                score += 10
            if plant.plant_type == "prize":
                score += plant.prize_points
                score += 20
            return score

        def get_garden_stats(self) -> str:
            """Return string of garden statistics."""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm")

    def __init__(self) -> None:
        """Initialize garden manager with empty gardens dictionary."""
        self.gardens = {}

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager and increment count."""
        self.gardens[garden.owner] = garden
        GardenManager.garden_count += 1

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        """Create a network of gardens for given owners."""
        manager = cls()
        for owner in owners:
            manager.add_garden(Garden(owner, manager.GardenStats()))
        return manager

    @staticmethod
    def generate_report(garden: Garden) -> None:
        """Generate and print a report for a specific garden."""
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.get_info()}")

    @staticmethod
    def display_garden_stats(garden: Garden) -> None:
        """Display statistics for a specific garden."""
        print(garden.garden_stats.get_garden_stats())
        reg, flow, prize = garden.garden_stats.get_plant_types_count()
        print(f"Plant types: {reg} regular, "
              f"{flow} flowering, {prize} prize flowers")

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate the height of a plant."""
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice_garden = manager.gardens["Alice"]
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red", True))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", True, 10))

    bob_garden = manager.gardens["Bob"]
    bob_garden.plants.append(Plant("Pine", 92))

    print()
    alice_garden.grow_all(1)

    print()
    manager.generate_report(alice_garden)

    print()
    manager.display_garden_stats(alice_garden)

    print()
    print("Height validation test: "
          f"{GardenManager.validate_height(alice_garden.plants[0].height)}")
    alice_garden.count_garden_score()
    bob_garden.count_garden_score()
    print(f"Garden scores - Alice: {alice_garden.score}, "
          f"Bob: {bob_garden.score}")
    print(f"Total gardens managed: {GardenManager.garden_count}")
