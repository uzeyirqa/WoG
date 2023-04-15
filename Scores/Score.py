from Utils import SCORES_FILE_NAME
from os.path import exists


def add_score(lvl_sel):
    try:
        points = (int(lvl_sel) * 3) + 5  # Convert lvl_sel to int and calculate the points of winning based on the
        # difficulty level
    except ValueError:
        raise ValueError(
            "Invalid argument: lvl_sel must be an integer")  # Raise an error if lvl_sel is not a valid integer

    if exists(SCORES_FILE_NAME):  # Check if the score file exists
        with open(SCORES_FILE_NAME, 'r') as scores:  # Open the score file for reading
            scores_list = [int(x.strip()) for x in
                           scores.readlines()]  # Read all lines in the file as a list and convert items to integers
        current_score = sum(scores_list)  # Sum the values in the list to get the current score
    else:
        current_score = 0  # If the score file does not exist, set the current score to 0

    update_score = current_score + points  # Calculate the updated score

    with open(SCORES_FILE_NAME, 'w') as scores:  # Open the score file for writing
        scores.write(str(update_score))  # Write the updated score to the score file as a string

    return update_score  # Return the updated score
