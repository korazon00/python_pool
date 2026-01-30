

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant (Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")

class PrizeFlower (FloweringPlant):
    def __init__ (self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
        self.type = "prize flowers"

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.points}")

class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.count = 0
        self.total_grow = 0

    def add_plant(self, plant, flag):
        self.plants += [plant]
        self.count += 1
        if flag == 1:
            print(f"added, {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for i in range(self.count):
            self.plants[i].grow()
            self.total_grow += 1

    def get_info(self):
        for i in range(self.count):
            self.plants[i].get_info()

class GardenManager:
    gardens = []
    garden_count = 0

    class GardenStats:
        @staticmethod
        def print_stats(garden):
            r = 0
            f = 0
            p = 0

            for plant in garden.plants:
                if plant.type == "regular":
                    r += 1
                elif plant.type == "flowering":
                    f += 1
                elif plant.type == "prize flowers":
                    p += 1

            print(f"\nPlant added: {garden.count}, Total growth: {garden.total_grow}cm")
            print(f"Plant type: {r} regular, {f} flowering, {p} prize flowering")



    def add_garden(self, garden):
            GardenManager.gardens += [garden]
            GardenManager.garden_count += 1

    
    @classmethod
    def creat_garden_network(cls):
        # r = 0
        # f = 0
        # p = 0
        print(f"\n=== {cls.gardens[0].owner}'s Garden Report ===")
        print("Plants in garden:")
        garden = cls.gardens[0]
        for j in range(garden.count):
            garden.plants[j].get_info()
        #     if garden.plants[j].type == "regular":
        #         r += 1
        #     elif garden.plants[j].type == "flowering":
        #         f += 1
        #     elif garden.plants[j].type == "prize flowers":
        #         p += 1
        # print(f"\nPlant added: {garden.count}, Total growth: {garden.total_grow}cm")
        # print(f"Plant type: {r} regular, {f} flowering, {p} prize flowering")
        
        cls.GardenStats.print_stats(garden)

        print(f"\nHeight validation test: {GardenManager.height_validation()}")
        print("Garden scores - ", end="")
        for i in range(cls.garden_count):
            garden = cls.gardens[i]
            score = 0
            for j in range(garden.count):
                score += garden.plants[j].height
            print(f"{garden.owner}: {score}", end="")
            if i < cls.garden_count - 1:
                print(", ", end="")


    @classmethod
    def height_validation(cls) -> bool:
        for garden in cls.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    return False
        return True


    @classmethod
    def total_gardens(cls):
        return cls.garden_count

if __name__ == "__main__":
    print ("=== Garden Management System Demo ===\n")
    manager = GardenManager()

    alice = Garden("Alice")
    bob = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)


    alice.add_plant(Plant("Oak Tree", 100), 1)
    alice.add_plant(FloweringPlant("Rose", 25, "red"),1)
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10),1)
    bob.add_plant(Plant("sakura", 92),0)

    print("")
    alice.grow_all()

    GardenManager.creat_garden_network()
    print(f"\nTotal gardens: {GardenManager.total_gardens()}")

