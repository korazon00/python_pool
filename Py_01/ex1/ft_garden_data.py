
class Plant:
    def __init__(self, name, height, age):
        self.name: str= name
        self.height: int = height
        self.age: int = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

plants = [plant1, plant2, plant3]


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    for p in plants:
        p.get_info()


if __name__ == "__main__":
    ft_garden_data()
