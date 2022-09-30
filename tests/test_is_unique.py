'''Test'''
import unittest

from unique_characters import is_unique


class TestIsUnique(unittest.TestCase):
    '''Test if the characters in one strings are unique'''

    def test_is_unique(self):
        '''Check if the characters are unique'''
        assert is_unique('miau')

    def test_is_not_unique(self):
        '''Check if the characters are not unique'''
        assert not is_unique('aleoia')


if __name__ == '__main__':
    unittest.main()
