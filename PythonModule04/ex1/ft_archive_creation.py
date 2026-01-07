def main() -> None:
    """Create 'new_discovery.txt' and write three data entries."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    try:
        file_name = "new_discovery.txt"
        print(f"\nInitializing new storage unit: {file_name}")
        new_discovery = open(file_name, "w")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        entry1 = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
        new_discovery.write(entry1)
        print(entry1, end="")

        entry2 = "{[}ENTRY 002{]} Efficiency increased by 347%\n"
        new_discovery.write(entry2)
        print(entry2, end="")

        entry3 = "{[}ENTRY 003{]} Archived by Data Archivist abdelaziz\n"
        new_discovery.write(entry3)
        print(entry3, end="")

        new_discovery.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
