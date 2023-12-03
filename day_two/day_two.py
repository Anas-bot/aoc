with open("input.txt", "r") as f:
    lines = f.readlines()


def part_one():
    cubes = {"red": 12, "green": 13, "blue": 14}
    game_ids_sum = 0
    for games in lines:
        game_id = int(games[4:games.index(":")])
        final_count = 0
        for game in games[games.index(":") + 1:].split(";"):
            count = 0
            for game_cubes in game.split(","):
                if cubes[game_cubes.strip()[2:].strip()] >= int(game_cubes.strip()[0:2]):
                    print(f'game_id:{game_id}, color: {game_cubes.strip()[2:].strip()}, num:{game_cubes.strip()[0:2]}')  # noqa: E501
                    count += 1
            if count == len(game.split(",")):
                final_count += 1
        if final_count == len(games[games.index(":") + 1:].split(";")):
            game_ids_sum += game_id


def part_two():
    power_sum = 0
    for games in lines:
        max_red = max_green = max_blue = 0
        for game in games[games.index(":") + 1:].split(";"):
            for game_cubes in game.split(","):
                if game_cubes.strip()[2:].strip() == "blue" and int(game_cubes.strip()[0:2]) > max_blue:  # noqa: E501
                    max_blue = int(game_cubes.strip()[0:2])
                elif game_cubes.strip()[2:].strip() == "red" and int(game_cubes.strip()[0:2]) > max_red:  # noqa: E501
                    max_red = int(game_cubes.strip()[0:2])
                elif game_cubes.strip()[2:].strip() == "green" and int(game_cubes.strip()[0:2]) > max_green:  # noqa: E501
                    max_green = int(game_cubes.strip()[0:2])

        power_sum += (max_red * max_green * max_blue)
        max_red = max_green = max_blue = 0


part_two()
