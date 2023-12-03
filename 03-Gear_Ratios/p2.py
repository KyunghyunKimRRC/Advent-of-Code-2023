'''
Answer: 78272573
'''

file = open("input.txt", "r")

lines = file.read().splitlines()
rows = len(lines)
columns = len(lines[0])

def is_symbol(char):
    return char in ['*']

gear_ratio_sum = 0
numbers_dict = {}
number_id = '1'
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
                        dict_id = f"{number}-{row}-{col}"
                        numbers_dict[dict_id] = {
                            'number': number,
                            'row': r,
                            'col': c
                        }
            number = ""

processed_pair = set()
for num1, info1 in numbers_dict.items():
    for num2, info2 in numbers_dict.items():
        if num1 != num2 and info1['row'] == info2['row'] and info1['col'] == info2['col']:
            pair = frozenset([num1, num2])
            if pair not in processed_pair:
                processed_pair.add(pair)
                ratio = int(info1['number']) * int(info2['number'])
                gear_ratio_sum += ratio

print(gear_ratio_sum)
