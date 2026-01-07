def open_file(file_name: str) -> None:
    """
    Attempt to open and read a file with comprehensive error handling.
    """
    try:
        with open(file_name, "r") as file:
            print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    open_file("lost_archive.txt")
    open_file("classified_vault.txt")
    open_file("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
