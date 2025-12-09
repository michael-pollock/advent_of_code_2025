from unittest import TestCase
import os
from advent_of_code.day.day_1 import decipher_lock_pt_1, decipher_lock_pt_2


class Day1Tests(TestCase):

    def test_decipher_lock_pt_1(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_1_test_input.txt')
        with open(file_path) as f:
            input_data = f.readlines()
        combo = decipher_lock_pt_1(input_data)
        self.assertEqual(3, combo)

    def test_decipher_lock_pt_2(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_1_test_input.txt')
        with open(file_path) as f:
            input_data = f.readlines()
        combo = decipher_lock_pt_2(input_data)
        self.assertEqual(6, combo)

    def test_decipher_lock_pt_2_multiple_turns(self):
        input_data = ['R1000']
        combo = decipher_lock_pt_2(input_data)
        self.assertEqual(10, combo)