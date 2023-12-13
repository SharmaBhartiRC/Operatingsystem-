import subprocess
import sys

def copy_file(source_path, destination_path):
    try:
        # Using system call to copy file (Linux/Unix)
        subprocess.run(["cp", source_path, destination_path])

        # For Windows, you can use the following system call:
        # subprocess.run(["copy", source_path, destination_path])

        print(f"File copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if source and destination paths are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python copy_file.py <source_path> <destination_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    destination_path = sys.argv[2]

    copy_file(source_path, destination_path)
