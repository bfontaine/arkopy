# -*- coding: UTF-8 -*-

import ply.yacc
from collections import OrderedDict

from .lexer import tokens, lex

# a:4:{s:4:"date";s:10:"2019-12-29";s:10:"type_fonds";s:11:"arko_seriel";s:4:"ref1";i:12;s:4:"ref2";i:4669;}

start = 'expression'


def p_expression(p):
    """expression : integer
                  | boolean
                  | string
                  | null
                  | array"""
    p[0] = p[1]


def p_integer(p):
    """integer : I_SYMBOL COLON INTEGER"""
    p[0] = int(p[3])


def p_boolean(p):
    """boolean : B_SYMBOL COLON INTEGER"""
    p[0] = p[3] != "0"


def p_string(p):
    """string : S_SYMBOL COLON INTEGER COLON STRING"""
    p[0] = p[5]


def p_null(p):
    """null : N_SYMBOL """
    p[0] = None


def p_array(p):
    """array : A_SYMBOL COLON INTEGER COLON LEFT_BRACKET array_expressions RIGHT_BRACKET"""
    d = OrderedDict()
    expressions = p[6]
    for i, k in enumerate(expressions[::2]):
        d[k] = expressions[i * 2 + 1]
    p[0] = d


def p_array_expressions_array_expression(p):
    """array_expressions : array_expression"""
    p[0] = [p[1]]


def p_array_expressions_array_expression_array_expressions(p):
    """array_expressions : array_expression array_expressions"""
    p[0] = [p[1]] + p[2]


def p_array_expression_expression(p):
    """array_expression : expression SEMICOLON"""
    p[0] = p[1]


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
