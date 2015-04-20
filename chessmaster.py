#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster Piece Tracker"""
import time


class ChessPiece(object):
    """Docstring
    """
    prefix = ''
    
    def __init__(self, position):
        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Docstring
        """
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
        """Docstring
        """
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """Docstring
        """
        if self.is_legal_move(position):
            move = (self.prefix + self.position, self.prefix + position, time.time())
            self.moves.append(move)
            self.position = position
            return move
        else:
            return False


class Rook(ChessPiece):
    """Docstring
    """
    prefix = 'R'
    
    
    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Docstring
        """
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
    """Docstring
    """
    prefix = 'B'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Docstring
        """
        boldpos = self.algebraic_to_numeric(position)
        bnewpos = self.algebraic_to_numeric(self.position)
        if ChessPiece.is_legal_move(self, position):
            if (boldpos[0]+bnewpos[0]) % (boldpos[1]+bnewpos[1]) is 0:
                return True
        else:
            return False


class King(ChessPiece):
    """Docstring
    """
    prefix = 'K'

    def __init__(self, position):
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Docstring
        """
        oldpos = self.algebraic_to_numeric(position)
        newpos = self.algebraic_to_numeric(self.position)
        if ((abs(newpos[1] - oldpos[1]) <= 1)):
            if (newpos[1]+newpos[0]%oldpos[1]+oldpos[0]):
                return True
        else:
            return False


class ChessMatch(object):
    """Docstring
    """
    

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []
            
    def reset(self):
        """Some Docstring.
        """
        self.log = []
        self.pieces = {'Ra1': Rook('a1'),
                    'Rh1': Rook('h1'),
                    'Ra8': Rook('a8'),
                    'Rh8': Rook('h8'),
                    'Bc1': Bishop('c1'),
                    'Bf1': Bishop('f1'),
                    'Bc8': Bishop('c8'),
                    'Bf8': Bishop('f8'),
                    'Ke1': King('e1'),
                    'Ke8': King('e8')}
        
        return self.pieces
        
    def move(self, piece, position):
        """Docstring
        """
        ChessPiece.move.__init__(self)
        if piece in self.pieces:
            self.pieces[piece]
            chesspiece = self.pieces[piece]
            moved = chesspiece.move(position)
            self.log.append(moved)
            self.pieces.pop(piece)
            self.pieces.update({moved[1]:chesspiece})
