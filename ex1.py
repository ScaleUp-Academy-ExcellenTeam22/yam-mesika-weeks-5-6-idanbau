import os
import re

#match pattern to check for files in
MATCH_PATTERN: str = "deep"


def deep_files(path: str):
    """
    :param path: the current path we'd like to check
    :return: the files that accept the rule in the pattern
    """
    return [f for f in os.listdir(path) if re.search(MATCH_PATTERN, f)]
