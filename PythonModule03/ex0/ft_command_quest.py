import sys


def command_quest() -> None:
    """Prints command line arguments"""
    print("=== Command Quest ===")

    total_args = len(sys.argv)
    if total_args < 2:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")
    if total_args > 1:
        print(f"Arguments received: {total_args - 1}")

        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest()
