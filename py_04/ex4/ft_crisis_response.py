
def ft_crisis_response() -> None:

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt") as lost:
            lost.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt") as access_deny:
            access_deny.write()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt") as stand:
            data: str = stand.read()
            print(f"SUCCESS: Archive recovered - ``{data}''")
    except Exception as e:
        print("STATUS: Operations have not resumed normally")
    else:
        print("STATUS: Normal operations resumed")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        ft_crisis_response()
    except Exception as e:
        print("ERROR: ", e)
    finally:
        print("\nAll crisis scenarios handled successfully. Archives secure.")