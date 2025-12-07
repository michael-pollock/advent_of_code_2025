from unittest import TestCase
import os
from advent_of_code.day.day_two import get_invalid_ids, get_invalid_ids_by_range, id_is_valid
from advent_of_code.helper_files.io_operations import get_csv_input


class DayTwoTests(TestCase):

    def test_id_is_valid(self):
        self.assertTrue(id_is_valid(21))
        self.assertFalse(id_is_valid(22))
        self.assertTrue(id_is_valid(121))
        self.assertFalse(id_is_valid(2121))
        self.assertFalse(id_is_valid(21032103))
        self.assertTrue(id_is_valid(1234567123456))

    def test_get_invalids_by_range(self):
        self.assertListEqual([11, 22], get_invalid_ids_by_range(start=11, end=22))

    def test_get_invalid_ids_11_through_1010(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_two_test_input.csv')
        input_data = ['11-1010']
        invalid_ids = get_invalid_ids(input_data)
        expected_invalid_ids = [
            11, 22, 33, 44, 55, 66, 77, 88, 99, 1010
        ]
        self.assertEqual(expected_invalid_ids, invalid_ids)

    def test_get_invalid_ids(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_two_test_input.csv')
        input_data = get_csv_input(file_path)
        invalid_ids = get_invalid_ids(input_data)
        expected_invalid_ids = [
            11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859
        ]
        self.assertEqual(expected_invalid_ids, invalid_ids)

    def test_get_sum_of_invalid_ids(self):
        invalid_ids = [
            11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859
        ]
        id_sum = sum(invalid_ids)
        self.assertEqual(1227775554, id_sum)