import hashlib
import os
import time


MONITOR_DIR = "./test_folder"
BASELINE_FILE = "baseline.txt"


def calculate_hash(filepath):
    sha256_hash = hashlib.sha256

    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(8192):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    except FileNotFoundError:
        return None
    except PermissionError:
        return None


def create_baseline():
    print("----- CREATING NEW BASELINE -----")

    if os.path.exists(BASELINE_FILE):
        os.remove(BASELINE_FILE)

    files_processed = 0
    with open(BASELINE_FILE, 'w') as file:
        for root, dirs, files in os.walk(MONITOR_DIR):
            for file in files:
                filepath = os.path.join(root, file)
                file_hash = calculate_hash(filepath)

                if file_hash:
                    file.write(f"{filepath}|{file_hash}\n")
                    files_processed += 1
                    print(f"Hashed: {filepath}")

    print(f"Baseline created with {files_processed} file.")


def main():
    print("File Integrity Monitor")
    print("A) Create new Baseline")
    print("B) Start Monitoring")

    choice = input("Select Option (A/B): ").upper()

    # if choice == 'A':
    # Add a function to create baseline.txt
    # elif choice == 'B':
    # Add a function to start monitoring
    # else:
    #    print("Invalid choice.")


if __name__ == "__main__":
    main()
