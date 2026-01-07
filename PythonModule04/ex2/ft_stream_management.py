import sys


def main() -> None:
    """Read user input and display messages to stdout and stderr."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    arch_id = input("\nInput Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print("\n{[}STANDARD{]} Archive status from "
          f"{arch_id}: {status_report}")

    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("{[}STANDARD{]} Data transmission complete")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
