from manimlib import *

class WhatDidYouSee(InteractiveScene):
    def construct(self):
        what = TexText("Nothing wrong here,", font_size=40)
        what.shift(UP * 3)

        see = TexText("What did you see?", font_size=38).set_color([YELLOW, ORANGE])
        see.next_to(what, DOWN, buff=MED_LARGE_BUFF)

        equ = Tex(R"\int x\, dx = \frac{x^2}{2}", font_size=40).set_color([PURPLE_A, PURPLE_C])
        equ_c = Tex(R"\int x\, dx = \frac{x^2}{2} - C", font_size=40).match_style(equ)

        self.play(
            Write(equ),
            FadeIn(what, UP * 0.5)
        )
        self.wait(3)
        self.play(
            Transform(
                equ, equ_c[:-2],
            ),
            FadeIn(equ_c["- C"]),
            FadeIn(see),
            run_time=1.5
        )
        self.wait(3) 