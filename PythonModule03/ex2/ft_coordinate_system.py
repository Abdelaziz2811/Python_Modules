import math


def coordinate_system():
    """Demonstrate tuple operations for coordinate handling."""
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    x1, y1, z1 = position
    print(f"\nPosition created: {position}")

    default_position = (0, 0, 0)
    x2, y2, z2 = default_position

    print(f"Distance between {default_position} and {position}: "
          f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.2f}")

    input_str = "3,4,0"
    print(f"\nParsing coordinates: \"{input_str}\"")
    coordinates = input_str.split(',')

    position = tuple((int(num) for num in coordinates))
    print(f"Parsed position: {position}")
    x1, y1, z1 = position

    print(f"Distance between {default_position} and {position}: "
          f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.1f}")

    input_str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{input_str}\"")
    coordinates = input_str.split(',')

    try:
        position = tuple((int(num) for num in coordinates))
        print(f"Parsed position: {position}")
        x1, y1, z1 = position
        print(f"Distance between {default_position} and {position}: "
              f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


if __name__ == "__main__":
    coordinate_system()
