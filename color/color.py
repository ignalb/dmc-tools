#!/usr/bin/env python3

import re
from color.rgb import RGB
from color.hsv import HSV

def RGBtoHSV(input : RGB) -> HSV:
    V = max(input.r, input.g, input.b)
    C = V - min(input.r, input.g, input.b)
    if input.r == input.g == input.b:
        H = 0
    elif input.r == V:
        H = 60 * (input.g - input.b) / C
    elif input.g == V:
        H = 60 * (2 + (input.b - input.r) / C)
    else: #input.b == V
        H = 60 * (4 + (input.r - input.g) / C)

    if input.r == input.g == input.b == 0:
        S = 0
    else:
        S = C / V

    return HSV(H, S, V / 255)

def RGBtoHex(input : RGB) -> str:
    return '#{0:0{1}x}'.format(input.r << 16 | input.g << 8 | input.b, 6)

def HSVtoRGB(input : HSV) -> RGB:
    C = input.v * input.s
    H_ = input.h / 60;
    X = C * (1 - abs(H_ % 2 - 1))
    if 0 <= H_ <= 1:
        (r_, g_, b_) = (C, X, 0)
    elif 1 < H_ <= 2:
        (r_, g_, b_) = (X, C, 0)
    elif 2 < H_ <= 3:
        (r_, g_, b_) = (0, C, X)
    elif 3 < H_ <= 4:
        (r_, g_, b_) = (0, X, C)
    elif 4 < H_ <= 5:
        (r_, g_, b_) = (X, 0, C)
    elif 5 < H_ <= 6:
        (r_, g_, b_) = (C, 0, X)
    else:
        (r_, g_, b_) = (0, 0, 0)
    m = input.v - C
    return RGB(*tuple(int(255*(n+m)) for n in (r_, g_, b_)))

def HSVtoHex(input : HSV) -> str:
    return RGBtoHex(HSVtoRGB(input))

class Color:
    """A color container class.

    Internally stores as RGB"""

    def __init__(self, value : 'hex str or RGB or HSV'):
        if type(value) is str:
            match_hex = re.match(r'(?:#|0[xX])(?P<r>[0-9a-fA-F]{2})(?P<g>[0-9a-fA-F]{2})(?P<b>[0-9a-fA-F]{2})$', value)
            if match_hex:
                r = int(match_hex.group('r'), 16)
                g = int(match_hex.group('g'), 16)
                b = int(match_hex.group('b'), 16)
                self.color = RGB(r,g,b)
            else:
                raise ValueError("Input string parsing failed.")
        elif type(value) is RGB:
            self.color = value
        elif type(value) is HSV:
            self.color = HSVtoRGB(value)
        else:
            raise ValueError("Value must be a hex code passed as a string ",
                            ", or RGB object, or HSV object")

    def asRGB(self) -> RGB:
        return self.color

    def asHSV(self) -> HSV:
        return RGBtoHSV(self.color)

    def asHex(self) -> str:
        return RGBtoHex(self.color)

    def __repr__(self):
        return repr(self.color)
