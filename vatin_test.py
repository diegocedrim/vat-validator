import unittest

from vatin import Vatin
from collections import namedtuple


class TestVatin(unittest.TestCase):

    def test_init(self):
        TestCase = namedtuple('TestCase', 'vatin want_valid want_code want_number')
        tests = [
            TestCase('AAA2898738973', True, 'AA', 'A2898738973'),
            TestCase('CZ28987373', True, 'CZ', '28987373'),
            TestCase('SE556900620701', True, 'SE', '556900620701'),
            TestCase('AA.+', True, 'AA', '.+'),
            TestCase('BR123', True, 'BR', '123'),
            TestCase('BR1', False, None, None),
            TestCase('AAA28987389732342423', False, None, None),
            TestCase(None, False, None, None),
            TestCase('', False, None, None),
            TestCase(123, False, None, None),
        ]
        for test in tests:
            vatin = Vatin(test.vatin)
            self.assertEqual(vatin.valid_format, test.want_valid)
            self.assertEqual(vatin.country, test.want_code)
            self.assertEqual(vatin.number, test.want_number)
