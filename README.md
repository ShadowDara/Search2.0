# sai - Search and Indexing Programme by ShadowDara Version 1.2.0

This File is about a little Explanation for your Version of sai - Search and Indexing Programme.

## Description

This project consists of two Python scripts designed to work together to manage and search through large directory structures efficiently:

- Indexing Script: Creates an index file listing all directories and files in a specified folder, including their sizes.
- Search Script: Searches the generated index file for specific terms and returns the full paths of matching files.

These tools are ideal for system administrators, developers, or anyone who needs a quick way to analyze and locate files in large file systems.

## How to use
- install Python - min python 3.6 or higher (recommended) needed
- run the script
- follow the instructions from the python script or Check this File, it contains a explanation for every included python script.


# Downloads
- Changelogs are at the end of this File.

### [Version 1.1.0](https://github.com/ShadowDara/Search2.0/releases/tag/V.1.1.0)

### [Version 1.0.0](https://github.com/ShadowDara/Search2.0/releases/tag/V.1.0.0)


# create-index.py

### Description
This Python script indexes all directories and files within a specified folder (recursively) and writes the details into an output file. Additionally, it provides a summary of:

- Directories and their names.
- Files in each directory, including their sizes.
- Total number of files and directories.
- Total storage size of all files in megabytes (MB).

Finally, the script saves the results to a file.

### Features
Easy to customize.
Handles large directory structures efficiently.
Useful for generating reports, backups, or directory overviews.

### How to use
- Open the File with Python 3.6 or higher
- Paste in the Folder path (e.g. ``C:\Users\"Your Username"\Documents`` This is the folder path for your documents folder. Be aware you can't this path, because you probably have a different username.)
- After pasting the folder path press enter
- now you need a file in which the indexing is saved
- just create an empty File (e.g. ``index.txt``) and paste the folder path in the terminal (e.g. ``C:\Users\"Your Username"\Documents\index.txt`` If the file is located in your documents folder, but remember, you have a different username)
- BE AWARE THAT YOU ARE NOT OVERWRITING ANY OTHER OF YOUR IMPORTANT FILES, WHEN CHOOSING YOUR INDEX FILE.
- when you press enter and no error message apeared, the programm should be working properly


# search-through-index.py

### Description
This Python script searches through an index file (generated by a script like the one shown earlier) for a specific term. If the term is found, it outputs the full file paths of the matching files.

The script is helpful for quickly locating files or directories listed in a pre-generated index file based on keywords.

### Key Features
Tracks directory structure: The script understands how files are organized within directories, making the file paths accurate.
Case-insensitive search: Matches terms regardless of case.
Graceful error handling: If the file doesn’t exist, the script provides a clear error message.

### Example Use Cases
Quickly locate files in a large directory structure using a pre-generated index file.
Perform text-based searches on file names or metadata in an indexed directory list.

### How to use
- Open the File with Python 3.6 or higher


# Credits

This Projekt is made by ShadowDara


# Licence
- MIT Licence
- see LICENSE File for more Information


# Changelogs

## V.1.2.0
- changed Name to "sai - Search and Indexing Programme"
- changed language to english
- added the size for each File in the (via "create-index.py") created Index File
- added ``INFO.md``

## V.1.1.0
**added Statistics at the end of the (via "create-index.py") created Index File**

``Total directories: XXXX``

``Total files: XXXX``

``Total size: XXXX.XX MB``

``Total items: XXXX``

## V.1.0.0
- First Release
