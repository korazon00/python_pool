
class Plant:
    def __init__(self, name, heigth):
        self.name = name
        self.heigth = name

    def grow(self):
        self.heigth += 1
        print(f"{self.name} grew 1cm")

class FloweringPlant (Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

class PrizeFlower (FloweringPlant):
    def __init__ (self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

class garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = [None, None, None, None, None]
        self.count = 0

        def add_plant (self, plant):
            self.plant[self.count] = plant
            self.count += 1
            print(f"added, {plant.name} to {self.owner}'s garden")

        def grow_all(self):
            for i in range(self.count):
                self.plant[i].grow()


class GardenManager:
    gardens = [None, None]
    garden_count = 0        

    class GardenStats:
        @staticmethod
        def count_plants(garden):
            return garden_count

    def add_garden(self, garden):
            GardenManager.gardens[GardenManager.garden_count] = garden
            GardenManager.garden_count += 1

    @classmethod
    def creat_garden_network(cls):
        print("Garden scores: ")
        if i in range(cls.garden_count):
            garden = cls.gardens[i]
            score = 0
            for j in range(garden.count):
                score += garden.plant[j].height
            print(f"{garden.owner} : {score}")

    @classmethod
    def total_gardens(cls):
        return cls.garden_count

def main():
    manager = GardenManager()

    alice = garden("Alice")
    Deku = garden("Deku")

    manager.add_garden(alice)
    manager.add_garden(Deku)

    alice.add_plant(plant("Oak", 100))
    alice.add_plant(plant("Rose", 25, "red"))
    alice.add_plant(plant("Sunflower", 50, "yellow", 10))

    alice.grow_all()

    GardenManager.creat_garden_network()
    print(f"Total gardens: {GardenManager.total_gardens()}")

if __name__ == "__main__":
    main()
