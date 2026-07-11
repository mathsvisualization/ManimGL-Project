from manimlib import *

class Paid(InteractiveScene):
    def construct(self):
        logo = Tex(R"\langle \psi \rangle")
        logo.scale(0.8)
        logo.set_color(PURPLE_A)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)

        v_line = Line(UP, RIGHT)
        v_line.set_height(logo.get_height() * 1.5)
        v_line.next_to(logo, RIGHT, buff=SMALL_BUFF)
        self.add(v_line)