# This script is written by ShadowDara

# Github: https://github.com/ShadowDara

# Version 1.3.0

# GitHub Repository: https://github.com/ShadowDara/Search2.0

import os
import time

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

print("Folder path:", skript_verzeichnis, "\n\nLaunching Version 1.3.0 of sai - Search and Indexing Programme by ShadowDara.\n\n")


def search_index_file_with_paths(index_file, search_term):
    """
    Searches an index file for a specific term and returns file paths.

    Args:
        index_file (str): The path to the index file.
        search_term (str): The term to search for.

    Returns:
        list: A list of matches with full file paths.
    """
    matches = []
    current_dir = None  # Stores the current directory

    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # If the line represents a directory, update current_dir
                if line.startswith("[DIR]"):
                    current_dir = line[5:]  # Remove the prefix "[DIR] "
                elif current_dir and search_term.lower() in line.lower():
                    # A file containing the search term was found
                    file_path = os.path.join(current_dir, line)
                    matches.append(file_path)

    except FileNotFoundError:
        print(f"Error: The file {index_file} was not found.")
        return []

    return matches


def search_files_by_size(index_file, size_threshold, larger_than=True):
    """
    Searches the index file for files larger or smaller than the given size threshold.

    Args:
        index_file (str): The path to the index file.
        size_threshold (int): The file size threshold in bytes.
        larger_than (bool): If True, find files larger than the threshold; if False, find files smaller.

    Returns:
        list: A list of matches with full file paths.
    """
    matches = []
    current_dir = None  # Stores the current directory

    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # If the line represents a directory, update current_dir
                if line.startswith("[DIR]"):
                    current_dir = line[5:]  # Remove the prefix "[DIR] "
                elif current_dir and "(" in line:
                    # Extract the size from the line, assuming the format "file_name (size KB)"
                    parts = line.split('(')
                    file_name = parts[0].strip()
                    size_str = parts[1].replace(')', '').strip()  # Extract size in KB

                    try:
                        size = float(size_str) * 1024  # Convert to bytes
                        if (larger_than and size > size_threshold) or (not larger_than and size < size_threshold):
                            file_path = os.path.join(current_dir, file_name)
                            matches.append(file_path)
                    except ValueError:
                        continue  # Skip lines where size is not in the expected format

    except FileNotFoundError:
        print(f"Error: The file {index_file} was not found.")
        return []

    return matches


def search_files_by_date(index_file, target_date):
    """
    Searches the index file for files modified on a specific date.

    Args:
        index_file (str): The path to the index file.
        target_date (str): The date in YYYY-MM-DD format.

    Returns:
        list: A list of matches with full file paths.
    """
    matches = []
    current_dir = None  # Stores the current directory

    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # If the line represents a directory, update current_dir
                if line.startswith("[DIR]"):
                    current_dir = line[5:]  # Remove the prefix "[DIR] "
                elif current_dir and "Last modified" in line:
                    # Extract the date from the line
                    parts = line.split('Last modified: ')
                    file_name = parts[0].strip()
                    last_modified_date = parts[1].strip()

                    if target_date in last_modified_date:  # Check if the date matches
                        file_path = os.path.join(current_dir, file_name)
                        matches.append(file_path)

    except FileNotFoundError:
        print(f"Error: The file {index_file} was not found.")
        return []

    return matches

def choice():

    choice = input("\n1 Press 1 to serch for a word in the Index File.\n2 Press 2 to search for small or large Files.\n3 Press 3 to search for a file with the modification date.\n4 Press 4 to view the stats at the end of the index File.\n\n")

    if choice == '1':
        search_word = input("Enter the word to search for: ")
        results = search_index_file_with_paths(index_path, search_word)

        if results:
            print(f"Matches found for '{search_word}':")
            for match in results:
                print(match)
        else:
            print(f"No matches found for '{search_word}'.")

    elif choice == '2':
        # Search for large or small files
        size_option = input("Search for files larger (L) or smaller (S) than the threshold? (L/S): ").strip().lower()
        size_threshold = int(input("\nEnter the file size threshold in KB: ")) * 1024  # Convert KB to bytes

        if size_option == 'l':
            results_size = search_files_by_size(index_path, size_threshold, larger_than=True)
        else:
            results_size = search_files_by_size(index_path, size_threshold, larger_than=False)

        if results_size:
            print(f"\nMatches for files {'larger' if size_option == 'l' else 'smaller'} than the threshold:")
            for match in results_size:
                print(match)
        else:
            print(f"No matches found for files {'larger' if size_option == 'l' else 'smaller'} than the threshold.")

    elif choice == '3':

        # Search for files by modification date
        target_date = input("\nEnter the modification date to search for (YYYY-MM-DD): ")
        results_date = search_files_by_date(index_path, target_date)

        if results_date:
            print(f"\nMatches for files modified on {target_date}:")
            for match in results_date:
                print(match)
        else:
            print(f"No matches found for files modified on {target_date}.")

    elif choice == '4':
        # view the stats at the end of the index file
        pass

    else:
        print("\n Invalid Input! Please try again.\n")
        choice()

def newindex():
    # option to save your result to a new index file
    pass

if __name__ == "__main__":
    index_path = input("Enter the path to the index file: ")

    if not os.path.isfile(index_path):
        print(f"The file '{index_path}' was not found. Please check the path.")
        input("\nPress Enter to exit the program...")
        exit()

    choice()

    newindex()

    input("\nPress Enter to exit the program...")
