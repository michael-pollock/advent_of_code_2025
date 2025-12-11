from typing import Tuple
from advent_of_code.helper_files.io_operations import get_input


def day_5_main():
    input = get_input('inputs/day_5_input.txt')
    fresh_ids, ingredients = get_fresh_id_set_and_ingredient_id_list(input)
    num_fresh_ingredients = get_num_fresh_ingredients(fresh_ids, ingredients)
    print(f'uh oh')

def get_fresh_id_set_and_ingredient_id_list(input) -> Tuple[set[int], list[int]]:
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
        if setting_ingredients: ingredients.append(line)
    fresh_ingredient_ids = set()
    for unparsed_range in unparsed_ranges:
        range_parts = unparsed_range.split('-')
        begin = int(range_parts[0])
        end = int(range_parts[1]) + 1
        print(f'range: {unparsed_range}, begin: "{type(begin)}", end: "{type(end)}"')
        for id in range(begin, end):
            fresh_ingredient_ids.add(id)
    return fresh_ingredient_ids, ingredients

def get_num_fresh_ingredients(fresh_ids: set[int], ingredient_ids: list[int]):
    fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        if ingredient_id in fresh_ids: fresh_ingredients += 1
    return fresh_ingredients