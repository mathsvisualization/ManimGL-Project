from manimlib import *

class Identity(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        equ = Tex("6^{x + 5} = 5^{x + 5}")
        equ.shift(UP)
        equ.set_color(color)
        
        ax = Tex("x = ?")
        ax.next_to(equ, DOWN, buff=MED_LARGE_BUFF)
        ax.set_color(color)

        self.play(LaggedStart(Write(equ), FadeIn(ax, UP * 0.5), lag_ratio=0.67))
        self.wait()

        self.play(
            FadeOut(ax, DOWN * 1),
            equ.animate.shift(UP * 1),
            run_time=0.67
        )
        self.wait(0.1)

        remb = VGroup(
            TexText("Remember:"),
            Tex(R"a^{m + n} = a^m \cdot a^n").set_color(color)
        )
        remb.arrange(DOWN, buff=LARGE_BUFF)

        r_s = SurroundingRectangle(remb.copy(), buff=MED_LARGE_BUFF * 0.4)
        r_s.set_stroke(color, 2)
        r_s.round_corners(0.1)

        self.play(
            LaggedStart(FadeIn(remb[0], UP * 0.2), Write(remb[1]), lag_ratio=0.25),
            ShowCreation(r_s),
            lag_ratio=1
        )
        self.wait()

        surs = VGroup(
            SurroundingRectangle(equ["6^{x + 5}"]),
            SurroundingRectangle(equ["5^{x + 5}"]),
            SurroundingRectangle(remb[1][R"a^m \cdot a^n"])
        )
        for sur in surs:
            sur.set_stroke(color, 2)
            sur.round_corners(0.1)

        self.play(ShowCreation(surs[-1]))
        self.play(TransformFromCopy(surs[-1], surs[0]), TransformFromCopy(surs[-1], surs[1]))
        self.wait()