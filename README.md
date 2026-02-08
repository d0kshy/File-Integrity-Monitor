# File Integrity Monitor (FIM)
A Python-based File Integrity Monitor (FIM) that tracks changes in a target directory. It uses SHA-256 hashing to create a secure baseline and detects file creations, deletions, and content modifications.

# Simple Scheme
<img width="710" height="628" alt="Screenshot 2026-02-06 at 02 22 16" src="https://github.com/user-attachments/assets/c09a6ea7-34b0-449e-afec-05267f052f1c" />


## Features:
1. **Create Baseline:** Scans the directory and calculates a digital fingerprint (Hash) for every file.
2. **Real-time Monitoring:** Continuously compares the files to the baseline.
3. **Alerting:** Gives immediate console alerts for:
    - File Creation
    - File Deletion
    - Content Modification

## Technologies
1. **Python 3**
2. **Hashlib** (for SHA-256 hashing)
3. **OS Module** (for file system traversal)
