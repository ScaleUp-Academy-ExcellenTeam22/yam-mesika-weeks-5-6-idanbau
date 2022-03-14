def join(*lists: list, seperator: chr = '-'):
    """

    :param lists: unlimited list to combine
    :param seperator: seperator between each list
    :return: return the list with seperator in the end (without the last character)
    """
    return [cell for curr_list in lists for cell in curr_list + [seperator]][:-1]


