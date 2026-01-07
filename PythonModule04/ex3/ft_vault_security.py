def main() -> None:
    """
    Read from and write to files using context manager for automatic cleanup.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    try:
        print("\nInitiating secure vault access...")

        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read())

        with open("security_protocols.txt", "w") as file2:
            print("\nSECURE PRESERVATION:")
            new_protocol = "{[}CLASSIFIED{]} New security protocols archived"
            file2.write(new_protocol)
            print(new_protocol)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
