def main() -> None:
    """Open and read content from 'ancient_fragment.txt'."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    try:
        file_name = "ancient_fragment.txt"
        file = open(file_name)
        print(f"\nAccessing Storage Vault: {file_name}")
        print("Connection established...")

        print("\nRECOVERED DATA:")
        print(file.read())

        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    main()
