
class Plant:
    def __init__(self, name, height, age):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def factory_patern(data: list[tuple[str, int, int]]) -> list[Plant]:
    return [Plant(name, height, age) for name, height, age in data]


data: list[tuple[str, int, int]] = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants = factory_patern(data)
    i: int = 0
    for p in plants:
        p.get_info()
        i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
