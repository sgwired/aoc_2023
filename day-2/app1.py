import re
f = open("input.txt", "r")
lines = f.readlines()

MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}



def is_game_possible(line):
    games = line.split(":")[1].split(";")
    for game in games:
        # print(game)
        for num_cubes in game.split(','):
            num, color = num_cubes.split()
            print(num, color)
            print(MAX_CUBES[color])
            if int(num) > MAX_CUBES[color]:
                return False
    return True


def main():
    TOTAL = 0
    index = 0
    for line in lines: 
        if is_game_possible(line):
            print(f"Game {index + 1} is possible")
            TOTAL += (index + 1)
        else:
            print(f"Game {index + 1} is NOT possible")
        index += 1

    print("the total", TOTAL)

if __name__ == '__main__':
    main()