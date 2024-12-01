# This script is written by ShadowDara
# Github: https://github.com/ShadowDara
# Version 1.2.0

import os

def search_index_file_with_paths(index_file, search_term):
    """
    Sucht in einer Index-Datei nach einem bestimmten Begriff und gibt Dateipfade aus.

    Args:
        index_file (str): Der Pfad zur Index-Datei.
        search_term (str): Der Suchbegriff.

    Returns:
        list: Eine Liste von Treffern mit vollständigen Dateipfaden.
    """
    matches = []
    current_dir = None  # Speichert das aktuelle Verzeichnis

    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # Wenn die Zeile ein Verzeichnis ist, aktualisieren wir current_dir
                if line.startswith("[DIR]"):
                    current_dir = line[5:]  # Entfernt das Präfix "[DIR] "
                elif current_dir and search_term.lower() in line.lower():
                    # Eine Datei gefunden, die den Suchbegriff enthält
                    file_path = os.path.join(current_dir, line)
                    matches.append(file_path)

    except FileNotFoundError:
        print(f"Error: Die Datei {index_file} wurde nicht gefunden.")
        return []

    return matches


if __name__ == "__main__":
    index_path = input("Geben Sie den Pfad zur Index-Datei ein: ")

    if not os.path.isfile(index_path):
        print(f"Die Datei '{index_path}' wurde nicht gefunden. Bitte prüfen Sie den Pfad.")
        input("\nDrücken Sie die Eingabetaste, um das Programm zu beenden...")
        exit()

    search_word = input("Geben Sie das zu suchende Wort ein: ")
    results = search_index_file_with_paths(index_path, search_word)

    if results:
        print(f"Gefundene Treffer für '{search_word}':")
        for match in results:
            print(match)
    else:
        print(f"Keine Treffer für '{search_word}' gefunden.")

    input("\nDrücken Sie die Eingabetaste, um das Programm zu beenden...")
