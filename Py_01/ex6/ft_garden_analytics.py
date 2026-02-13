
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.type: str = "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant (Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.type: str = "flowering"

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm,", end=" ")
        print(f"{self.color} flowers (blooming)")


class PrizeFlower (FloweringPlant):
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points
        self.type: str = "prize flowers"

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color},", end=" ")
        print(f"flowers (blooming), Prize points: {self.points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.count: int = 0
        self.total_grow: int = 0

    def add_plant(self, plant: Plant, flag: int) -> None:
        self.plants += [plant]
        self.count += 1
        if flag == 1:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for i in range(self.count):
            self.plants[i].grow()
            self.total_grow += 1

    def get_info(self) -> None:
        for i in range(self.count):
            self.plants[i].get_info()


class GardenManager:
    gardens: list[Garden] = []
    garden_count: int = 0

    def heading() -> None:
        print("=== Garden Management System Demo ===\n")

    heading = staticmethod(heading)

    class GardenStats:
        def print_stats(cls, garden: Garden) -> None:
            r: int = 0
            f: int = 0
            p: int = 0

            for plant in garden.plants:
                if plant.type == "regular":
                    r += 1
                elif plant.type == "flowering":
                    f += 1
                elif plant.type == "prize flowers":
                    p += 1

            print(f"\nPlant added: {garden.count}, Total growth:", end=" ")
            print(f"{garden.total_grow}cm")
            print(f"Plant type: {r} regular, {f} flowering,", end=" ")
            print(f"{p} prize flowers")

        print_stats = classmethod(print_stats)

    def add_garden(self, garden: Garden) -> None:
        GardenManager.gardens += [garden]
        GardenManager.garden_count += 1

    def creat_garden_network(cls) -> None:
        for garden in cls.gardens:
            print(f"\n=== {garden.owner}'s Garden Report ===")
            print("Plants in garden:")
            for j in range(garden.count):
                garden.plants[j].get_info()
            break

        cls.GardenStats.print_stats(garden)

        print(f"\nHeight validation test: {GardenManager.height_validation()}")
        print("Garden scores - ", end="")
        for i in range(cls.garden_count):
            garden: Garden = cls.gardens[i]
            score: int = 0
            for j in range(garden.count):
                score += garden.plants[j].height
            print(f"{garden.owner}: {score}", end="")
            if i < cls.garden_count - 1:
                print(", ", end="")

    creat_garden_network = classmethod(creat_garden_network)

    def height_validation(cls) -> bool:
        for garden in cls.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    return False
        return True

    height_validation = classmethod(height_validation)

    def total_gardens(cls) -> None:
        return cls.garden_count

    total_gardens = classmethod(total_gardens)


if __name__ == "__main__":
    manager: GardenManager = GardenManager()

    manager.heading()

    alice: Garden = Garden("Alice")
    bob: Garden = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)

    alice.add_plant(Plant("Oak Tree", 100), 1)
    alice.add_plant(FloweringPlant("Rose", 25, "red"), 1)
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10), 1)
    bob.add_plant(Plant("sakura", 92), 0)

    print("")
    alice.grow_all()

    GardenManager.creat_garden_network()
    print(f"\nTotal gardens: {GardenManager.total_gardens()}")
