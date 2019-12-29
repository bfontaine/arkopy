#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
from .lexer import lex
from .parser import parse
from .dumper import dump

if False:
    lex, parse, dump


def decode(payload):
    return base64.b64decode(payload).decode("utf-8")

def encode(value):
    return base64.b64encode(value.encode("utf-8")).decode("utf-8")
