# This script is written by ShadowDara

# Github: https://github.com/ShadowDara

# Version 1.3.0

# GitHub Repository: https://github.com/ShadowDara/Search2.0

import os
import time

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

print("Folder path:", skript_verzeichnis, "\n\nLaunching Version 1.3.0 of sai - Search and Indexing Programme by ShadowDara.\n\n")


def change_file_timestamps(file_path, year, month, day, hour, minute, second):
    """
    Changes the access and modification timestamps of a file.

    Args:
        file_path (str): The path to the file whose timestamps are to be changed.
        year (int): Year for the new timestamp.
        month (int): Month for the new timestamp.
        day (int): Day for the new timestamp.
        hour (int): Hour for the new timestamp.
        minute (int): Minute for the new timestamp.
        second (int): Second for the new timestamp.
    """
    try:
        # Create a Unix timestamp from the provided date and time
        new_time = time.mktime((year, month, day, hour, minute, second, 0, 0, -1))

        # Update the file's access and modification times
        os.utime(file_path, (new_time, new_time))

        print(f"Timestamps for '{file_path}' successfully updated to {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def prompt_user_for_file_and_time():
    global year, month, day, hour, minute, second
    """
    Prompts the user to input the file path and new timestamp details, and then updates the file's timestamps.
    """

    # Get date and time details from the user
    try:
        print("Enter the new timestamp for the file:")
        year = int(input("Year (e.g., 2023): "))
        month = int(input("Month (1-12): "))
        day = int(input("Day (1-31): "))
        hour = int(input("Hour (0-23): "))
        minute = int(input("Minute (0-59): "))
        second = int(input("Second (0-59): "))

        # single or multipel files mode
        choice()

        # Call the function to change timestamps
        change_file_timestamps(file_path, year, month, day, hour, minute, second)
    except ValueError:
        print("Error: Invalid input. Please ensure all fields are filled with correct numeric values.")

def choice():
    choice = input("\nPress 1 for changing the edittime for 1 file.\nPress 2 for changing the edittime for all files in 1 folder (not for subfolders)\n\nYour Choice: ")

    if choice == '1':
        single_mode()

    elif choice == '2':
        folder_mode()

    else:
        print("\nThis was not a valid Input. Please try again")
        choice()

def single_mode():
    global file_path
    # Get file path from user
    file_path = input("Enter the file path to modify: ").strip()

def folder_mode():
    """
    Changes the access and modification timestamps for all files in a specified folder (excluding subfolders).
    """
    global file_path
    folder_path = input("\nEnter the folder path to modify all files in it: ").strip()

    # Check if the provided folder exists
    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
        return

    print(f"\nProcessing all files in folder: {folder_path}")

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Build the full file path
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            try:
                # Change timestamps for the file
                change_file_timestamps(file_path, year, month, day, hour, minute, second)
            except Exception as e:
                print(f"Failed to update timestamps for '{file_path}': {e}")

    print(f"\nAll files in '{folder_path}' have been processed.")


if __name__ == "__main__":
    # Run the user prompt
    prompt_user_for_file_and_time()

    # Keep the console window open until the user presses Enter
    input("Press Enter to exit...")
