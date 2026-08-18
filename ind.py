from manimlib import *

class Identity(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        equ = Tex(R"6^{x + 5} = 5^{x + 5}")
        equ.set_color(color)

        xequal = TexText("x = ?")
        xequal.set_color(color)
        xequal.next_to(equ, DOWN, buff=MED_LARGE_BUFF*1.1)

        self.play(LaggedStart(Write(equ), FadeIn(xequal, shift=UP * 0.5), lag_ratio=0.5))
        self.wait()

        self.play(
            equ.animate.shift(2.0 * UP),
            FadeOut(xequal, shift=DOWN*0.5)
        )
        self.wait()

        remember = VGroup(
            TexText("Remember", font_size=40),
            Tex(R"a^{m + n} = a^m \cdot a^n", font_size=40)
        )
        remember.arrange(DOWN, buff=MED_LARGE_BUFF * 1.1)
        remember.set_submobject_colors_by_gradient(color)

        remember_rect = SurroundingRectangle(remember, buff=MED_LARGE_BUFF * 0.35, stroke_width=3, stroke_color=color)
        remember_rect.round_corners(0.05)

        self.play(
            ShowCreation(remember_rect),
            LaggedStart(Write(remember[0]), FadeIn(remember[1], shift=UP * 0.5), lag_ratio=0.25)
        )
        self.wait(0.5)

        rect1 = SurroundingRectangle(equ["6^{x + 5}"][0], stroke_color=color, stroke_width=3).round_corners(0.05)
        rect2 = SurroundingRectangle(equ["5^{x + 5}"][0], stroke_color=color, stroke_width=3).round_corners(0.05)
        rect3 = SurroundingRectangle(remember[1][R"a^m \cdot a^n"][0], stroke_color=color, stroke_width=3).round_corners(0.05)

        all_rect = VGroup(rect1, rect2, rect3)

        self.play(
            LaggedStart(
                *(ShowCreation(rect) for rect in all_rect),
                lag_ratio=0,
                rate_func=lambda x: x,
                run_time=2
            )
        )
        self.wait()