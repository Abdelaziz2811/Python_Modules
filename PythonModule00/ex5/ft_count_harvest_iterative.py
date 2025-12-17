def ft_count_harvest_iterative():
    days_until_harvest = int(input("Days until harvest: "))
    days = range(1, days_until_harvest + 1)
    for day in days:
        print(f"Day {day}")
    print("Harvest time!")
