"""Test helper functions that can be reused"""


def search_str_in_file(file_path, word):
    """searches a string in file and returns true if found an false if not"""
    with open(file_path, 'r', encoding="utf8") as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            return True
        return False
