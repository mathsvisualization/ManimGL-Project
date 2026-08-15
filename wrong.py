from manimlib import *

class WhatDidYouSee(InteractiveScene):
    def construct(self):
        what = TexText("What did you see?", font_size=40)
        what.shift(UP * 2)

        equ = Tex(R"\int x /; dx = \frac{x^2}{2} - C", font_size=40).set_color([PURPLE_A, PURPLE_C])
        equ_c = equ.copy()[:-2]

        self.play(
            Write(equ_c),
            FadeIn(what, UP * 0.5)
        )
        self.wait(3)
        self.play(
            FadeTransform(
                equ_c, equ,
            ),
            run_time=3
        )
        self.wait(2)