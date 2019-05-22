#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from paranthesis_balanced import is_paranthesis_balanced


class TestParanthesisBalances(unittest.TestCase):
    def test_empty(self):
        s = ''
        self.assertTrue(is_paranthesis_balanced(s))

    def test_correct(self):
        s = '({[()]}{<>})'
        self.assertTrue(is_paranthesis_balanced(s))

    def test_close_without_open(self):
        s = '()]'
        self.assertFalse(is_paranthesis_balanced(s))

    def test_open_without_close(self):
        s = '([)'
        self.assertFalse(is_paranthesis_balanced(s))
        s = '()['
        self.assertFalse(is_paranthesis_balanced(s))

    def test_intersection(self):
        s = '([)]'
        self.assertFalse(is_paranthesis_balanced(s))


if __name__ == '__main__':
    unittest.main()
