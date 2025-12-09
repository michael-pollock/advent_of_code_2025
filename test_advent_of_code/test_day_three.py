from unittest import TestCase

from advent_of_code.day.day_three import get_highest_joltage, get_highest_joltage_and_ignore_all_safety_protocol

class DayThreeTests(TestCase):

    def test_get_highest_joltage(self):
        self.assertEqual(12, get_highest_joltage('12'))
        self.assertEqual(21, get_highest_joltage('21'))
        self.assertEqual(29, get_highest_joltage('219'))
        self.assertEqual(89, get_highest_joltage('1111189'))
        self.assertEqual(99, get_highest_joltage('192234569'))
        self.assertEqual(98, get_highest_joltage('911111118'))
        self.assertEqual(98, get_highest_joltage('987654321111111'))
        self.assertEqual(89, get_highest_joltage('811111111111119'))
        self.assertEqual(78, get_highest_joltage('234234234234278'))
        self.assertEqual(92, get_highest_joltage('818181911112111'))

    def test_get_highest_joltage_and_ignore_all_safety_protocol(self):
        self.assertEqual('811111191111', get_highest_joltage_and_ignore_all_safety_protocol('1234567811111191111'))
        self.assertEqual('434234234278', get_highest_joltage_and_ignore_all_safety_protocol('234234234234278'))
        self.assertEqual('999999999999', get_highest_joltage_and_ignore_all_safety_protocol('98989898989898989898989'))
        self.assertEqual('987654321111', get_highest_joltage_and_ignore_all_safety_protocol('987654321111111'))
        self.assertEqual('811111111119', get_highest_joltage_and_ignore_all_safety_protocol('811111111111119'))
        self.assertEqual('888911112111', get_highest_joltage_and_ignore_all_safety_protocol('818181911112111'))

    
