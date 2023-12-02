'''
Answer: 54911
'''

file = open("input.txt", "r")

lines = file.read().splitlines()

round_power_sum = 0
for line in lines:
    # game_id = line.split(" ")[1].replace(":", "")

    game_rounds = line.split(": ")[1]
    game_rounds = game_rounds.split("; ")

    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game_round in game_rounds:
        cubes = game_round.split(", ")
        for cube in cubes:
            quantity = cube.split(" ")[0]
            color = cube.split(" ")[1]
            if min_cubes[color] < int(quantity):
                min_cubes[color] = int(quantity)
    power = int(min_cubes['red']) * int(min_cubes['green']) * int(min_cubes['blue'])
    round_power_sum += power
print(round_power_sum)

