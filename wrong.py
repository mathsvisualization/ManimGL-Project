from manimlib import *

class WhatDidYouSee(InteractiveScene):
    def construct(self):
        what = TexText("What did you see?")
        what.shift(UP * 1.5)

        equ = Tex(R"\int x dx = \frac{x^2}{2} - C")
        equ_c = equ.copy()[:-1]

        self.play(
            Write(equ),
            FadeIn(what, UP * 0.5)
        )
        self.wait()
        self.play(
            Transform(equ, equ_c),
            run_time=2
        )
        self.wait()