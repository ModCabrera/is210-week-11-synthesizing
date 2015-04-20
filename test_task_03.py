#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03."""


# Import Python libs
import unittest


# Import user libs
import chessmaster


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    def test_bishop_movement(self):
        """Tests that bishops may freely move along diagonals"""
        bishop = chessmaster.Bishop('d4')
        self.assertTrue(bishop.move('f6'), 'd4 => f6')
        self.assertTrue(bishop.move('d4'), 'f6 => d4')
        self.assertTrue(bishop.move('f2'), 'd4 => f2')
        self.assertTrue(bishop.move('d4'), 'f2 => d4')
        self.assertFalse(bishop.move('d5'), 'd4 => d5')


if __name__ == '__main__':
    unittest.main()
