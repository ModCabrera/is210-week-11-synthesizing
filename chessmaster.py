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
        boldpos = self.algebraic_to_numeric(position)
        bnewpos = self.algebraic_to_numeric(self.position)
        if ChessPiece.is_legal_move(self, position):
            if (boldpos[0]+bnewpos[0]) % (boldpos[1]+bnewpos[1]) is 0:
                return True
        else:
            return False


class King(ChessPiece):
    prefix = 'K'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        koldpos = self.algebraic_to_numeric(position)
        knewpos = self.algebraic_to_numeric(self.position)
        if ChessPiece.is_legal_move(self, position):
            if (knewpos[1]+knewpos[0]%koldpos[1]+koldpos[0]):
                return True    
            else:
                return False


class ChessMatch(object):
    

    def __init__(self, pieces=None):
        if pieces is not None:
            self.pieces = pieces
            self.log = []
        else:
            None
            
    def reset(self):
        ChessMatch.__init__(self)
        position_dict = {'Ra1': 'a1',
                    'Rh1': 'h1',
                    'Ra8': 'a8',
                    'Rh8': 'h8',
                    'Bc1': 'c1',
                    'Bf1': 'f1',
                    'Bc8': 'c8',
                    'Bf8': 'f8',
                    'Ke1': 'e1',
                    'Ke8': 'e8'}
        self.log = []
        return self.log
        
    def move(self, pieces, position):
        pieces = self.pieces
        print pieces
        
            
        



if __name__ == '__main__':
    piece = ChessPiece('a1')
    piece.move('b2')
    rook = Rook('a1')
    rook.move('h1')
    bishop = Bishop('f2')
    king = King('d4')
    match = ChessMatch({'Bf2': bishop, 'Kd5': king})
    match.move('Ke1', 'e2')
    #match.reset()
    
