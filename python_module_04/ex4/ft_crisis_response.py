
def ft_crisis_response(file: str) -> None:

    try:
        with open(file) as f:
            print(f"\nROUTINE ACCESS: Attempting access to '{file}'...")
            data = f.read()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:

    files = ['lost_archive.txt', 'classified_vault.txt',
             'standard_archive.txt']

    for file in files:
        ft_crisis_response(file)


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    try:
        main()
    except Exception as e:
        print("ERROR: ", e)
    finally:
        print("\nAll crisis scenarios handled successfully. Archives secure.")
