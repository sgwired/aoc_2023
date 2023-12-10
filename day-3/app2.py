import sys
sys.path.append("..")
from common.utils import read_lines_from_file

def is_gear_symbol(char):
    return char == '*'

def get_full_number(grid, row, col):
    left_bound = col
    while left_bound > 0 and grid[row][left_bound - 1].isdigit():
        left_bound -= 1

    right_bound = col
    while right_bound < len(grid[row]) - 1 and grid[row][right_bound + 1].isdigit():
        right_bound += 1

    return grid[row][left_bound:right_bound + 1], left_bound, right_bound

def find_part_numbers(diagram, row, col):
    """Get all all part numbers net to the current position."""
    part_numbers = []

    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            if row_offset == 0 and col_offset == 0:
                continue

            adjacent_row = row + row_offset
            adjacent_col = col + col_offset

            if 0 <= adjacent_row < len(diagram) and 0 <= adjacent_col < len(diagram[0]):
                if diagram[adjacent_row][adjacent_col].isdigit():
                    num, _, _ = get_full_number(diagram, adjacent_row, adjacent_col)
                    if num.isdigit():
                        part_numbers.append(int(num))
    print("part numbers: ", list(set(part_numbers)))
    return list(set(part_numbers))

def calculate_gear_ratios(diagram):
    total = 0
    visited_gears = set()

    for row in range(len(diagram)):
        print("visited gears: ", visited_gears)
        print("row:", row)
        for col in range(len(diagram[row])):
            print("col:", col)
            if is_gear_symbol(diagram[row][col]) and (row, col) not in visited_gears:
                part_numbers = find_part_numbers(diagram, row, col)
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total += gear_ratio
                    print(f"found gear at ({row}, {col}): part numbers {part_numbers}, gear ratio: {gear_ratio}")
                visited_gears.add((row, col))

    return total




def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'ex2.txt'
    diagram = read_lines_from_file(file_path)
    total = calculate_gear_ratios(diagram)
    print("total gear ratios:", total)


if __name__ == '__main__':
    main()