
def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def ft_helper_function(days):
        if days > 0:
            ft_helper_function(days - 1)
            print(f"Day: {days}")

    ft_helper_function(days)
    print("Harvest time!")
