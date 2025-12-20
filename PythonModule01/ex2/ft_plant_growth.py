class Plant:
    """
    Represents a plant that can grow and age over time.
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        """
        Initialize the plant.
        """
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        """Increase plant height by 1cm."""
        self.height += 1

    def age(self) -> None:
        """Increase plant age by 1 day."""
        self.days += 1

    def get_info(self) -> str:
        """Returns plant info"""
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def simulate_growth(self, days: int) -> None:
        """
        Simulates plant growth over specific number of days.
        Prints plant status at the start and end day.
        """
        day = 1
        print(f"=== Day {day} ===")
        print(self.get_info())
        while day < days:
            self.grow()
            self.age()
            day += 1
        print(f"=== Day {day} ===")
        print(self.get_info())


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    old_height = rose.height
    rose.simulate_growth(7)
    print(f"Growth this week: +{rose.height - old_height}cm")
