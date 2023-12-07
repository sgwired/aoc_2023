import re
f = open("input.txt", "r")
lines = f.readlines()





def is_game_possible(line):
    MIN_CUBES = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    games = line.split(":")[1].split(";")
    print(games)
    for game in games:
        # print(game)
        for num_cubes in game.split(','):
            num, color = num_cubes.split()
            # print(num, color)
            # print(MIN_CUBES[color])
            if int(num) >= MIN_CUBES[color]:
                MIN_CUBES[color] = int(num)
                # return False
                # print(MIN_CUBES[color])
    # print(MIN_CUBES)
    # print(int(MIN_CUBES['red']) * int(MIN_CUBES['green']) * int(MIN_CUBES['blue'])))
    return int(MIN_CUBES['red']) * int(MIN_CUBES['green']) * int(MIN_CUBES['blue'])


def main():
    TOTAL = 0
    index = 0
    for line in lines: 
        value = is_game_possible(line)
        print(value)
        TOTAL += value

           

    print("the total", TOTAL)

if __name__ == '__main__':
    main()