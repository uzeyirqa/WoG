from Utils import SCORES_FILE_NAME
from os.path import exists


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    contents = None
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        contents = file.read()
        file.close()
    if contents:
        current_score = int(contents) + points_of_winning
    else:
        current_score = points_of_winning
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(current_score))
    file.close()
    return current_score
