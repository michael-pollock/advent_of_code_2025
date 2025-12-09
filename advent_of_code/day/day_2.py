from advent_of_code.helper_files.io_operations import get_csv_input


def day_2_main(): 
    input = get_csv_input(file_path = 'inputs/day_2_input.csv')
    invalid_ids = get_repeating_id_halfs(input)
    print(f'Day two part one: sum of invalid ids: {sum(invalid_ids)}')
    invalid_ids = get_repeating_id_sections(input)
    print(f'Day two part two: sum of invalid ids: {sum(invalid_ids)}')

def get_repeating_id_halfs(data_ranges: list[str]):
    invalid_ids = []
    for range in data_ranges:
        range_bounds = range.split('-')
        if len(range_bounds) != 2:
            continue
        invalid_ids.extend(get_repeating_id_halfs_by_range(start=int(range_bounds[0]), end=int(range_bounds[1])))

    return invalid_ids

def get_repeating_id_halfs_by_range(start: int, end: int):
    if start > end:
        temp_start = start
        start = end
        end = temp_start
    invalid_ids = []
    start_str = str(start)
    end_str = str(end)
    if len(start_str) == len(end_str) and len(start_str) % 2 != 0:
        return []
    if len(start_str) == len(end_str) and len(start_str) % 2 == 0:
        invalid_ids = list(int(id) for id in range(start, end + 1) if not id_halfs_are_unique(id))
        return invalid_ids
    invalid_ids = []
    id:int = start

    while id <= end:
        id_str = str(id)
        if len(id_str) % 2 != 0:
            id = int('1' + '0'*len(id_str))
            continue
        if not id_halfs_are_unique(id): invalid_ids.append(id)
        id = id + 1
    return invalid_ids

def id_halfs_are_unique(id: int):
    id_str = str(id)
    if len(id_str)%2 != 0:
        return True
    center_index: int = (len(id_str) // 2)
    left = id_str[:center_index]
    right = id_str[center_index:]
    return left != right 

def id_sections_are_unique(id: int):
    id_str = str(id)
    section_lengths = []
    for i in range(len(id_str) // 2 + 1):
        if i < 1: continue
        if len(id_str) % i != 0: continue
        section_lengths.append(i)
    section_lengths.sort(reverse=True)
    for length in section_lengths:
        section_to_match = id_str[:length]
        has_unique_section = False
        for i in range(length, len(id_str), length):
            if section_to_match != id_str[i:i+length]:
                has_unique_section = True
                break
        if not has_unique_section: 
            return False
    return True

def get_repeating_id_sections_by_range(start: int, end: int):
    if start > end:
        temp_start = start
        start = end
        end = temp_start
    invalid_ids = []
    id: int = start
    while id <= end:
        if not id_sections_are_unique(id): invalid_ids.append(id)
        id += 1
    return invalid_ids

def get_repeating_id_sections(data_ranges: list[str]):
    invalid_ids = []
    for range in data_ranges:
        range_bounds = range.split('-')
        if len(range_bounds) != 2:
            continue
        invalid_ids.extend(get_repeating_id_sections_by_range(start=int(range_bounds[0]), end=int(range_bounds[1])))

    return invalid_ids
