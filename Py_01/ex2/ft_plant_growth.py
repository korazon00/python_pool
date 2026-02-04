
class Plant:
    def __init__(self, name: str, height: int, age_of_p: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age_of_p: int = age_of_p

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_of_p} days old")

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_of_p += 1


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 30, 40)
plants = [plant1, plant2]


def ft_plant_grow() -> None:
    total_growth: int = 0
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    for i in range(6):
        for p in plants:
            p.grow()
            total_growth += 1
            p.age()
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
    print(f"Growth this week: +{total_growth}cm")


if __name__ == "__main__":
    ft_plant_grow()
