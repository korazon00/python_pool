
import sys

print("=== Command Quest ===")

arguments: int = len(sys.argv)

if arguments < 2:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {arguments - 1}")

    x = 1
    while x < arguments:
        print(f"Argument {x}: {sys.argv[x]}")
        x += 1

print(f"total arguments: {arguments}\n")
