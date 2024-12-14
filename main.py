# This script is written by ShadowDara

# Github: https://github.com/ShadowDara

# Version 1.3.0

# GitHub Repository: https://github.com/ShadowDara/Search2.0

import os
import time

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

print("Folder path:", skript_verzeichnis, "\n\nLaunching Version 1.3.0 of sai - Search and Indexing Programme by ShadowDara.\n\n")

def cpu_benchmark():

    input("\nPress Enter to start ")

    elapsed_times = []

    for e in range(1, 101):

        start_time = time.time()

        for i in range(1, 1_000_001):
            pass

        end_time = time.time()

        elapsed_time = end_time - start_time
        elapsed_times.append(elapsed_time)

        print(f"Test {e}: Das Programm hat {elapsed_time:.6f} Sekunden gebraucht, um auf 1 Million zu zählen.")

    average_time = sum(elapsed_times) / len(elapsed_times)

    print(f"\nDer Mittelwert der Laufzeiten beträgt {average_time:.6f} Sekunden.")

    input()

def choice():
    choice = input("\n0 Press 0 to exit the Programm.\n1 Press 1 to run a CPU Benchmark.\n\nYour Choice: ")

    if choice == '0':
        pass

    elif choice == '1':
        cpu_benchmark()

    elif choice == '2':
        pass

    elif choice == '3':
        pass

    elif choice == '4':
        pass

    else:
        print("\n Invalid Input.! Please try again!")
        choice()

if __name__ == "__main__":
    choice()