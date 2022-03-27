import re

BLOCK_SIZE: int = 1024
BINARY_PATTERN = b'[a-z]{5,}!'


def read_binary_file(file_path: str, block_size: int):
    """
    Read binary function which get a path and block size and return a generator of it for each block_size data
    :param file_path: The path for our program
    :param block_size: The size of each block to read
    :return: A block of the file to read
    """
    with open(file_path, 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return None


def find_binary_string(file_path: str, binary_string: re.Pattern):
    """
    Function which get system path and extract a string that includes the binary string
    :param file_path: the path of the system 
    :param binary_string:
    :return: A list of words from the file
    """
    strings = [re.findall(binary_string, current_block) for current_block in read_binary_file(file_path, BLOCK_SIZE)
               if re.findall(binary_string, current_block)]
    return strings
