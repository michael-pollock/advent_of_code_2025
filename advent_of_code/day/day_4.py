from advent_of_code.helper_files.io_operations import get_input


def day_4_main():
    print(f'day four: uh oh')
    grid = get_input('inputs/day_4_input.txt')
    num_accessible_rolls = get_num_accessible_rolls(grid)
    print(f'Day 4 part 1: {num_accessible_rolls}')
    num_removable_rolls = get_num_removable_rolls(grid)
    print(f'Day 4 part 2: {num_removable_rolls}')

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
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            continue
        if grid[row][col] == '@':
            neighboring_rolls += 1
    return neighboring_rolls

def get_coordinates_of_neighboring_rolls(row_index: int, col_index: int, grid: list[str]) -> list[list[int]]:
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
    neighboring_roll_coordinates = []
    neighboring_rolls = 0
    for row, col in surrounding_positions:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]): continue
        if grid[row][col] == '@':
            neighboring_rolls += 1
            neighboring_roll_coordinates.append([row, col])
    return neighboring_roll_coordinates

def get_num_accessible_rolls(grid: list[str]) -> int:
    num_accessible_rolls = 0
    
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] != '@':
                continue
            num_neighboring_rolls = get_num_of_neighboring_rolls(row_index, col_index, grid)
            if num_neighboring_rolls < 4:
                num_accessible_rolls += 1
    return num_accessible_rolls

def get_num_removable_rolls_incorrectly_and_complicatedly(grid: list[str]) -> int:
    # 11433 was too high for main
    # this one getting false removals somehow. 
    num_removed_rolls = 0
    row_index = 0
    while row_index < len(grid):
        print(f'checking row {row_index}')
        move_row_back = False
        col_index = 0
        while col_index < len(grid[row_index]):
            move_col_back = False
            if grid[row_index][col_index] != '@':
                col_index += 1
                continue
            neighboring_roll_coords = get_coordinates_of_neighboring_rolls(row_index, col_index, grid)
            if len(neighboring_roll_coords) < 4:
                grid[row_index] = f'{grid[row_index][:col_index]}X{grid[row_index][col_index+1:]}'
                num_removed_rolls += 1                
                for coord_row, coord_col in neighboring_roll_coords:
                    if coord_row < row_index:
                        move_row_back = True
                        break
                    if coord_col < col_index:
                        move_col_back = True
                        break
            if move_row_back: row_index -= 1
            if move_col_back: col_index -= 1 
            elif not move_row_back: col_index += 1
            
        row_index += 1
    return num_removed_rolls

def get_num_removable_rolls(grid: list[str]) -> int:
    # main comes out to 9083
    total_removed_rolls = 0
    rolls_removed_in_pass = 0
    iteration = 0
    while rolls_removed_in_pass > 0 or iteration == 0:
        rolls_removed_in_pass = 0
        iteration += 1
        if iteration > 1000000:
            print(f'you should optimize something with the forklifts')
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                # print(f'[{row_index}][{col_index}]')
                if grid[row_index][col_index] != '@':
                    col_index += 1
                    continue
                neighboring_rolls = get_num_of_neighboring_rolls(row_index, col_index, grid)
                if neighboring_rolls < 4:
                    grid[row_index] = f'{grid[row_index][:col_index]}X{grid[row_index][col_index+1:]}'
                    rolls_removed_in_pass += 1
        # print(f'removed {rolls_removed_in_pass} this pass. Current total: {total_removed_rolls}')
        total_removed_rolls += rolls_removed_in_pass
            
    return total_removed_rolls