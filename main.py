import hashlib
import os
import time

MONITOR_DIR = "./test_folder"
BASELINE_FILE = "baseline.txt"


def log_event(message):
    print(message)
    with open("log.txt", 'a') as file:
        file.write(message+'\n')


def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()

    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None


def create_baseline():
    print("\n----- CREATING NEW BASELINE -----")

    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)
        print(f"Created directory: {MONITOR_DIR}")

    if os.path.exists(BASELINE_FILE):
        os.remove(BASELINE_FILE)

    files_processed = 0
    with open(BASELINE_FILE, 'w') as baseline:
        for root, dirs, files in os.walk(MONITOR_DIR):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_hash(filepath)

                if file_hash:
                    baseline.write(f"{filepath}|{file_hash}\n")
                    files_processed += 1
                    print(f"Hashed: {filepath}")

    print(f"Baseline created with {files_processed} files.")


def start_monitoring():
    print("\n----- STARTING MONITORING MODE -----")

    baseline_db = {}

    try:
        with open(BASELINE_FILE, 'r') as f:
            for line in f:
                filepath, saved_hash = line.strip().split("|")
                baseline_db[filepath] = saved_hash
    except FileNotFoundError:
        print("Error: No baseline found! Run with option 'A' first.")
        return

    print(f"Monitoring {len(baseline_db)} files... (Press Ctrl+C to stop)")

    while True:
        time.sleep(1)

        current_files_on_disk = set()

        for root, dirs, files in os.walk(MONITOR_DIR):
            for filename in files:
                filepath = os.path.join(root, filename)
                current_files_on_disk.add(filepath)

                current_hash = calculate_hash(filepath)
                if not current_hash:
                    continue

                if filepath not in baseline_db:
                    log_event(f"[ALERT] NEW FILE DETECTED: {filepath}")
                    baseline_db[filepath] = current_hash
                elif baseline_db[filepath] != current_hash:
                    log_event(f"[ALERT] FILE CHANGED: {filepath}")
                    log_event(f"     Old Hash: {baseline_db[filepath]}")
                    log_event(f"     New Hash: {current_hash}")
                    baseline_db[filepath] = current_hash

        for filepath in list(baseline_db.keys()):
            if filepath not in current_files_on_disk:
                log_event(f"[ALERT] FILE DELETED: {filepath}")
                del baseline_db[filepath]


def main():
    print("File Integrity Monitor")
    print("A) Create new Baseline")
    print("B) Start Monitoring")

    choice = input("Select Option (A/B): ").upper()

    if choice == 'A':
        create_baseline()
    elif choice == 'B':
        start_monitoring()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
