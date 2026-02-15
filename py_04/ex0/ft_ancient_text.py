
def ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")

    try:
        with open("ancient_fragment.txt") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found")

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        ancient_text()
    except Exception as e:
        print("ERROR: ", e)
