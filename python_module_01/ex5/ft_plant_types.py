
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

        def get_info() -> None:
            print(f"{name}: {height}cm, {age}days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        print(f"{self.name} provides ", end="")
        print(f"{self.trunk_diameter * 1.56:.0f}", end="")
        print(" square meters of shade")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


Rose: Flower = Flower("Rose", 25, 30, "red")
Sunflower: Flower = Flower("Sunflower", 20, 40, "yellow")

Oak: Tree = Tree("Oak", 500, 1825, 50)
Sakura: Tree = Tree("Sakura", 600, 200, 40)

Tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
Potato: Vegetable = Vegetable("potato", 80, 90, "summer", "Potassium")

flowers_list: list[Flower] = [Rose, Sunflower]
trees_list: list[Tree] = [Oak, Sakura]
vegetables_list: list[Vegetable] = [Tomato, Potato]


def ft_plant_types():
    print("=== Garden Plant Types ===")
    for flower in flowers_list:
        print(f"\n{flower.name} (Flower): {flower.height}cm, ", end=" ")
        print(f"{flower.age} days, {flower.color} color")
        flower.get_info()
    for tree in trees_list:
        print(f"\n{tree.name} (Tree): {tree.height}cm, ", end="")
        print(f"{tree.age} days, {tree.trunk_diameter}cm diametrek")
        tree.get_info()
    for vegetable in vegetables_list:
        print(f"\n{vegetable.name} (Vegetable): {vegetable.height}cm,", end="")
        print(f" {vegetable.age} days, {vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is rish in {vegetable.nutritional_value}")


if __name__ == "__main__":
    ft_plant_types()
