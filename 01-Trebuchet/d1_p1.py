'''
Answer: 54968
'''

import sys

class OpenFile:
    '''This class will open, read, and close a file.'''
    def __init__(self, filename, mode):
        '''Initialize the OpenFile object with the filename and mode'''
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        '''Opens a file using initialized filename and mode values'''
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_trace):
        '''Closes the opened file'''
        self.file.close()

def main():
    with OpenFile("input.txt", "r") as file:
        lines = file.readlines()
    result = 0
    for line in lines:
        first_digit, second_digit = None, None
        while first_digit is None and second_digit is None:
            for front_char, back_char in zip(line, reversed(line)):
                if front_char.isdigit() and first_digit is None:
                    first_digit = front_char
                if back_char.isdigit() and second_digit is None:
                    second_digit = back_char
        result += int(first_digit + second_digit)
    print(result)



if __name__ == "__main__":
    main()