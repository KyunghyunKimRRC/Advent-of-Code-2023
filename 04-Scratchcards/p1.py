'''
Answer: 21213
'''

file = open("input.txt", "r")

lines = file.read().splitlines()

total_points = 0
for line in lines:
    numbers = line.split(": ")[1]

    win_nums = numbers.split(" | ")[0].split(" ")
    win_nums = [num for num in win_nums if num != ""]
    have_nums = numbers.split(" | ")[1].split(" ")
    have_nums = [num for num in have_nums if num != ""]

    points = 0
    for have_num in have_nums:
        if have_num in win_nums:
            if points == 0:
                points = 1
            else:
                points *= 2

    total_points += points

print(total_points)
