# AV-Check
This script checks for running antivirus processes on a Windows machine using the WMI (Windows Management Instrumentation) interface.
## Features:
- Detects antivirus processes from a list of common antivirus vendors.
- Case-insensitive matching for process names.

## Prerequisites:
- Python 3.x
- WMI module (`pip install wmi`)

## How to Use:
1. Install the required WMI module:
   pip install wmi
   python3 AV-check.py
