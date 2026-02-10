
def water_plants(plant_list):

    if not plant_list:
        raise ValueError ("Cannot water None - invalid plant!")
    for plant in plant_list:
        if not plant:
            raise ValueError ("Cannot water None - invalid plant!")
        print(f"Watring {plant}")


def test_watring_system():
    success: bool = False
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        good_plans = ["", "lettuce", "carrots"]
        water_plants(good_plans)

    except ValueError as e:
        print(f"Error: {e}")
    else:
        success = True
    finally:
        print("Closing watering system (cleanup)")
    if success is True:
        print("Watering completed successfully!\n")

    try:
        print("Testing with error...")
        bad_plants = ["tomato", None, "carrots"]
        water_plants(bad_plants)

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")
    print("Cleanup always happens, even with errors!")

test_watring_system()
