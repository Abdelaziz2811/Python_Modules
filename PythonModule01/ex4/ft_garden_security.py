class SecurePlant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if (height < 0):
            print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
                "\nSecurity: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def get_height(self):
        return self.__height

    def set_age(self, age):
        if (age < 0):
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]"
                  "\nSecurity: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm,"
          f" {rose.get_age()} days)")
