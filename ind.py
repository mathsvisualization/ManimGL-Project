from manimlib import *

class Identity(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        equ = Tex(R"6^{x + 5} = 5^{x + 5}")
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
        self.wait(0.5)

        remb = VGroup(
            TexText("Remember:"),
            Tex(R"a^{m + n} = a^m + a^n").set_color(color)
        )
        remb.arrange(DOWN, buff=LARGE_BUFF)
        remb_b = SurroundingRectangle(remb)
        remb_b.set_stroke(color, 2)
        remb_b.round_corners(0.1)
        remb[1].shift(UP * 0.5).scale(0.95)

        self.play(
            LaggedStart(Write(remb[1]), FadeIn(remb[0], UP * 0.2), lag_ratio=0.25),
            ShowCreation(remb_b)
        )
        self.wait()