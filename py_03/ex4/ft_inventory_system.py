
import sys


def sort_dict(dic: dict) -> dict:

    cur_dict: dict = {}
    tmp_dict: dict = {}
    for item in dic.items():
        tmp_dict.update({item})

    x: int = 0
    while x < len(tmp_dict):
        tmp_v: int = 0
        tmp_k: int = 0
        v: int = 0
        for k, v in tmp_dict.items():
            if v > tmp_v:
                tmp_v = v
                tmp_k = k

        cur_dict.update({tmp_k: tmp_v})
        tmp_dict[tmp_k] = 0
        x += 1
    return cur_dict


def inventory_statistics(dic: dict) -> None:
    i: int = 0
    k: str = None
    v: int = None
    for k, v in dic.items():
        if i == 0:
            print(f"Most abundant: {k} ({v}", end=" ")
            if v > 1:
                print("units)")
            else:
                print("unit)")
        i += 1
    print(f"Least abundant: {k} ({v}", end=" ")
    if v > 1:
        print("units)")
    else:
        print("unit)")


def item_categories(dic: dict) -> dict:

    scarce_dict: dict = {}
    moderate_dict: dict = {}
    item_dict: dict = {}
    k: str = None
    v: int = None
    for k, v in dic.items():
        if v < 4:
            scarce_dict[k] = v
        elif v >= 4:
            moderate_dict[k] = v
    item_dict.update({"moderate": moderate_dict, "scarce": scarce_dict})
    return item_dict


def restock(dic: dict) -> None:

    items_list: list = []
    for k, v in dic.items():
        if v <= 1:
            items_list += [k]
    print(f"Restock needed: {items_list}")


def get_the_keys(dic: dict) -> None:
    keys_list: list = []
    for key in dic.keys():
        keys_list += [key]
    print(f"Dictionary keys: {keys_list}")


def get_the_values(dic: dict) -> None:
    values_list: list = []
    for value in dic.values():
        values_list += [value]
    print(f"Dictionary values: {values_list}")


def lookup(dict: dict, word: str) -> None:
    for key in dict.keys():
        if key == word:
            print(f"'{word}' in inventory: True")
            return
    print(f"No '{word}' in inventory: False")


def main():
    print("=== Inventory System Analysis ===")

    arguments: list = sys.argv

    inventry: dict = {}

    i: int = 1
    while i < len(arguments):
        x: list = arguments[i].split(":")
        inventry[x[0]] = int(x[1])
        i += 1

    i = 0
    for key in inventry.keys():
        i += inventry.get(key)
    print(f"Total items in inventory: {i}")
    print(f"Unique item types: {len(inventry.items())}")

    print("\n=== Current Inventory ===")

    inventry = sort_dict(inventry)
    for x in inventry:
        print(f"{x}: {inventry[x]}", end=" ")
        if inventry[x] > 1:
            print("units", end=" ")
        else:
            print("unit", end=" ")
        print(f"({(inventry[x] * 100 / i):.1f}%)")

    print("\n=== Inventory Statistics ===")

    inventory_statistics(inventry)

    print("\n=== Item Categories ===")

    items = item_categories(inventry)
    print(f"Moderate: {items["moderate"]}")
    print(f"Scarce: {items["scarce"]}")

    print("\n=== Management Suggestions ===")

    restock(inventry)

    print("\n=== Dictionary Properties Demo ===")
    get_the_keys(inventry)
    get_the_values(inventry)

    print("Sample lookup", end=" - ")
    lookup(inventry, "sword")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
