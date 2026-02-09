
import sys

def sort_dict(dict: dict) -> dict:

    cur_dict = {}
    tmp_dict = {}
    for item in dict.items():
        tmp_dict.update({item})

    x = 0
    while x < len(tmp_dict):
        tmp_v = 0
        tmp_k = 0
        v = 0
        for k, v in tmp_dict.items():
            if v > tmp_v:
                tmp_v = v
                tmp_k = k

        cur_dict.update({tmp_k: tmp_v})
        tmp_dict[tmp_k] = 0
        x += 1
    return cur_dict

def the_most_abundant(dict: dict) -> None:
    tmp_v = 0
    for k, v in dict.items():
        if v > tmp_v:
            tmp_v = v
            tmp_k = k
    print(f"Most abundant: {tmp_k} ({tmp_v}", end=" ")
    if tmp_v > 1:
        print("units)")
    else:
        print("unit)")
#     print(f"Most abundant: {k} ({v}", end=" ")

# def Least_abundant(dict: dict) -> None:
#     pass

if __name__ == "__main__":

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
        print(f"{x}: {inventry[x]}",end=" ")
        if inventry[x] > 1:
            print("units",end=" ")
        else:
            print("unit", end=" ")
        print(f"({(inventry[x] * 100 / i):.1f}%)")

    print("=== Inventory Statistics ===")
    # # x = 0
    # # for item in inventry:
    # #     print(f"\nMost abundant: {item} ({inventry[item]}", end=" ")
    # #     if inventry[item] > 1:
    # #         print("units)",end=" ")
    # #     else:
    # #         print("unit)", end=" ")
    # #     if x < len(inventry.items()):
    # #         continue
    # #     x += 1
    the_most_abundant(inventry)
    # if inventry[item] > 1:
    #     print("units)",end=" ")
    # else:
    #     print("unit)", end=" ")