from clear import clear

SCORES_FILE_NAME = "Scores/scores.txt"
SCORES_FILE_FLASK = "./Scores.txt"
LAST_SCORES = "./Scores/Last_scores.txt"
LAST_SCORES_FLASK = "./Last_scores.txt"
BAD_RETURN_CODE = "ERROR CODE 504"


def screen_cleaner():
    clear()


def transfer_and_clear_file(src_file, cp_file):
    try:
        with open(src_file, 'r') as src:  # Open the source file for reading
            current_score = src.read().strip()  # Read the contents and remove any whitespace
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{src_file}' not found")  # Raise an error if the source file is not found

    try:
        with open(cp_file, 'w') as cp:  # Open the destination file for writing
            cp.write(current_score)  # Write the contents of the source file to the destination file
    except PermissionError:
        raise PermissionError(
            f"Cannot write to destination file '{cp_file}'")  # Raise an error if unable to write to the destination file

    try:
        with open(src_file, 'w') as src:  # Open the source file again for writing
            src.write('')  # Clear the contents of the source file
    except PermissionError:
        raise PermissionError(
            f"Cannot clear source file '{src_file}'")  # Raise an error if unable to clear the source file

    return True  # Return True to indicate successful transfer and clearing of files
