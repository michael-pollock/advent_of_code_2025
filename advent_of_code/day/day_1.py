from advent_of_code.helper_files.io_operations import get_input


def day_1_main():
    input = get_input(file_path = 'inputs/day_1_input.txt')
    print(f'Day one part one: {decipher_lock_pt_1(combination = input)}')
    print(f'Day one part two: {decipher_lock_pt_2(combination = input)}')
    

def decipher_lock_pt_1(combination: list[str]) -> int:
    combo: int = 0
    position: int = 50
    num_positions: int = 100
    rotation: str
    for rotation in combination:
        direction: str = rotation[0]
        distance: int = int(rotation[1:])
        if direction == 'L':
            position = (position - distance) % num_positions
        else:
            position = (position + distance) % num_positions

        if position == 0:
            combo += 1
    return combo

def decipher_lock_pt_2(combination: list[str]) -> int:
    combo: int = 0
    position: int = 50
    num_positions: int = 100
    rotation: str
    for rotation in combination:
        direction: str = rotation[0]
        distance: int = int(rotation[1:])
        num_full_rotations = distance // num_positions
        distance = distance % num_positions
        combo += num_full_rotations
        position_crosses_zero = False
        if direction == 'L':
            position = 100 if position == 0 else position
            position = (position - distance)
            position_crosses_zero = position <= 0
            position = position % num_positions
        else:
            position = (position + distance)
            position_crosses_zero = position >= num_positions
            position = position % num_positions    
        if position_crosses_zero:
            combo += 1        
    return combo