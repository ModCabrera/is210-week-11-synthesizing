#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import unittest


# Import user libs
import chessmaster


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""

    def test_rook_movement(self):
        """Tests that rooks may freely move along 2 axes"""
        rook = chessmaster.Rook('d4')
        self.assertTrue(rook.move('d8'), 'd4 => d8')
        self.assertTrue(rook.move('d4'), 'd8 => d4')
        self.assertTrue(rook.move('a4'), 'd4 => a4')
        self.assertTrue(rook.move('d4'), 'a4 => d4')
        self.assertFalse(rook.move('e5'), 'd4 => e5')


if __name__ == '__main__':
    unittest.main()
