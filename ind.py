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
        self.wait(0.1)

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
            LaggedStart(FadeIn(remb[0], UP * 0.2), Write(remb[1]), lag_ratio=0.25),
            ShowCreation(remb_b),
            lag_ratio=1
        )
        self.wait()

        idt = VGroup(
            SurroundingRectangle(equ["6^{x + 5}"]),
            SurroundingRectangle(equ["5^{x + 5}"]),
            SurroundingRectangle(remb[1]["a^m + a^n"])
        )
        self.add(idt[0], idt[1], idt[2])
        """self.play(
            ShowCreation(idt[0]),
            ShowCreation(idt[1]),
            ShowCreation(idt[2])
        )
        self.wait()"""