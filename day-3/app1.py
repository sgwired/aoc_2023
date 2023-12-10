import sys
sys.path.append("..")
from common.utils import read_lines_from_file

def is_symbol(char):
    #Check to see if the character is a symbol
    return char not in '0123456789.'

def get_full_number(grid, row, col):
    #find the full number by moving to the left and right
    #go to the left to find the start of the number
    left_bound = col
    while left_bound > 0 and grid[row][left_bound - 1].isdigit():
        left_bound -= 1

    # go to the right to find the end of the number
    right_bound = col
    while right_bound < len(grid[row]) - 1 and grid[row][right_bound + 1].isdigit():
        right_bound += 1

    return grid[row][left_bound:right_bound + 1], left_bound, right_bound

def is_next_to_symbol(diagram, row, col, left_bound, right_bound):
    """is the number is next to a symbol."""

    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            for index in range(left_bound, right_bound + 1):
                adj_row = row + row_offset
                adj_col = col + col_offset + index - left_bound
                if 0 <= adj_row < len(diagram) and 0 <= adj_col < len(diagram[0]):
                    if is_symbol(diagram[adj_row][adj_col]):
                        return True
    return False

def add_part_numbers(diagram):
    total = 0
    visited = set()

    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col].isdigit() and (row, col) not in visited:
                number, left_bound, right_bound = get_full_number(diagram, row, col)
                if number and is_next_to_symbol(diagram, row, col, left_bound, right_bound):
                    total += int(number)
                    print(f"Found a part number at: ({row}, {left_bound}-{right_bound}): {number}, The Sum: {total}")

                # set all the digits of the number as visited
                for index in range(left_bound, right_bound + 1):
                    visited.add((row, index))

    return total


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'ex1.txt'
    diagram = read_lines_from_file(file_path)
    total = add_part_numbers(diagram)
    print("total parts:", total)


if __name__ == '__main__':
    main()