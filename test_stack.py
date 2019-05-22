#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from stack import Stack, StackOverflowError, StackIsEmptyError


class TestStack(unittest.TestCase):
    def test_push_pop(self):
        a = [1, 2, 5, 7]
        s = Stack(4)
        for v in a:
            s.push(v)
        b = [s.pop() for i in range(len(a))]
        self.assertEqual(a[::-1], b)

    def test_overflow_error(self):
        s = Stack(1)
        s.push(1)
        self.assertRaises(StackOverflowError, s.push, 2)

    def test_empty_error(self):
        s = Stack(1)
        self.assertRaises(StackIsEmptyError, s.pop)

    def test_len(self):
        a = [1, 2, 5, 7]
        s = Stack(10)
        self.assertEqual(len(s), 0)
        for v in a:
            s.push(v)
        self.assertEqual(len(s), 4)


if __name__ == '__main__':
    unittest.main()
