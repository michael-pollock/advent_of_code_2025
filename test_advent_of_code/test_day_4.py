from unittest import TestCase
from advent_of_code.day.day_4 import get_num_accessible_rolls, get_num_of_neighboring_rolls, init_input
import os


class Day4Tests(TestCase):

    def test_init_input(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_4_test_input.txt')
        grid = init_input(file_path = file_path)
        row_len = len(grid)
        col_len = len(grid[0])

        self.assertEqual(10, row_len)
        self.assertEqual(10, col_len)
        self.assertEqual('.', grid[0][0])
        self.assertEqual('.', grid[0][1])
        self.assertEqual('@', grid[1][0])
        self.assertEqual('@', grid[1][1])

        print(f'grid[0]: {grid[0]}')
        grid[0] = f'{grid[0][:1]}X{grid[0][2:]}'
        print(f'grid[0]: {grid[0]}')
        self.assertEqual('.', grid[0][0])
        self.assertEqual('X', grid[0][1])
        self.assertEqual('@', grid[0][2])
        self.assertEqual('@', grid[0][3])


    def test_get_num_of_surrounding_rolls(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_4_test_input.txt')
        grid = init_input(file_path = file_path)
        self.assertEqual(2, get_num_of_neighboring_rolls(0, 0, grid))
        self.assertEqual(4, get_num_of_neighboring_rolls(0, 1, grid))
        self.assertEqual(3, get_num_of_neighboring_rolls(0, 2, grid))
        self.assertEqual(3, get_num_of_neighboring_rolls(1, 0, grid))
        self.assertEqual(4, get_num_of_neighboring_rolls(2, 0, grid))
        self.assertEqual(7, get_num_of_neighboring_rolls(3, 3, grid))

    def test_get_num_valid_rolls(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_4_test_input.txt')
        grid = init_input(file_path = file_path)
        self.assertEqual(13, get_num_accessible_rolls(grid))