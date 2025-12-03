def day_one_main():
    input = get_input(file_path = 'inputs/day_one_input.txt')
    print(decipher_lock(combination = input))

def decipher_lock(combination: list[str]) -> int:
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

def get_input(file_path: str) -> list[str]:
     with open(file_path) as input_file:
          return input_file.readlines()