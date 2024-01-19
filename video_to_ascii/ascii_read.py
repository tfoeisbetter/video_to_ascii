import time

from .constants import TXT_FILE
from .utils import clear_console

# function to read ASCII from file frame by frame
def read_ascii_from_file(num_of_lines, fps):
    file = open(TXT_FILE, "r")
    content = file.readlines()

    start = 0
    end = num_of_lines

    while end < len(content):
        time.sleep(1 / int(fps))
        clear_console()

        for line in content[start:end]:
            print(line, end = '')

        start += (num_of_lines)
        end += (num_of_lines)

    file.close()
    clear_console()