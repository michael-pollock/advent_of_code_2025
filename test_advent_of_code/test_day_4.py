from unittest import TestCase
from advent_of_code.day.day_4 import get_coordinates_of_neighboring_rolls, get_num_accessible_rolls, get_num_of_neighboring_rolls, get_num_removable_rolls, init_input
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
        
        grid[0] = f'{grid[0][:1]}X{grid[0][2:]}'
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

    def test_removal_functions_on_mini_grid(self):
        mini_grid = [
            '@@@',
            '@.@'
        ]

        self.assertListEqual(
            [[0,1],[1,0]],
            get_coordinates_of_neighboring_rolls(0,0, mini_grid)
        )
        self.assertListEqual(
            [[0,0],[0,2],[1,0],[1,2]],
            get_coordinates_of_neighboring_rolls(0,1, mini_grid)
        )

        removable_rolls = get_num_removable_rolls(mini_grid)
        self.assertEqual(5, removable_rolls)

    def test_get_num_removable_rows(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_4_test_input.txt')
        grid = init_input(file_path = file_path)
        removable_rolls = get_num_removable_rolls(grid)
        self.assertEqual(43, removable_rolls)

    def test_get_num_removable_rows_for_main(self):
        dir_path = os.path.join(os.path.dirname(__file__), '..\\advent_of_code\\inputs')
        file_path = os.path.join(dir_path, 'day_4_input.txt')
        grid = init_input(file_path = file_path)
        removable_rolls = get_num_removable_rolls(grid)
        self.assertEqual(9083, removable_rolls)