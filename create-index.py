# This script is written by ShadowDara
# Github: https://github.com/ShadowDara
# Version 1.2.0

import os

def index_folder(directory, output_file):
    """
    Indexes all files and folders in the given directory recursively,
    including file sizes.

    Args:
        directory (str): The path of the directory to index.
        output_file (str): The file where the index will be saved.
    """
    total_files = 0
    total_dirs = 0
    total_size = 0  # Gesamtspeicherplatz für Dateien

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(directory):
            # Write current directory to output file
            f.write(f"[DIR] {root}\n")
            total_dirs += 1

            # Write all files in the current directory
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)  # Dateigröße in Bytes
                    total_size += size
                    f.write(f"    {file} ({size / 1024:.2f} KB)\n")  # In KB formatieren
                except OSError as e:
                    f.write(f"    {file} (Fehler beim Abrufen der Dateigröße: {e})\n")
                total_files += 1

        # Write summary at the end of the file
        f.write("\n")
        f.write(f"---\n")
        f.write(f"Total directories: {total_dirs}\n")
        f.write(f"Total files: {total_files}\n")
        f.write(f"Total size: {total_size / (1024 * 1024):.2f} MB\n")  # In MB formatieren
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
