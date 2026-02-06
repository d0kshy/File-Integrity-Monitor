# File Integrity Monitor (FIM)
A Python-based File Integrity Monitor (FIM) that tracks changes in a target directory. It uses SHA-256 hashing to create a secure baseline and detects file creations, deletions, and content modifications.

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