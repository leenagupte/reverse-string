import unittest
from hamcrest import assert_that, equal_to
from reverse_string import reverse_string, reverse_words, reverse_word_order


class TestReverseString(unittest.TestCase):
    def test_get_last_character(self):
        str = "abcdefg"

        assert_that(str[-1], equal_to("g"))

    def test_remove_last_character_from_string(self):
        str = "abcdefg"

        assert_that(str[:-1], equal_to("abcdef"))

    def test_get_reverse_string(self):
        str = "abcdefg"

        assert_that(reverse_string(str), equal_to("gfedcba"))

    def test_reverse_each_word_in_string(self):

        str = "star wars"

        assert_that(reverse_words(str), equal_to("rats sraw"))

    def test_reverse_word_order(self):
        str = "star wars"

        assert_that(reverse_word_order(str), equal_to("wars star"))
