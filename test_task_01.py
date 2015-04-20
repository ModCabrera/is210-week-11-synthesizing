#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import chessmaster


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_chesspiece_prefix_attr(self):
        """Tests that the prefix attribute exists and is an empty string"""
        self.assertEqual(chessmaster.ChessPiece.prefix, '')

    def test_chesspiece_init_position_value(self):
        """Tests that the position attribute is set by constructor"""
        cp = chessmaster.ChessPiece('a1')
        self.assertEqual(cp.position, 'a1')

    def test_chesspiece_init_moves_value(self):
        """Tests that the moves list is instantiated by the constructor"""
        cp = chessmaster.ChessPiece('a1')
        self.assertEqual(cp.moves, [])

    def test_chesspiece_illegal_position_value(self):
        """Tests that the constructor disallows an illegal position."""
        with self.assertRaises(ValueError):
           cp = chessmaster.ChessPiece('a9')

    def test_algebraic_to_numeric(self):
        """Tests that algebraic_to_numeric returns the expected conversion."""
        cp = chessmaster.ChessPiece('a1')
        self.assertEqual(cp.algebraic_to_numeric('d6'), (3,5))

    def test_algebraic_bad_file(self):
        """Tests that algebraid_to_numeric returns None if passed bad file."""
        cp = chessmaster.ChessPiece('a1')
        self.assertIsNone(cp.algebraic_to_numeric('j1'))

    def test_algebraic_bad_rank(self):
        """Tests that algebraid_to_numeric returns None if passed bad rank."""
        cp = chessmaster.ChessPiece('a1')
        self.assertIsNone(cp.algebraic_to_numeric('a9'))

    def test_is_legal_move(self):
        """Tests that is_legal_move returns the expected positive output"""
        cp = chessmaster.ChessPiece('a1')
        self.assertTrue(cp.is_legal_move('b5'))

    def test_is_legal_move_returns_false(self):
        """Tests that is_legal_move returns the expected negative output"""
        cp = chessmaster.ChessPiece('a1')
        self.assertFalse(cp.is_legal_move('j9'))

    def test_move_returns_tuple(self):
        """Tests that move() returns a tuple with the prefixed positions."""
        cp = chessmaster.ChessPiece('a1')
        cp.prefix = 'Y'
        self.assertEqual(cp.move('b5')[:2], ('Ya1', 'Yb5'))
    
    def test_move_tuple_timestamp(self):
        """Tests that the move tuple returns a number that is a timestamp."""
        cp = chessmaster.ChessPiece('a1')
        retval = cp.move('b5')
        self.assertEqual(len(retval), 3)
        self.assertIsInstance(retval[2], float)

    def test_move_tuple_in_moves_log(self):
        """Tests that the returned tuples are also in the moves log."""
        cp = chessmaster.ChessPiece('a1')
        moves = []
        moves.append(cp.move('b5'))
        moves.append(cp.move('d4'))
        moves = [v[:2] for v in moves]
        cpmoves = [v[:2] for v in cp.moves]
        self.assertEqual(cpmoves, moves)

    def test_move_changes_position(self):
        """Tests that move also changes position."""
        cp = chessmaster.ChessPiece('a1')
        cp.move('b5')
        self.assertEqual(cp.position, 'b5')


if __name__ == '__main__':
    unittest.main()
