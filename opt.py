from manimlib import *

class Identity(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        equ = Tex(R"6^{x + 5} = 5^{x + 5}")
        equ.set_color(color)

        xequal = TexText("x = ?")
        xequal.set_color(color)
        xequal.next_to(equ, DOWN, buff=MED_LARGE_BUFF * 1.1)

        self.play(
            LaggedStart(
                Write(equ),
                FadeIn(xequal, shift=UP * 0.5),
                lag_ratio=0.5
            )
        )
        self.wait()

        self.play(
            equ.animate.shift(2.0 * UP),
            FadeOut(xequal, shift=DOWN * 0.5)
        )
        self.wait()

        remember = VGroup(
            TexText("Remember", font_size=40),
            Tex(R"a^{m + n} = a^m \cdot a^n", font_size=40)
        )
        remember.arrange(DOWN, buff=MED_LARGE_BUFF * 1.1)
        remember.set_submobject_colors_by_gradient(color)

        remember_rect = SurroundingRectangle(
            remember,
            buff=MED_LARGE_BUFF * 0.35,
            stroke_width=3,
            stroke_color=color
        ).round_corners(0.05)

        self.play(
            ShowCreation(remember_rect),
            LaggedStart(
                Write(remember[0]),
                FadeIn(remember[1], shift=UP * 0.5),
                lag_ratio=0.25
            )
        )
        self.wait(0.1)

        rects = [
            SurroundingRectangle(
                equ[f"{base}^{{x + 5}}"][0],
                stroke_color=color,
                stroke_width=3
            ).round_corners(0.05)
            for base in (6, 5)
        ]

        rect3 = SurroundingRectangle(
            remember[1][R"a^m \cdot a^n"][0],
            stroke_color=color,
            stroke_width=3
        ).round_corners(0.05)

        self.play(
            LaggedStart(
                *(ShowCreation(rect) for rect in (*rects, rect3)),
                lag_ratio=0,
                rate_func=lambda x: x,
                run_time=2
            )
        )
        self.wait()

        new_equ = Tex(R"6^x \cdot 6^5 = 5^x \cdot 5^5")
        new_equ.shift(2.0 * UP)
        new_equ.set_color(color)

        all_rects = [
            SurroundingRectangle(
                new_equ[f"{base}^x \\cdot {base}^5"],
                stroke_width=3,
                stroke_color=color
            ).round_corners(0.05)
            for base in (6, 5)
        ]

        # Transform both sides using the same pattern
        transforms = []

        for i, base in enumerate((6, 5)):
            old_power = equ[f"{base}^{{x"][0]
            new_power = new_equ[f"{base}^x"][0]

            old_base = equ[str(base)][0 if base == 6 else 1]
            new_base = new_equ[str(base)][1 if base == 6 else 2]

            transforms.extend([
                Transform(old_power, new_power),
                Transform(old_base.copy(), new_base),
                FadeIn(new_equ[R"\cdot"][i]),
                FadeOut(equ["+"][i]),
                ReplacementTransform(rects[i], all_rects[i]),
            ])

        
        transforms.append(
                    Transform(
                        equ["5"][-1],
                        new_equ["5"][-1]
                    )
        )
        self.play(*transforms)
        self.wait()