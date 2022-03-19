from typing import Iterable


def interleave(*iterables: Iterable):
    """
    This function receive a list of iterables and returns a generator of each iterable item
    it removes each iterable that went to his end.
    :param iterables: A list of iterables to walk through
    """
    current_iterables_iterators = [iter(iterator) for iterator in iterables]
    while len(current_iterables_iterators) != 0:
        for iterable in current_iterables_iterators:
            try:
                yield next(iterable)
            except StopIteration:
                current_iterables_iterators.remove(iterable)
