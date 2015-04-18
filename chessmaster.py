#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster Piece Tracker"""
import time


class ChessPiece(object):
    prefix = ''
    
    def __init__(self, position):
        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        xaxes = 'abcdefgh'
        yaxes = [1,2,3,4,5,6,7,8]
        if len(tile) > 2:
            return None
        else:
            if tile[0] in xaxes and int(tile[1]) in yaxes:
                return (xaxes.find(tile[0]), int(tile[1])-1)
            else:
                return None

    def is_legal_move(self, position):
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        if self.is_legal_move(position):
            move = (self.prefix + self.position, self.prefix + position, time.time())
            self.moves.append(move)
            self.position = position
            return move
        else:
            return False


class Rook(ChessPiece):
    prefix = 'R'
    
    
    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            else:
                if int(self.position[1]) == int(position[1]):
                    return True
        else:
            return False


class Bishop(ChessPiece):
    prefix = 'B'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        newpos = self.algebraic_to_numeric(position)
        oldpos = self.algebraic_to_numeric(self.position)
        if ChessPiece.is_legal_move(self, position):
            if (newpos[0]%oldpos[0]) == (newpos[1]%oldpos[1]):
                return True
        else:
            return False


class King(ChessPiece):
    prefix = 'K'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        if ChessPiece.is_legal_move(self, position):
            
            return True
        else:
            return False




if __name__ == '__main__':
    piece = ChessPiece('a1')
    piece.move('b2')
    rook = Rook('a1')
    rook.move('h1')
    bishop = Bishop('c3')
    print bishop.move('a5')
    king = King('a1')
    king.move('a8')
