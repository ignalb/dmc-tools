#!/usr/bin/env python3

import re

class RGB:
    """Container class for a color in RGB space"""

    def __init__(self, r : int, g : int, b : int):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            raise ValueError("RGB value should be in the range 0-255")
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def get(self) -> tuple:
        return (self.r, self.g, self.b)

    def asFloat(self) -> tuple:
        return (self.r/255, self.g/255, self.b/255)

    def __repr__(self):
        return repr(self.get())

def parse(string : str) -> RGB:
    match_rgb = re.match(r'\((?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3})\)', string)
    if match_rgb:
        for group in match_rgb.groups():
            if int(group) < 0 or int(group) > 255:
                raise ValueError("RGB value should be in the range 0-255")
        return RGB( int(match_rgb.group('r')),
                    int(match_rgb.group('g')),
                    int(match_rgb.group('b')))
    else:
        raise ValueError("RGB string parsing failed.")
