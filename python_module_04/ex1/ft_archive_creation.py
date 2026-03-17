
def ft_archive_creation() -> None:

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")

    file = open("new_discovery.txt", "w")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.close()

    file = open("new_discovery.txt")
    content: str = file.read()
    print(content)

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        ft_archive_creation()
    except Exception as e:
        print("ERROR: ", e)
