#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster Piece Tracker"""
import time
import pprint

class ChessPiece(object):
    prefix = ''

    def __init__(self, position):
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        xaxes = 'abcdefg'
        if tile[0] in xaxes:
            if int(tile[1]) <= 8:
                return (xaxes.find(tile[0]), int(tile[1])-1)
            

    def is_legal_move(self, position):
        newposition = self.algebraic_to_numeric(position)
        if newposition is None:
            return False
        else:
            return True

    def move(self, position):
        if self.is_legal_move(position):
            oldposition = self.prefix + self.position
            newposition = self.prefix + position
            newmove = []
            newmove.append(newposition)
            newmove.append(time.time())
            newmove = tuple(newmove)
            self.moves.append(newmove)
            return self.moves
        
    


if __name__ == '__main__':
    piece = ChessPiece('a1')
    print piece.move('c4')
