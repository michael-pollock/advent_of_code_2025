from advent_of_code.helper_files.io_operations import get_input


def day_4_main():
    print(f'day four: uh oh')
    grid = init_input('inputs/day_4_input.txt')
    num_accessible_rolls = get_num_accessible_rolls(grid)
    print(f'Day 4 part 1: {num_accessible_rolls}')

def init_input(file_path) -> list[str]:
    grid = get_input(file_path = file_path)
    return grid

def get_num_of_neighboring_rolls(row_index: int, col_index: int, grid: list[str]):
    surrounding_positions = [
        [row_index-1, col_index-1],
        [row_index-1, col_index],
        [row_index-1, col_index+1],
        [row_index, col_index-1],
        [row_index, col_index+1],
        [row_index+1, col_index-1],
        [row_index+1, col_index],
        [row_index+1, col_index+1]
    ]
    neighboring_rolls = 0
    for row, col in surrounding_positions:
        # print(f'checking [{row}][{col}]')
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            # print(f'skipping index [{row}][{col}]')
            continue
        if grid[row][col] == '@':
            neighboring_rolls += 1
    return neighboring_rolls

def get_num_and_remove_neighboring_rolls(row_index: int, col_index: int, grid: list[str]):
    info_dict = {
        "num_accessible_rolls": 0,
        "neighboring_roll_coordinates": []
    }
    surrounding_positions = [
        [row_index-1, col_index-1],
        [row_index-1, col_index],
        [row_index-1, col_index+1],
        [row_index, col_index-1],
        [row_index, col_index+1],
        [row_index+1, col_index-1],
        [row_index+1, col_index],
        [row_index+1, col_index+1]
    ]
    neighboring_rolls = 0
    for row, col in surrounding_positions:
        # print(f'checking [{row}][{col}]')
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            # print(f'skipping index [{row}][{col}]')
            continue
        if grid[row][col] == '@':
            neighboring_rolls += 1
            info_dict['neighboring_roll_coordinates'].append([row, col])
            print(f'grid[0]: {grid[0]}')
            grid[row] = f'{grid[row][:col]}X{grid[row][col+1:]}'
            print(f'grid[0]: {grid[0]}')
    return neighboring_rolls

def get_num_accessible_rolls(grid: list[str]) -> int:
    num_accessible_rolls = 0
    
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] != '@':
                continue
            num_neighboring_rolls = get_num_of_neighboring_rolls(row_index, col_index, grid)
            # print(f'[{row_index}][{col_index}]: neighboring rolls: {num_neighboring_rolls}')
            if num_neighboring_rolls < 4:
                num_accessible_rolls += 1
    return num_accessible_rolls

def get_num_removable_rows(grid: list[str]) -> int:
    num_accessible_rolls = 0
    
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] != '@':
                continue
            num_neighboring_rolls = get_num_of_neighboring_rolls(row_index, col_index, grid)
            # print(f'[{row_index}][{col_index}]: neighboring rolls: {num_neighboring_rolls}')
            if num_neighboring_rolls < 4:
                num_accessible_rolls += 1
    return num_accessible_rolls
