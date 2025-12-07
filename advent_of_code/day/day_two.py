from advent_of_code.helper_files.io_operations import get_input


def day_two_main(): 
    input = get_input(file_path = 'inputs/day_two_input.csv')
    print(f'input: {input}')

def get_invalid_ids(data_ranges):
    invalid_ids = []
    print(f'data_ranges: {data_ranges}')
    for range in data_ranges:
        range_bounds = range.split('-')
        if len(range_bounds) != 2:
            print(f'len of range bounds: {len(range_bounds)}')
            continue
        invalid_ids.append(get_invalid_ids_by_range(start=range_bounds[0], end=range_bounds[1]))

    return invalid_ids

def get_invalid_ids_by_range(start: str, end: str):
    print(f'getting invalid ids for range {start} - {end}')
    if int(start) > int(end):
        temp_start = start
        start = end
        end = temp_start
    invalid_ids = []
    if len(start) == len(end) and len(start) % 2 != 0:
        print(f'return []')
        return []
    if len(start) == len(end) and len(start) % 2 == 0:
        invalid_ids = list(int(id) for id in range(int(start), int(end) + 1) if not id_is_valid(str(id)))
        print(f'invalid ids: {invalid_ids}')
        return invalid_ids
    invalid_ids = []
    id = start

    while int(id) <= int(end):
        print(f'current id: {id}')
        if len(id) % 2 != 0:
            new_id = '1' + '0'*len(id)
            print(f'jumping from {id} to {new_id}')
            id = new_id
            continue
        if not id_is_valid(id): invalid_ids.append(id)
        id = str(int(id) + 1)
    print(f'returning {invalid_ids}')
    return invalid_ids

def id_is_valid(id: str):
    print(f'checking id: {id}')
    if len(id)%2 != 0:
        return True
    center_index: int = (len(id) // 2)
    left = id[:center_index]
    right = id[center_index:]
    return left != right 
