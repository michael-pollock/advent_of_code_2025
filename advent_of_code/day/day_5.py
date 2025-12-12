from typing import Tuple
from advent_of_code.helper_files.io_operations import get_input


def day_5_main():
    input = get_input('inputs/day_5_input.txt')
    fresh_id_ranges, ingredients = get_fresh_id_set_and_ingredient_id_list(input)
    num_fresh_ingredients = get_num_fresh_ingredients(fresh_id_ranges, ingredients)
    num_fresh_ids = get_num_fresh_ids(fresh_id_ranges)
    print(f'Day 5 part 1: {num_fresh_ingredients}')
    print(f'Day 5 part 2: {num_fresh_ids}')

def get_fresh_id_set_and_ingredient_id_list(input) -> Tuple[list[list[int]], list[int]]:
    unparsed_ranges = []
    ingredients = []
    setting_ranges = True
    setting_ingredients = False
    for line in input:
        if line == '': 
            setting_ranges = False
            setting_ingredients = True
            continue
        if setting_ranges: unparsed_ranges.append(line)
        if setting_ingredients: ingredients.append(int(line))
    fresh_id_ranges = []
    for unparsed_range in unparsed_ranges:
        fresh_id_ranges = update_ranges(fresh_id_ranges, unparsed_range)
    return fresh_id_ranges, ingredients

def update_ranges(existing_ranges: list[list[int]], new_range: str) -> list[list[int]]:
    range_parts = new_range.split('-')
    new_start = int(range_parts[0])
    new_end = int(range_parts[1])
    if not existing_ranges: return [[new_start, new_end]]

    new_ranges = []
    i = 0
    placed = False
    while i < len(existing_ranges):
        update_previous_range = False
        existing_start = existing_ranges[i][0]
        existing_end = existing_ranges[i][1]
        # print(f'comparing new {new_start}-{new_end} against existing {existing_start}-{existing_end}')
        if new_start <= existing_start and new_end >= existing_start and new_end <= existing_end:
            existing_ranges[i][0] = new_start
            new_end = existing_end
            placed = True
            if i > 0 and existing_ranges[i-1][0] == new_start:
                existing_ranges[i-1][1] = new_end
                existing_ranges.pop(i)
                continue
            # print(f'updated existing start: {existing_start} | {existing_ranges[i][0]}')
        if new_end >= existing_end and new_start <= existing_end and new_start >= existing_start:
            existing_ranges[i][1] = new_end
            new_start = existing_start
            placed = True
            # print(f'updated existing end: {existing_end} | {existing_ranges[i][1]}')
        if new_start <= existing_start and new_end >= existing_end:
            existing_ranges[i][0] = new_start
            existing_ranges[i][1] = new_end
            placed = True
            # print(f'updated existing start: {existing_start} | {existing_ranges[i][0]}')
            # print(f'updated existing end: {existing_end} | {existing_ranges[i][1]}')
        if new_start >= existing_start and new_end <= existing_end:
            placed = True
        i += 1

    if not placed: 
        # print(f'not placed: {new_start} - {new_end}')
        new_ranges.append([new_start, new_end])
        # print(f'new ranges: {new_ranges}')
    existing_ranges.extend(new_ranges)
    existing_ranges = sorted(existing_ranges, key=lambda item: item[0])
    # print(f'updated existing ranges: {existing_ranges}')
    return existing_ranges
# def compress_ranges(ranges: list[str]):
#     parsed_ranges 

def get_num_fresh_ingredients(fresh_ids: list[list[int]], ingredient_ids: list[int]):
    fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        for fresh_start, fresh_end in fresh_ids:
            if fresh_start <= ingredient_id and ingredient_id <= fresh_end:
                fresh_ingredients += 1
                break
    return fresh_ingredients

def get_num_fresh_ids(fresh_id_ranges: list[list[int]]) -> int:
    num_ids = 0
    for start, end in fresh_id_ranges:
        num_ids += (end-start) + 1
    return num_ids
    