import hashlib
import os
import time


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
