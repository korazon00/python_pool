
import sys

def ft_stream_management():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    arch_id: str = input("Input Stream active. Enter archivist ID: ")
    status_rep: str = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status_rep}l\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    print("[STANDARD] Data transmission complete")

    print("\nThree-channel communication test successful")


if __name__== "__main__":
    try:
        ft_stream_management()
    except Exception as e:
        print("ERROR: ", e)