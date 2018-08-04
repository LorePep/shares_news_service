import unittest

from scraping import (
    _get_share_name,
    _get_words_from_text,
    _is_news_interesting,
)

class TestScraping(unittest.TestCase):

    def get_share_name_test(self):
        bad_name = "this is a bad name"
        with self.assertRaises(ValueError):
            _get_share_name(bad_name)

        empty_name = ""
        with self.assertRaises(ValueError):
            _get_share_name(empty_name)

        none_name = None
        with self.assertRaises(ValueError):
            _get_share_name(none_name)
        
        valid_name = "OXB asdweo"
        actual = _get_share_name(valid_name)
        self.assertEqual("OXB", actual)

    def is_news_interesting_test(self):
        test_cases = [
        {
            "name": "empty_text",
            "input": [],
            "expected": False
        },
        {
            "name": "none_text",
            "input": None,
            "expected": False
        },
        {
            "name": "no_keyword",
            "input": ["a", "b", "c"],
            "expected": False
        },
        {
            "name": "keyword_in_text",
            "input": ["result", "a", "b"],
            "expected": True
        }
    ]

        for tt in test_cases:
            actual = _is_news_interesting(tt["input"])
            self.assertEqual(tt["expected"], actual, msg="failed %s" % tt["name"])

    def get_words_from_text_test(self):
        test_cases = [
        {
            "name": "empty_text",
            "input": [],
            "expected": []
        },
        {
            "name": "none_text",
            "input": None,
            "expected": []
        },
        {
            "name": "valid_text",
            "input": "this is, some valid text",
            "expected": ["this", "is", "some", "valid", "text"]
        }
    ]

        for tt in test_cases:
            actual = _get_words_from_text(tt["input"])
            self.assertEqual(tt["expected"], actual, msg="failed %s" % tt["name"])
