from advent_of_code.helper_files.io_operations import get_input


def day_4_main():
    print(f'day four: uh oh')
    input = init_input('inputs/day_4_input.txt')

def init_input(file_path):
    input = get_input(file_path = file_path)
    return input

def get_num_of_surrounding_rolls(row_index: int, col_index: int, grid: list[list[str]]):
    print(f'current location: [{row_index}][{col_index}]: {grid[row_index][col_index]}')
    surrounding_indicies = []
    row_check = row_index - 1
    col_check = col_index - 1

