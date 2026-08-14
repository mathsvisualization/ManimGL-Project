from manimlib import *


class Independence80(InteractiveScene):
    def construct(self):

        title = Text(
            "Can mathematics reveal a number?",
            font_size=42
        ).to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        expression = Tex(r"\frac{8!}{7!}\cdot\frac{\Gamma(3)}{\Gamma(2)}\cdot\binom{5}{2}\cdot\left(\zeta(0)+1\right)", font_size=48)

        self.play(Write(expression))
        self.wait(2)

        box = SurroundingRectangle(expression[0], buff=0.15)
        self.play(ShowCreation(box))

        step = Tex(r"\frac{8!}{7!}=8", font_size=42)
        step.next_to(expression, DOWN, buff=0.8)

        self.play(Write(step))
        self.wait(1)
        self.play(FadeOut(box), FadeOut(step))

        new_expression = Tex(r"8\cdot\frac{\Gamma(3)}{\Gamma(2)}\cdot\binom{5}{2}\cdot\left(\zeta(0)+1\right)", font_size=48)

        self.play(Transform(expression, new_expression))
        expression = new_expression

        box = SurroundingRectangle(expression[2], buff=0.15)
        self.play(ShowCreation(box))

        step = Tex(r"\frac{\Gamma(3)}{\Gamma(2)}=\frac{2!}{1!}=2", font_size=42)
        step.next_to(expression, DOWN, buff=0.8)

        self.play(Write(step))
        self.wait(1)
        self.play(FadeOut(box), FadeOut(step))

        new_expression = Tex(r"8\cdot2\cdot\binom{5}{2}\cdot\left(\zeta(0)+1\right)", font_size=48)

        self.play(Transform(expression, new_expression))
        expression = new_expression

        box = SurroundingRectangle(expression[4], buff=0.15)
        self.play(ShowCreation(box))

        step = Tex(r"\binom{5}{2}=\frac{5!}{2!3!}=10", font_size=42)
        step.next_to(expression, DOWN, buff=0.8)

        self.play(Write(step))
        self.wait(1)
        self.play(FadeOut(box), FadeOut(step))

        new_expression = Tex(r"8\cdot2\cdot10\cdot\left(\zeta(0)+1\right)", font_size=48)

        self.play(Transform(expression, new_expression))
        expression = new_expression

        box = SurroundingRectangle(expression[6], buff=0.15)
        self.play(ShowCreation(box))
        self.wait(1)

        step = Tex(r"\zeta(0)=-\frac{1}{2}", font_size=48)
        step.next_to(expression, DOWN, buff=0.8)

        self.play(Write(step))
        self.wait(1.5)

        step2 = Tex(r"\zeta(0)+1=-\frac{1}{2}+1=\frac{1}{2}", font_size=42)
        step2.next_to(expression, DOWN, buff=0.8)

        self.play(Transform(step, step2))
        self.wait(1.5)

        self.play(FadeOut(box), FadeOut(step))

        final_expression = Tex(r"8\times2\times10\times\frac{1}{2}", font_size=60)

        self.play(Transform(expression, final_expression))
        self.wait(1.5)

        result = Tex(r"8\times2\times10\times\frac{1}{2}=80", font_size=70)

        self.play(Transform(final_expression, result))
        self.wait(2)

        eighty = Tex(r"80", font_size=180)

        self.play(
            FadeOut(title),
            FadeOut(result)
        )

        self.play(Write(eighty))
        self.wait(2)

        self.play(eighty.animate.scale(0.45).to_edge(LEFT))

        outer_circle = Circle(
            radius=2.2,
            stroke_width=6
        )

        inner_circle = Circle(
            radius=0.35,
            stroke_width=4
        )

        spokes = VGroup()

        for k in range(24):
            spoke = Line(
                ORIGIN,
                2.2 * UP,
                stroke_width=3
            )
            spoke.rotate(k * TAU / 24)
            spokes.add(spoke)

        chakra = VGroup(
            outer_circle,
            inner_circle,
            spokes
        )

        chakra.move_to(RIGHT * 2)

        self.play(
            ShowCreation(outer_circle),
            run_time=1
        )

        self.play(
            LaggedStart(
                *[ShowCreation(spoke) for spoke in spokes],
                lag_ratio=0.05
            ),
            run_time=3
        )

        self.play(ShowCreation(inner_circle))

        self.wait(1)

        final_text = Text(
            "80th Independence Day",
            font_size=44
        ).to_edge(DOWN)

        self.play(Write(final_text))

        self.wait(3)