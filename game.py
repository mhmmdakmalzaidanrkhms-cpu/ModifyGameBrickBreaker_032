
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


class Game:

    def __init__(self, root):
        self.root = root
        root.title("BLOCK BREAKER")
        root.resizable(False, False)

        self.c = tk.Canvas(
            root,
            width=W,
            height=H,
            bg=BG,
            highlightthickness=0
        )
        self.c.pack()

        self.keys = set()

        root.bind("<KeyPress>", self.key_down)
        root.bind(
            "<KeyRelease>",
            lambda e: self.keys.discard(e.keysym)
        )

        # ---------- TEKS GAME ----------
        font = ("Helvetica", 12, "bold")

        self.score_text = self.c.create_text(
            20, 20,
            anchor="w",
            fill=WHITE,
            font=font
        )

        self.lives_text = self.c.create_text(
            W - 20, 20,
            anchor="e",
            fill=WHITE,
            font=font
        )

        self.msg_text = self.c.create_text(
            W // 2, H // 2 + 60,
            fill=WHITE,
            font=("Helvetica", 14),
            justify="center"
        )

        # ---------- OBJEK GAME ----------
        self.trail = [
            self.c.create_oval(
                0, 0, 0, 0,
                outline=""
            )
            for _ in range(TRAIL)
        ]

        self.ball = self.c.create_oval(
            0, 0, 0, 0,
            fill=WHITE,
            outline=""
        )

        self.paddle = self.c.create_rectangle(
            0, 0, 0, 0,
            fill=WHITE,
            outline=""
        )

        self.blocks = []
        self.particles = []

        # ---------- EFEK GAME OVER ----------
        self.overlay = self.c.create_rectangle(
            0, 0, W, H,
            fill="#000000",
            stipple="gray50",
            outline="",
            state="hidden"
        )

        self.game_over_title = self.c.create_text(
            W // 2, H // 2 - 55,
            text="GAME OVER",
            fill="#ff4757",
            font=("Helvetica", 30, "bold"),
            state="hidden"
        )

        self.game_over_score = self.c.create_text(
            W // 2, H // 2,
            text="SKOR AKHIR: 0",
            fill=WHITE,
            font=("Helvetica", 17, "bold"),
            state="hidden"
        )

        self.game_over_hint = self.c.create_text(
            W // 2, H // 2 + 55,
            text="TEKAN SPASI UNTUK MAIN LAGI",
            fill="#feca57",
            font=("Helvetica", 11, "bold"),
            state="hidden"
        )

        self.blink_counter = 0
        self.game_over_scale = 0

        self.new_game()
        self.loop()
