
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught WaterError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!\n")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")
