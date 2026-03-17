
def ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")

    try:
        file = open("ancient_fragment.txt")
        content = file.read()
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
    else:
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        ancient_text()
    except Exception as e:
        print("ERROR: ", e)
