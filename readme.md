uptime.py
A simple Python script to report the system uptime in seconds.

Description
uptime.py reads the system uptime from /proc/uptime and prints the number of seconds the system has been running. This script is intended for Linux environments where /proc/uptime is available.

Usage
bash
python uptime.py
This will output:

Code
Uptime: <number_of_seconds> seconds
How it works
The script reads the first value from /proc/uptime, which represents the total number of seconds the system has been up.
It prints this value in a human-readable format.
Example
Code
Uptime: 123456.78 seconds
Requirements
Python 3
Linux environment (with /proc/uptime available)
