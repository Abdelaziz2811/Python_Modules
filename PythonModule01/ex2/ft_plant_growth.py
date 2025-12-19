class Plant:
    def __init__(self, name, height, days) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.days} days old"


rose = Plant("Rose", 25, 30)
old_height = rose.height
day = 1

print(f"=== Day {day} ===")
print(rose.get_info())

while day < 7:
    rose.grow()
    rose.age()
    day += 1

print(f"=== Day {day} ===")
print(rose.get_info())

print(f"Growth this week: +{rose.height - old_height}cm")
