
import sys

def sort_dict(dict: dict) -> dict:

    cur_dict = {}
    tmp_dict = {}
    for item in dict.items():
        tmp_dict.update({item})
    print(tmp_dict)

    x = 0
    while x < len(tmp_dict):
        print(len(tmp_dict))
        tmp_v = 0
        tmp_k = 0
        v = 0
        for k, v in tmp_dict.items():
            if v > tmp_v:
                tmp_v = v
                tmp_k = k

        cur_dict.update({tmp_k: tmp_v})
        tmp_dict.pop(tmp_k)
        x += 1
    print(cur_dict)
    return cur_dict


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
    # for x in inventry:
    #     print(x)
