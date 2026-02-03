
def garden_operations():
    """ Demonstrates errors"""
    try:
        print(f"{'abc':d}")
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")

    try:
        x = 100000000 / 0
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        file: int = open("missing.txt")
        file.close()
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        garden: dict = {
            "flower": 5
        }
        print(garden["plant"])
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'plant'\n")

    try:
        print(f"{'abc':d}")
        x: int = 100000000 / 0
        print(x)
        file: int = open("missing.txt")
        plants: dict = {
            "flower": 5
        }
        print(plants["tomato"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")


def test_error_types():
    """ test the errors """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!\n")
