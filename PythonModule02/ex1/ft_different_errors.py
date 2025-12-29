def garden_operations(action_name: str):
    if action_name == "ValueError":
        int("invalid input")
    elif action_name == "ZeroDivisionError":
        5 / 0
    elif action_name == "FileNotFoundError":
        open("missing.txt")
    elif action_name == "KeyError":
        plant = {}
        plant["missing_plant"]


def test_error_types():
    """
    Executes tests to demonstrate exception handling patterns.

    This function showcases two main patterns:
    1. Catching specific exceptions individually to provide unique feedback.
    2. Catching a multiple exceptions in a single block for general recovery.

    Note:
        In the multiple-error test block, only the first error is caught;
        subsequent lines in the 'try' block are skipped.
    """
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    try:
        print("\nTesting KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    try:
        print("\nTesting multiple errors together...")
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
        garden_operations("FileNotFoundError")
        garden_operations("KeyError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
