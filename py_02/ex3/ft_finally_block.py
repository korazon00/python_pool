
def water_plants(plant_list):
    success = False
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"watering {plant}")
        success = True
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!\n")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_plant = ["tomato", "lettuce", "carrots"]
    water_plants(good_plant)

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")
