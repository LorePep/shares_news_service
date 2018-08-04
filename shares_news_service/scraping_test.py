import unittest

import mock
from bs4 import BeautifulSoup

from scraping import (
    scrape_interesting_news,
    _get_share_name,
    _get_words_from_text,
    _is_news_interesting,
)


FIXTURE_HTML = """
<html>
    <head>
        <title>Some fixture HTML</title>
    </head>
    <body>
        <table style="width:100%">
            <tr>
                <td class="m" colspan="2">A news results</td>
                <td class="mb" align="right" valign="top">NAME ksjadlk</td> 
            </tr>
        </table>
    </body>
</html>
"""


def _return_fixture_scraped(url):
    return BeautifulSoup(FIXTURE_HTML, "html.parser")


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
    
    @mock.patch('scraping._get_soup_from_url', side_effect=_return_fixture_scraped)
    def test_scrape_interesting_news(self, mock_get_soup_from_url):
        actual = scrape_interesting_news("one_url")
        expected = {
            "NAME": "A news results"
        }
        self.assertDictEqual(actual, expected)
