class GardenError(Exception):
    """
    Base class inherits from the base Exception class for all exceptions
    related to the garden.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for issues specifically affecting plant health."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for water issues, supply, level, etc."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def check_plant_health():
    """Simulates a health check that fails for a tomato plant.

    Raises:
        PlantError: Always raised to demonstrate plant-specific error handling.
    """
    raise PlantError("The tomato plant is wilting!")


def check_water_level():
    """Simulates a sensor check that detects low water levels.

    Raises:
        WaterError: Always raised to demonstrate water-specific error handling.
    """
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")
