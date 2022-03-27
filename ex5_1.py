import os
import re
import datetime
import random

# Match pattern to check for all files with deep on it.
FILES_DEEP_PATTERN: str = "deep"
INPUT_DATE_MESSAGE = "Please enter date in YYYY-MM-DD:"
MONDAY_MESSAGE = "אין לי ויניגרט"


def show_files_by_pattern(system_path: str, match_pattern: str):
    """
    Function with receive system path and pattern and returns a
    list of files with includes the pattern in its own name.
    :param match_pattern: Our wanted pattern to check for files name
    :param system_path: The current path to check for pattern files
    :return: The files list that accept the rule in the pattern
    """
    return [file for file in os.listdir(system_path) if os.path.isfile(file) and re.search(match_pattern, file)]


def read_date(input_message: str) -> datetime.datetime:
    """
    Read date from the user in YYYY-MM-DD format
    :param input_message: Message to console about the input data
    :return: date object of YYYY-MM-DD pattern date
    """
    return datetime.datetime.fromisoformat(input(input_message))


def get_random_date(first_date: datetime.datetime, second_date: datetime.datetime) -> datetime.date:
    """
    :param first_date:first date as lower bound date
    :param second_date:second date as higher bound date
    :return: a random date between the two.
    """
    second_difference = int(second_date.timestamp() - first_date.timestamp())
    return datetime.date.fromtimestamp(first_date.timestamp() + random.randint(0, second_difference))


def check_if_monday(date: datetime.datetime.date, message: str):
    """
    Function to check if monday and if yes output a message
    :param date: Current date to check for it
    :param message: Output message if current date is monday
    """
    if date.isoweekday() == 1:
        print(message)
