from manimlib import *

class Paid(InteractiveScene):
    def construct(self):
        logo = Tex(R"\langle \psi \rangle")
        logo.scale(0.8)
        logo.set_color(PURPLE_A)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)

        v_line = Line(UP, DOWN)
        v_line.set_height(logo.get_height() * 1.5)
        v_line.next_to(logo, RIGHT, buff=MED_SMALL_BUFF)
        v_line.insert_n_curves(10)
        v_line.set_stroke(width=[0.5, 1.5, 1.5, 0.5])
        self.add(v_line)

        h_line = Line(LEFT, RIGHT)
        h_line.set_width(FRAME_WIDTH - 2)
        h_line.to_edge(DOWN, buff=MED_LARGE_BUFF)
        h_line.insert_n_curves(10)
        h_line.set_stroke(width=[0.5, 2, 2, 0.5])
        self.add(h_line)