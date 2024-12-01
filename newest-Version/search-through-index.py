# This script is written by ShadowDara
# Github: https://github.com/ShadowDara
# Version 1.2.0

import os

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


if __name__ == "__main__":
    index_path = input("Enter the path to the index file: ")

    if not os.path.isfile(index_path):
        print(f"The file '{index_path}' was not found. Please check the path.")
        input("\nPress Enter to exit the program...")
        exit()

    search_word = input("Enter the word to search for: ")
    results = search_index_file_with_paths(index_path, search_word)

    if results:
        print(f"Matches found for '{search_word}':")
        for match in results:
            print(match)
    else:
        print(f"No matches found for '{search_word}'.")

    input("\nPress Enter to exit the program...")
