'''
Answer: 2476
'''

file = open("input.txt", "r")

lines = file.read().splitlines()

round_id_sum = 0
for line in lines:
    valid_game = True
    game_id = line.split(" ")[1].replace(":", "")

    game_rounds = line.split(": ")[1]
    game_rounds = game_rounds.split("; ")


    for game_round in game_rounds:
        total_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        cubes = game_round.split(", ")
        for cube in cubes:
            quantity = cube.split(" ")[0]
            color = cube.split(" ")[1]
            total_cubes[color] += int(quantity)
        if (total_cubes['red'] > 12) or (total_cubes['green'] > 13) or (total_cubes['blue'] > 14):
            valid_game = False
    if valid_game is True:
        round_id_sum += int(game_id)
print(round_id_sum)

