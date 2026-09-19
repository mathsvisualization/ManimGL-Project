from manimlib import *

class FunctionGrowthComparison(Scene):
    def construct(self):
        # Title
        title = Text("How Fast Can a Function Grow?", font_size=36)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))

        # Data for functions: (Name, Math LaTeX/Text, Box Size, Color)
        # Size ko hum growth ke hisaab se scale kar rahe hain
        stages = [
            ("decimal factorial", "1", 1.0, BLUE_E),
            ("factorial", "n!", 1.5, TEAL_E),
            ("self power", "n^n", 2.2, GREEN_E),
            ("exp. quadratic", "2^{n^2}", 3.0, YELLOW_E),
            ("double exponential", "2^{2^n}", 4.0, RED_E),
        ]

        current_box = None
        current_label = None
        current_formula = None

        for name, formula_str, size, color in stages:
            # Create Card/Box
            box = Square(side_length=size, fill_color=color, fill_opacity=0.8)
            box.set_stroke(WHITE, width=2)
            box.move_to(ORIGIN)

            # Labels inside box
            lbl = Text(name, font_size=20).to_edge(UP, buff=0.2)
            form = Tex(formula_str, font_size=int(40 * (size / 2.0)))
            form.move_to(box.get_center())

            group = VGroup(box, lbl, form)

            if current_box is None:
                # Pehla box direct aayega
                self.play(FadeIn(group, scale=0.5))
            else:
                # Baaki steps me pichhla wala chhota hokar side/background me jayega aur naya bada box aayega
                self.play(
                    current_group.animate.scale(0.4).to_edge(LEFT, buff=0.5).set_opacity(0.4),
                    FadeIn(group, scale=0.7),
                    run_time=1
                )
            
            current_group = group
            self.wait(1.5)

        self.wait(2)
