def water_plants(plant_list):
    """
    Simulates a garden irrigation process with mandatory resource cleanup.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise Exception("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Demonstrates the behavior of the watering system

    Two scenarios are tested:
    1. A successful run where all plants are valid.
    2. A failure scenario where an invalid plant (None) triggers an exception.
    """
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
