# -*- coding: UTF-8 -*-

def dump(value):
    if isinstance(value, bool):
        return "b:1" if value else "b:0"

    if isinstance(value, int):
        return "i:%d" % value

    if isinstance(value, float):
        return "d:%f" % value

    if isinstance(value, str):
        return 's:%d:"%s"' % (len(value), value.replace('\\', '\\\\').replace('"', '\\"'))

    if value is None:
        return 'N'

    if isinstance(value, (dict, list, tuple)):
        size = len(value)

        kvs = value.items() if isinstance(value, dict) else enumerate(value)
        expressions = [dump(expression) for k, v in kvs for expression in [k, v]]

        return "a:%d:{%s;}" % (size, ";".join(expressions))
