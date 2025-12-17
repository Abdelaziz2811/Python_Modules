def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))

    def recusive_helper(current_day):
        if current_day > days_until_harvest:
            return
        print(f"Day {current_day}")
        recusive_helper(current_day + 1)
    recusive_helper(1)
    print("Harvest time!")
