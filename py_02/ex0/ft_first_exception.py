

def check_temperature(temp_str: str) -> int:
    try:
        num: int = int(temp_str)
        if (0 <= num <= 40):
            return num
        elif num < 0:
            return -1
        elif num > 40:
            return -2
    except Exception:
        return -3


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    tests: list = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"Testing temperature: {test}")
        check: int = check_temperature(test)

        if check >= 0:
            print(f"Temperature {test}°C is perfect for plants!\n")

        elif check == -3:
            print(f"Error: '{test}' is not a valid number\n")

        elif check == -2:
            print(f"Error: {test}°C is too hot for plants (max 40°C)\n")

        elif check == -1:
            print(f"Error: {test}°C is too cold for plants (min 0°C)\n")

    print("All tests completed - program didn't crash!")
