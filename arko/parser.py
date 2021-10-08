# -*- coding: UTF-8 -*-

import ply.yacc
from collections import OrderedDict

from .lexer import tokens, lex

# a:4:{s:4:"date";s:10:"2019-12-29";s:10:"type_fonds";s:11:"arko_seriel";s:4:"ref1";i:12;s:4:"ref2";i:4669;}
from .models import Object

start = 'expression'


def p_expression(p):
    """expression : atom
                  | associative"""
    p[0] = p[1]


def p_atom(p):
    """atom : integer
            | float
            | boolean
            | string
            | null"""
    p[0] = p[1]


def p_collection(p):
    """associative : array
                   | object"""
    p[0] = p[1]


def p_integer(p):
    """integer : I_SYMBOL COLON INTEGER"""
    p[0] = int(p[3])


def p_float(p):
    """float : D_SYMBOL COLON FLOAT"""
    p[0] = float(p[3])


def p_boolean(p):
    """boolean : B_SYMBOL COLON INTEGER"""
    p[0] = p[3] != "0"


def p_string(p):
    """string : S_SYMBOL COLON INTEGER COLON STRING"""
    p[0] = p[5]


def p_null(p):
    """null : N_SYMBOL"""
    p[0] = None


def p_array(p):
    """array : A_SYMBOL raw_array"""
    p[0] = p[2]


def p_raw_array(p):
    """raw_array : COLON INTEGER COLON LEFT_BRACKET array_expressions RIGHT_BRACKET"""
    d = OrderedDict()
    expressions = p[5]
    for i, k in enumerate(expressions[::2]):
        d[k] = expressions[i * 2 + 1]
    p[0] = d


def p_array_expressions_array_expression(p):
    """array_expressions : expression SEMICOLON"""
    p[0] = [p[1]]


def p_array_expressions_array_expression_array_expressions(p):
    """array_expressions : expression SEMICOLON array_expressions"""
    p[0] = [p[1]] + p[3]


def p_object(p):
    """object : O_SYMBOL COLON INTEGER COLON STRING raw_array"""
    p[0] = Object(p[5], dict(p[6]))


def eof():
    raise RuntimeError('EOF Reached')


def p_error(p):
    if p is None:
        eof()
    else:
        raise RuntimeError(str(p))


def parse(text):
    parser = ply.yacc.yacc()
    expression = parser.parse(text, lexer=lex())
    return expression
