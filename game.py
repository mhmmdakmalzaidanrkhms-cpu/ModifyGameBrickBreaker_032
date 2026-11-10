
import tkinter as tk
import random
import math


W, H = 600, 500
FPS = 60
SPEED = 5

PADDLE_W = 90
PADDLE_H = 10
PADDLE_Y = H - 40

RADIUS = 7
TRAIL = 10
COLS, ROWS = 10, 5

BG = "#0f1117"
WHITE = "#ffffff"
STRONG = "#dee2e6"

ROW_COLORS = [
    "#f06595",
    "#cc5de8",
    "#845ef7",
    "#5c7cfa",
    "#339af0"
]


def blend(c1, c2, t):
    a = [int(c1[i:i+2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i+2], 16) for i in (1, 3, 5)]

    return "#%02x%02x%02x" % tuple(
        int(x + (y - x) * t)
        for x, y in zip(a, b)
    )

