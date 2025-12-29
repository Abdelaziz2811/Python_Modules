def check_temperature(temp_str):
    """
    Checks if a temperature value is within the safe range for garden plants.

    Returns:
        int | None: Returns the temperature as an integer if it is within
            the safe range (0-40). Returns None if the input is invalid
            or out of range.

    Raises:
        Exception: Catches and handles all conversion or processing errors
            internally to prevent program crashes.
    """
    try:
        print(f"\nTesting temperature: {temp_str}")
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
