'''
Answer: 8549735
'''

file = open("input.txt", "r")

lines = file.read().splitlines()

total_cards = 0

copies = {'1': 0}

for line in lines:
    card_num = line.split(": ")[0].split(" ")[-1]

    numbers = line.split(": ")[1]

    win_nums = numbers.split(" | ")[0].split(" ")
    win_nums = [num for num in win_nums if num != ""]
    have_nums = numbers.split(" | ")[1].split(" ")
    have_nums = [num for num in have_nums if num != ""]

    loop_times = copies.get(card_num, 0) + 1

    match_count = 0
    for have_num in have_nums:
        if have_num in win_nums:
            match_count += 1

    for i in range(loop_times):
        for i in range(1, match_count + 1):
            copy_count = copies.get(str(int(card_num) + i))
            if copy_count is None:
                copies[str(int(card_num) + i)] = 1
            else:
                copies[str(int(card_num) + i)] += 1

for key, value in copies.items():
    total_cards += value
total_cards += len(lines)
print(total_cards)
