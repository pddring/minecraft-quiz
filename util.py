"""
This file has been taken from http://pi.minecraft.net/
"""
import collections

def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, basestring):
            for ee in flatten(e): yield ee
        else: yield e

def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))
