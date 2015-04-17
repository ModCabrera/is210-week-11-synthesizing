#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster Piece Tracker"""
import time


class ChessPiece(object):
    prefix = ''

    def __init__(self, position):
        self.position = position
        self.moves = []

    def algebraic_to_numeric(self, tile):
        axis_x = {0: 'a',
                  1: 'b',
                  2: 'c',
                  3: 'd',
                  4: 'e',
                  5: 'f',
                  6: 'g',
                  7: 'h'
                  }
        axis_y = {0: '1',
                  1: '2',
                  2: '3',
                  3: '4',
                  4: '5',
                  5: '6',
                  6: '7',
                  7: '8'
                  }
        
        tilelist = list(tile)
        self.newtile = {}
        keyindex = 0 
        for xkey, xvalue in axis_x.iteritems():
            if tilelist[0] == xvalue:
                keyindex = xkey
                self.newtile.update({xkey:0})
        for ykey, yvalue in axis_y.iteritems():
            if tilelist[1] == yvalue:
                self.newtile[keyindex] = ykey
                self.newtile = self.newtile.items().pop()
        if sum(self.newtile) >= 15:
            self.newtile = None
            return self.newtile
        else:
            return self.newtile
        
if __name__ == '__main__':
    piece = ChessPiece('g8')
    print piece.position
    print piece.algebraic_to_numeric('a2')
    print piece.algebraic_to_numeric('g8')
    print piece.algebraic_to_numeric('j9')
