class GardenError(Exception):
    """Base exception class for all garden management issues."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for errors specifically related to a plant"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised specifically related to water issues"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    """Represents a plant entity with specific environmental needs."""
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Manages the hydration, and health of garden plants."""
    def __init__(self) -> None:
        self.plants = []
        self.tank_level = 25

    def add_plant(self, name: str, water_level: int,
                  sunlight_hours: int) -> None:
        """
        Validates and adds a new plant to the garden collection.

        Raises:
            PlantError: If the plant name provided is an empty string.
        """
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")

            self.plants.append(Plant(name, water_level, sunlight_hours))
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """
        Simulates the irrigation process for all plants.

        Uses a finally block to ensure the watering system is closed.
        """
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise PlantError("Cannot water None - invalid plant!")
                plant.water_level += 5
                self.tank_level -= 5
                print(f"Watering {plant.name} - success")
        except PlantError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """
        Evaluates each plant's hydration.

        Raises:
            WaterError: Caught per plant if water level is < 1 or > 10.
        """
        for plant in self.plants:
            try:
                if plant.water_level < 1:
                    raise WaterError(
                        f"Water level {plant.water_level} is too low (min 1)"
                        )
                if plant.water_level > 10:
                    raise WaterError(
                        f"Water level {plant.water_level} is too high (max 10)"
                        )

                print(f"{plant.name}: healthy (water: {plant.water_level},"
                      f" sun: {plant.sunlight_hours})")
            except WaterError as e:
                print(f"Error checking {plant.name}: {e}")

    def check_tank_status(self) -> None:
        """
        Verifies if the water tank volume is enough.

        Raises:
            GardenError: Caught if tank_level falls below 20.
        """
        try:
            if self.tank_level < 20:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    manager = GardenManager()
    manager.add_plant("tomato", 0, 8)
    manager.add_plant("lettuce", 10, 8)
    manager.add_plant("", 0, 8)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.check_tank_status()

    print("\nGarden management system test complete!")
