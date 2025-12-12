from unittest import TestCase
import os
from advent_of_code.day.day_5 import get_fresh_id_set_and_ingredient_id_list, get_num_fresh_ids, get_num_fresh_ingredients, update_ranges
from advent_of_code.helper_files.io_operations import get_input

class Day5Tests(TestCase):
    
    def test_get_fresh_id_set_and_ingredient_id_list_returns_set_and_lists(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_5_test_input.txt')
        input = get_input(file_path = file_path)
        fresh_ids, ingredients = get_fresh_id_set_and_ingredient_id_list(input)
        expected_fresh_ids = [[3,5],[10,20]]
        expected_ingredients = [1,5,8,11,17,32]
        self.assertListEqual(expected_fresh_ids, fresh_ids)
        self.assertListEqual(expected_ingredients, ingredients)

    def test_get_num_fresh_ingredients_returns_expected_num(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_5_test_input.txt')
        input = get_input(file_path = file_path)
        fresh_ids, ingredients = get_fresh_id_set_and_ingredient_id_list(input)
        num_fresh_ingredients = get_num_fresh_ingredients(fresh_ids, ingredients)
        self.assertEqual(3, num_fresh_ingredients)

    def test_get_num_fresh_ingredients(self):
        fresh_ids = [[3,5],[10,20]]
        ingredients = [1,5,8,11,17,32]
        num_fresh_ingredients = get_num_fresh_ingredients(fresh_ids, ingredients)
        self.assertEqual(3, num_fresh_ingredients)

    def test_update_ranges(self):
        ranges = [
            '10-20',
            '0-3',
            '27-30',
            '9-21',
            '6-13',
            '19-25',
            '13-17'
        ]
        created_ranges = []
        for id_range in ranges:
            created_ranges = update_ranges(created_ranges, id_range)

        expected_ranges = [
            [0, 3], 
            [6, 25],
            [27, 30]
        ]
        print(f'created id ranges:')
        for id_range in created_ranges: 
            print(id_range)
        self.assertListEqual(expected_ranges, created_ranges)

    def test_get_num_fresh_ids(self):
        id_ranges = [[3,5],[10,20]]
        num_fresh_ids = get_num_fresh_ids(id_ranges)
        self.assertEqual(14, num_fresh_ids)