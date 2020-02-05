#!/usr/bin/env python3

import re

class HSV:
    """Container class for a color in HSV"""

    def __init__(self, h : float, s : float, v : float):
        if s < 0 or s > 1 or v < 0 or v > 1:
            raise ValueError("Saturation and Value expected as a percent 0-1")
        self.h = h % 360
        self.s = s
        self.v = v

    def get(self) -> tuple:
        return (self.h, self.s, self.v)

    def __repr__(self):
        return repr(self.get())

def parse(string : str) -> HSV:
    match_hsv = re.match(r'\((?P<h>\d{1,3}(?:\.\d*)?),(?P<s>[01](?:\.\d*)?),(?P<v>[01](?:\.\d*)?)\)', string)
    if match_hsv:
        h = float(match_hsv.group('h'))
        s = float(match_hsv.group('s'))
        v = float(match_hsv.group('v'))
        if s < 0 or s > 1 or v < 0 or v > 1:
            raise ValueError("Saturation and Value expectedas a percent 0-1")
        return HSV(h % 360, s, v)
    else:
        raise ValueError("HSV string parsing failed")
