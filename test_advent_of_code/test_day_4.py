from unittest import TestCase
from advent_of_code.day.day_4 import init_input
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