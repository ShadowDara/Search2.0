# This script is written by ShadowDara

# Github: https://github.com/ShadowDara

# Version 1.3.0

# GitHub Repository: https://github.com/ShadowDara/Search2.0

import os
from datetime import datetime

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

print("Folder path:", skript_verzeichnis, "\n\nLaunching Version 1.3.0 of sai - Search and Indexing Programme by ShadowDara.\n\n")

def index_folder(directory, output_file):
    """
    Indexes all files and folders in the given directory recursively,
    including file sizes and edit times.

    Args:
        directory (str): The path of the directory to index.
        output_file (str): The file where the index will be saved.
    """
    total_files = 0
    total_dirs = 0
    total_size = 0  # Total size of all files in bytes

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(directory):
            # Write the current directory to the output file
            f.write(f"[DIR] {root}\n")
            total_dirs += 1

            # Write all files in the current directory
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)  # File size in bytes
                    total_size += size

                    # Get and format the last modification time
                    edit_time = os.path.getmtime(file_path)
                    edit_time_formatted = datetime.fromtimestamp(edit_time).strftime('%Y-%m-%d %H:%M:%S')

                    # Write file information
                    f.write(f"    {file} ({size / 1024:.2f} KB, Modified: {edit_time_formatted})\n")
                except OSError as e:
                    f.write(f"    {file} (Error getting file size or time: {e})\n")
                total_files += 1

        # Write a summary at the end of the file
        f.write("\n")
        f.write(f"---\n")
        f.write(f"Total directories: {total_dirs}\n")
        f.write(f"Total files: {total_files}\n")
        f.write(f"Total size: {total_size / (1024 * 1024):.2f} MB\n")  # Format in MB
        f.write(f"Total items: {total_dirs + total_files}\n")

    print(f"Indexing completed. Indexed {total_dirs} directories, {total_files} files.")
    print(f"Total size: {total_size / (1024 * 1024):.2f} MB")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Example usage:
    folder_to_index = input("Enter the folder path to index: ")
    output_path = input("Enter the output file path (e.g., index.txt): ")

    if not os.path.exists(folder_to_index):
        print("Error: The specified folder does not exist.")
    else:
        index_folder(folder_to_index, output_path)
