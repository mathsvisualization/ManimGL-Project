from manimlib import *

class WhatDidYouSee(InteractiveScene):
    def construct(self):
        what = TexText("Nothing wrong here,", font_size=40)
        what.shift(UP * 3)

        see = TexText("What did you see?", font_size=38).set_color([YELLOW, ORANGE])
        see.next_to(what, DOWN, buff=MED_LARGE_BUFF)

        equ = Tex(R"\int x\, dx = \frac{x^2}{2} - C", font_size=40).set_color([PURPLE_A, PURPLE_C])
        equ_c = equ.copy()[:-2]

        self.play(
            Write(equ_c),
            FadeIn(what, UP * 0.5)
        )
        self.wait(3)
        self.play(
            Transform(
                equ_c, equ[:-2],
            ),
            Write(equ[-2:]),
            Write(see),
            lag_ratio=0.25,
            run_time=1
        )
        self.wait(2)