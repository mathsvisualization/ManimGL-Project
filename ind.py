from manimlib import *

class Independensday(InteractiveScene):
    def construct(self):
        tex1 = TexText("Can mathematics reveal a number?")
        tex1.set_width(FRAME_WIDTH - 1.5)
        self.play(Write(tex1), run_time=1.5)
        self.wait()

        self.play(tex1.animate.to_edge(UP, buff=MED_LARGE_BUFF))
        self.wait()

        expression = Tex(R"\frac{8!}{7!}\cdot\frac{\Gamma(3)}{\Gamma(2)}\cdot\binom{5}{2}\cdot\left(\zeta(0)+1\right)")
        expression.set_width(FRAME_WIDTH - 2)
        self.play(Write(expression))

        expression_box = SurroundingRectangle(
            expression,
            buff=SMALL_BUFF,
            color=YELLOW
        )
        expression_box.set_stroke(width=2)
        self.play(
            ShowCreation(expression_box),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            expression.animate.shift(2.2 * UP),
            expression_box.animate.shift(2.2 * UP)
        )
        self.play(
            Uncreate(
                expression_box
            )
        )
        self.wait()