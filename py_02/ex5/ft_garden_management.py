
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name: str = name
        self.water: int = water
        self.sun: int = sun


class GardenManager:
    def __init__(self):
        self.Plants: list[Plant] = []
        self.tank: int = 20

    def add_plants(self, plant: Plant):
        try:
            if not plant.name or plant.name.__class__.__name__ != "str":
                raise PlantError("Plant name cannot be empty!\n")
            self.Plants += [plant]
            print(f"Adding {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.Plants:
                if not plant:
                    raise WaterError("Plant is missing!")
                print(f"Watering {plant.name} - success")
                self.tank -= plant.water
        except WaterError as e:
            print(f"Error watering: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plants_health(self, name: str, water: int, sun: int):
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")

        if sun < 2:
            raise WaterError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise WaterError(
                f"Sunlight hours {sun} is too hight (max 12)"
                )
        print(f"{name}: healty (water: {water}, sun: {sun})")


def test_garden_management():
    print("=== Garden Management System ===\n")

    Manager: GardenManager = GardenManager()
    p1: Plant = Plant("tomato", 5, 8)
    p2: Plant = Plant("lettuce", 15, 10)
    p3: Plant = Plant("", 3, 7)
    plants: list[Plant] = [p1, p2, p3]

    print("Adding plants to garden...")
    for p in plants:
        Manager.add_plants(p)

    print("Watering plants...")
    Manager.water_plants()

    print("Checking plant health...")
    try:
        for p in plants:
            Manager.check_plants_health(p.name, p.water, p.sun)
    except WaterError as e:
        print(f"Error checking {p.name}: {e}")

    try:
        print("\nTesting error recovery...")
        if Manager.tank < 5:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    else:
        print("Garden status: Enough water in tank")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
