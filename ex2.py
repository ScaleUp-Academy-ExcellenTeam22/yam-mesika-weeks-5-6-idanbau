import datetime
import random

INPUT_PATTERN = "Please enter date in YYYY-MM-DD:"


def read_date() -> datetime.datetime:
    """
    :return: date object of YYYY-MM-INPUT_
    """
    return datetime.datetime.fromisoformat(input(INPUT_PATTERN))


def getRandomDate(first_date: datetime.datetime, second_date: datetime.datetime) -> datetime.date:
    """

    :param first_date:first date as lower bound date
    :param second_date:second date as higher bound date
    :return: a random date between the two.
    """
    second_difference = int(second_date.timestamp() - first_date.timestamp())
    return datetime.date.fromtimestamp(first_date.timestamp() + random.randint(0, second_difference))
