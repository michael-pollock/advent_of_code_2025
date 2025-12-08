from unittest import TestCase
import os
from advent_of_code.day.day_two import get_repeating_id_halfs, get_repeating_id_halfs_by_range, \
    get_repeating_id_sections, get_repeating_id_sections_by_range, id_halfs_are_unique, id_sections_are_unique
from advent_of_code.helper_files.io_operations import get_csv_input


class DayTwoTests(TestCase):

    def test_id_halfs_are_unique(self):
        self.assertTrue(id_halfs_are_unique(21))
        self.assertFalse(id_halfs_are_unique(22))
        self.assertTrue(id_halfs_are_unique(121))
        self.assertFalse(id_halfs_are_unique(2121))
        self.assertFalse(id_halfs_are_unique(21032103))
        self.assertTrue(id_halfs_are_unique(1234567123456))

    def test_get_repeating_id_halfs_by_range(self):
        self.assertListEqual([11, 22], get_repeating_id_halfs_by_range(start=11, end=22))

    def test_get_repeating_id_halfs_11_through_1010(self):
        input_data = ['11-1010']
        invalid_ids = get_repeating_id_halfs(input_data)
        expected_invalid_ids = [
            11, 22, 33, 44, 55, 66, 77, 88, 99, 1010
        ]
        self.assertEqual(expected_invalid_ids, invalid_ids)

    def test_get_repeating_id_halfs(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_two_test_input.csv')
        input_data = get_csv_input(file_path)
        invalid_ids = get_repeating_id_halfs(input_data)
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

    def test_id_sections_are_unique(self):
        self.assertTrue(id_sections_are_unique(21))
        self.assertFalse(id_sections_are_unique(22))
        self.assertTrue(id_sections_are_unique(121))
        self.assertFalse(id_sections_are_unique(2121))
        self.assertFalse(id_sections_are_unique(21032103))
        self.assertTrue(id_sections_are_unique(1234567123456))
        self.assertTrue(id_sections_are_unique(110))
        self.assertTrue(id_sections_are_unique(112))
        self.assertTrue(id_sections_are_unique(1234567123456))

    def test_get_repeating_id_sections_by_range(self):
        self.assertListEqual([11, 22], get_repeating_id_sections_by_range(start=11, end=22))

    def test_get_repeating_id_sections_11_through_1010(self):
        input_data = ['11-1010']
        invalid_ids = get_repeating_id_sections(input_data)
        expected_invalid_ids = [
            11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999, 1010
        ]
        self.assertEqual(expected_invalid_ids, invalid_ids)

    def test_get_repeating_id_sections(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_two_test_input.csv')
        input_data = get_csv_input(file_path)
        invalid_ids = get_repeating_id_sections(input_data)
        expected_invalid_ids = [
            11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656, 824824824, 2121212121
        ]
        self.assertEqual(expected_invalid_ids, invalid_ids)

    def test_get_repeating_id_sections_sum_is_correct(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_helpers')
        file_path = os.path.join(dir_path, 'day_two_test_input.csv')
        input_data = get_csv_input(file_path)
        invalid_ids = get_repeating_id_sections(input_data)
        self.assertEqual(4174379265, sum(invalid_ids))

