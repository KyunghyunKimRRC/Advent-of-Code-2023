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
        word_to_number = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        norm_line = line
        for i in range(len(line) - 4):
            substring = norm_line[i:i+5]
            for word, number in word_to_number.items():
                if word in substring:
                    norm_line = norm_line.replace(word, number)
        reversed_line = line[::-1]
        for i in range(len(reversed_line) - 4):
            substring = reversed_line[i:i+5]
            for word, number in word_to_number.items():
                if word[::-1] in substring:
                    reversed_line = reversed_line.replace(word[::-1], number)
        while first_digit is None and second_digit is None:
            for front_char, back_char in zip(norm_line, reversed_line):
                if front_char.isdigit() and first_digit is None:
                    first_digit = front_char
                if back_char.isdigit() and second_digit is None:
                    second_digit = back_char
        result += int(first_digit + second_digit)
    print(result)

if __name__ == "__main__":
    main()
