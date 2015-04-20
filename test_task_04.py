#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04."""


# Import Python libs
import unittest


# Import user libs
import chessmaster


class Task04TestCase(unittest.TestCase):
    """Task 04 tests"""

    def test_king_movement(self):
        """Tests that kings may freely move any direction, 1 square"""
        king = chessmaster.King('d4')
        self.assertTrue(king.move('d5'), 'd4 => d5')
        self.assertTrue(king.move('d4'), 'd5 => d4')
        self.assertTrue(king.move('e4'), 'd4 => e4')
        self.assertTrue(king.move('d4'), 'e4 => d4')
        self.assertTrue(king.move('e5'), 'd4 => e5')
        self.assertTrue(king.move('d4'), 'e5 => d4')
        self.assertTrue(king.move('c5'), 'd4 => c5')
        self.assertTrue(king.move('d4'), 'e4 => d4')
        self.assertFalse(king.move('d6'), 'd4 => d6')


if __name__ == '__main__':
    unittest.main()
