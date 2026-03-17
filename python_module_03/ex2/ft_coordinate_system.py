
import math


def calc_dist_tup(pos: tuple, tuple0: tuple) -> None:

    try:
        (x1, y1, z1) = tuple0

        if pos.__class__ == tuple:
            (x2, y2, z2) = pos
            dis: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

            print(f"Position created: {pos}")
            print(f"Distance between {tuple0} and {pos}: {dis:.2f}")
    except Exception as e:
        print(f"\nParsing invalid coordinates: \"{pos}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}", end=", ")
        print(f"Args: (\"{e}\",)")


def calc_dist_str(pos: str, tuple0: tuple) -> None:

    (x1, y1, z1) = tuple0

    try:
        if pos.__class__ == str:
            list_of_str: list = pos.split(",")

            list_of_dig: tuple = tuple((int(num)) for num in list_of_str)

            (x2, y2, z2) = list_of_dig

            print(f"\nParsing coordinates: \"{pos}\"")

            dis: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Parsed position: {x2, y2, z2}")
            print(f"Distance between: {tuple0} and {list_of_dig}: {dis:.1f}")

    except Exception as e:
        print(f"\nParsing invalid coordinates: \"{pos}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}", end=", ")
        print(f"Args: (\"{e}\",)")


def unpacking() -> None:
    try:
        player_pos: tuple = (3, 4, 0)
        (x, y, z) = player_pos
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}", end=", ")
        print(f"Args: (\"{e}\",)")


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")

    t: tuple = 0, 0, 0

    l1: list = (10, 20, 5)
    l2: str = "3,4,0"
    l3: str = "abc,def,ghi"

    calc_dist_tup(l1, t)

    calc_dist_str(l2, t)

    calc_dist_str(l3, t)

    unpacking()
