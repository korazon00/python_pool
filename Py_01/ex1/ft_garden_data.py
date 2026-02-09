
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1: Plant = Plant("Rose", 25, 30)
plant2: Plant = Plant("Sunflower", 80, 45)
plant3: Plant = Plant("Cactus", 15, 120)

plants: list[Plant] = [plant1, plant2, plant3]


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    for p in plants:
        p.get_info()


if __name__ == "__main__":
    ft_garden_data()
