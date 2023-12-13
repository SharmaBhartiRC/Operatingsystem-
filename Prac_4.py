import os
import sys
import stat
import time

def get_file_details(file_path):
    try:
        # Get file stat information
        file_stat = os.stat(file_path)

        # Extract owner access permissions
        permissions = stat.filemode(file_stat.st_mode)

        # Get file access time
        access_time = time.ctime(file_stat.st_atime)

        # Print file details
        print(f"File: {file_path}")
        print(f"Owner access permissions: {permissions}")
        print(f"File access time: {access_time}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python file_details.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    get_file_details(file_name)
