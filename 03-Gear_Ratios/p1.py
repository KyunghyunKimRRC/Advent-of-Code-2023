'''
Answer: 536202
'''

file = open("input.txt", "r")

lines = file.read().splitlines()
rows = len(lines)
columns = len(lines[0])

def is_symbol(char):
    return char in ['/', '*', '@', '=', '-', '$', '+', '#', '%', '&']

part_number_sum = 0
number = ""
for row in range(rows):
    for col in range(columns):
        if lines[row][col].isdigit():
            number = number + lines[row][col]
        if (lines[row][max(0, col-1)].isdigit() and not lines[row][col].isdigit() and (col != 0)) or (lines[row][col].isdigit() and (columns == col + 1)):
            valid_number = False
            for r in range(max(0, row - 1), min(rows, row + 2)):
                for c in range(max(0, col - len(number) - 1), min(columns, col + 1)):
                    if is_symbol(lines[r][c]):
                        valid_number = True
            if valid_number == True:
                part_number_sum += int(number)
            number = ""

print(part_number_sum)
