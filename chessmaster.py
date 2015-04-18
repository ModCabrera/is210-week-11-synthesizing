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
            self.holdposition = position

    def algebraic_to_numeric(self, tile):
        axis_x = {'a': 0,
                  'b': 1,
                  'c': 2,
                  'd': 3,
                  'e': 4,
                  'f': 5,
                  'g': 6,
                  'h': 7
                  }
        axis_y = {'1': 0,
                  '2': 1,
                  '3': 2,
                  '4': 3,
                  '5': 4,
                  '6': 5,
                  '7': 6,
                  '8': 7
                  }
    
        tilelist = list(tile)
        newtile = []
        for item in tile:
            if item in axis_x:
                newtile.append(axis_x[item])
            elif item in axis_y:
                newtile.append(axis_y[item])
                newtile = tuple(newtile)
                self.position = newtile
            else:
                return None
        return newtile

    def is_legal_move(self, position):
        newposition = self.algebraic_to_numeric(position)
        if newposition is None:
            return False
        else:
            return True

    def move(self, position):
        newposition = self.prefix + position
        if self.is_legal_move(position):
            oldposition = self.prefix + self.holdposition
            newmove = []
            newmove.append(oldposition)
            newmove.append(newposition)
            newmove.append(time.time())
            newmove = tuple(newmove)
            self.moves.append(newmove)
            return self.moves
        
    


if __name__ == '__main__':
    piece = ChessPiece('a1')
    print piece.move('c4')
