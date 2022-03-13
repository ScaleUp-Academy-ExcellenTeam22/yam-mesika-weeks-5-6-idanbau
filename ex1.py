import os
import re

MATCH_PATTERN = "deep"


def deep_files(path: str):
    return [f for f in os.listdir(path) if re.search(MATCH_PATTERN, f)]
