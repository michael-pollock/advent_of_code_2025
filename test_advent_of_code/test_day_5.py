from unittest import TestCase
import os
from advent_of_code.day.day_5 import get_fresh_id_set_and_ingredient_id_list, get_num_fresh_ingredients
from advent_of_code.helper_files.io_operations import get_input

class Day5Tests(TestCase):
    
    def test_get_fresh_id_set_and_ingredient_id_list_returns_set_and_lists(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_5_test_input.txt')
        input = get_input(file_path = file_path)
        fresh_ids, ingredients = get_fresh_id_set_and_ingredient_id_list(input)
        expected_fresh_ids = {3,4,5,10,11,12,13,14,15,16,17,18,19,20}
        expected_ingredients = [1,5,8,11,17,32]
        self.assertSetEqual(expected_fresh_ids, fresh_ids)
        self.assertListEqual(expected_ingredients, ingredients)

    def test_get_num_fresh_ingredients(self):
        fresh_ids = {3,4,5,10,11,12,13,14,15,16,17,18,19,20}
        ingredients = [1,5,8,11,17,32]
        num_fresh_ingredients = get_num_fresh_ingredients(fresh_ids, ingredients)
        self.assertEqual(3, num_fresh_ingredients)