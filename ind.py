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

        remember = VGroup(
            TexText("Remember!", font_size=40),
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
        self.wait(0.1)

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

        new_equ = Tex(R"6^x \cdot 6^5 = 5^x \cdot 5^5")
        new_equ.shift(2.0 * UP)
        new_equ.set_color(color)

        all_rects = VGroup(
            SurroundingRectangle(new_equ[R"6^x \cdot 6^5"], stroke_width=3, stroke_color=color).round_corners(0.05),
            SurroundingRectangle(new_equ[R"5^x \cdot 5^5"], stroke_width=3, stroke_color=color).round_corners(0.05)
        )

        self.play(
            Transform(equ["6^{x"][0], new_equ["6^x"][0], remover=True),
            ReplacementTransform(rect1, all_rects[0]),
            FadeIn(new_equ[R"\cdot"][0], remover=True),
            FadeOut(equ["+"][0]),
            Transform(equ["6"][0].copy(), new_equ["6"][1], remover=True),
            Transform(equ["5"][0], new_equ["5"][0], remover=True),
            Transform(equ["5^{x"][0], new_equ["5^x"][0], remover=True),
            Transform(equ["5"][1].copy(), new_equ["5"][2], remover=True),
            FadeIn(new_equ[R"\cdot"][1], remover=True),
            FadeOut(equ["+"][1]),
            Transform(equ["5"][-1], new_equ["5"][-1], remover=True),
            ReplacementTransform(rect2, all_rects[1]),
        )
        self.remove(equ)
        self.add(new_equ)
        self.wait()

        self.play(
            FadeOut(remember, shift=DOWN * 0.5),
            LaggedStart(
                *(Uncreate(rec) for rec in [*all_rect, *all_rects, remember_rect]),
                lag_ratio=0,
                rate_func=linear,
            )
        )
        self.wait()

        frac_equ = Tex(R"\frac{6^x}{5^x} = \frac{5^5}{6^5}", isolate=["6^x", "5^x", "5^5", "6^5"])
        frac_equ.set_color(color)
        self.play(
            LaggedStart(
                Transform(new_equ["="][0], frac_equ["="][0], remover=True),
                Transform(new_equ["6^x"][0], frac_equ["6^x"][0], remover=True),
                Transform(new_equ["5^x"][0], frac_equ["5^x"][0], remover=True),
                Transform(new_equ[R"\cdot"][0], frac_equ[2], remover=True),
                Transform(new_equ["5^5"][0], frac_equ["5^5"][0], remover=True),
                Transform(new_equ["6^5"][0], frac_equ["6^5"][0], remover=True),
                Transform(new_equ[R"\cdot"][1], frac_equ[-3], remover=True),
                lag_ratio=0.25
            )
        )
        self.add(frac_equ)
        self.play(
            frac_equ.animate.shift(2.0 * UP)
        )
        self.wait()

        frac_igp = VGroup(
            TexText("Remember!", font_size=40),
            Tex(R"\frac{a^n}{b^n} = \left( \frac{a}{b} \right)^n")
        )
        frac_igp.set_color(color)
        frac_igp.arrange(DOWN, buff=MED_LARGE_BUFF * 1.1)

        frac_igp_rect = SurroundingRectangle(frac_igp, stroke_width=3, stroke_color=color, buff=MED_LARGE_BUFF * 0.35).round_corners(0.05)

        frac_rects = VGroup(
            SurroundingRectangle(frac_equ[R"\frac{6^x}{5^x}"], stroke_width=3, stroke_color=color).round_corners(0.05),
            SurroundingRectangle(frac_equ[R"\frac{5^5}{6^5}"], stroke_width=3, stroke_color=color).round_corners(0.05),
            SurroundingRectangle(frac_igp[1][R"\left( \frac{a}{b} \right)^n"], stroke_width=3, stroke_color=color, buff=SMALL_BUFF * 0.75).round_corners(0.05),
        )
        self.play(
            Write(frac_igp[0]),
            FadeIn(frac_igp[1], DOWN * 0.5),
            ShowCreation(frac_igp_rect)
        )
        self.wait()
        frac_igp_rect.shift(0.0000001*RIGHT)
        self.play(
            LaggedStart(
             *(ShowCreation(rect) for rect in frac_rects),
                lag_ratio=0,
                rate_func=linear,
            )
        )
        self.wait()

        fin = Tex(R"\left( \frac{6}{5} \right)^x = \left( \frac{5}{6} \right)^5", isolate=["6", "5", R"\left(", R"\right)"])
        fin.shift(2.0 * UP)
        fin.set_color(color)

        fin_rects = VGroup(
            SurroundingRectangle(fin[R"\left( \frac{6}{5} \right)^x"], stroke_width=3, stroke_color=color).round_corners(0.05),
            SurroundingRectangle(fin[R"\left( \frac{5}{6} \right)^5"], stroke_width=3, stroke_color=color).round_corners(0.05),
        )
        self.play(
            Transform(frac_equ["6"][0], fin["6"][0],),
            Transform(frac_equ["5"][0], fin["5"][0],),
            Transform(frac_equ["x"], fin["x"][0],),
            Write(fin[R"\left("]),
            Write(fin(R"\right)"))
        )
        self.wait()