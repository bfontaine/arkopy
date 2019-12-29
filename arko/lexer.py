# -*- coding: UTF-8 -*-

import ply.lex

tokens = (
    'A_SYMBOL',
    'B_SYMBOL',
    'I_SYMBOL',
    'S_SYMBOL',
    'INTEGER',
    'STRING',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'COLON',
    'SEMICOLON',
)

t_COLON = r':'
t_SEMICOLON = ';'
t_LEFT_BRACKET = r'\{'
t_RIGHT_BRACKET = r'\}'

t_INTEGER = r'\d+'

t_A_SYMBOL = 'a'
t_B_SYMBOL = 'b'
t_I_SYMBOL = 'i'
t_S_SYMBOL = 's'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    raise RuntimeError(
        "Illegal character '{c}' with lexpos {p} in the area of ...{a}...".format(
            c=t.value[0], p=t.lexpos, a=t.value[0:100]))

def lex(text=None):
    lexer = ply.lex.lex()
    if text:
        lexer.input(text)
    return lexer
