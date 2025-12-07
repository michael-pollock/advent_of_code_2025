from advent_of_code.helper_files.io_operations import get_input


def day_two_main(): 
    input = get_input(file_path = 'inputs/day_two_input.csv')
    print(f'input: {input}')

def get_invalid_ids(data_ranges: list[str]):
    invalid_ids = []
    print(f'data_ranges: {data_ranges}')
    for range in data_ranges:
        range_bounds = range.split('-')
        if len(range_bounds) != 2:
            continue
        invalid_ids.extend(get_invalid_ids_by_range(start=int(range_bounds[0]), end=int(range_bounds[1])))

    return invalid_ids

def get_invalid_ids_by_range(start: int, end: int):
    print(f'getting invalid ids for range {start} - {end}')
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
        invalid_ids = list(int(id) for id in range(start, end + 1) if not id_is_valid(id))
        print(f'invalid ids: {invalid_ids}')
        return invalid_ids
    invalid_ids = []
    id:int = start

    while id <= end:
        id_str = str(id)
        if len(id_str) % 2 != 0:
            new_id_str = '1' + '0'*len(id_str)
            print(f'jumping from {id_str} to {new_id_str}')
            id = int(new_id_str)
            continue
        if not id_is_valid(id): invalid_ids.append(id)
        id = id + 1
    print(f'returning {invalid_ids}')
    return invalid_ids

def id_is_valid(id: int):
    id_str = str(id)
    if len(id_str)%2 != 0:
        return True
    center_index: int = (len(id_str) // 2)
    left = id_str[:center_index]
    right = id_str[center_index:]
    return left != right 
