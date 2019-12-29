# -*- coding: UTF-8 -*-

def dump(value):
    if isinstance(value, bool):
        return "b:1" if value else "b:0"

    if isinstance(value, int):
        return "i:%d" % value

    if isinstance(value, str):
        return 's:%d:"%s"' % (len(value), value)

    if isinstance(value, dict):
        size = len(value)
        exprs = [dump(expr) for k, v in value.items() for expr in [k, v]]
        return "a:%d:{%s;}" % (size, ";".join(exprs))

