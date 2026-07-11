from manimlib import *

class Paid(InteractiveScene):
    def construct(self):
        logo = Tex(R"\langle \psi \rangle")
        logo.scale(0.67)
        logo.set_color(PURPLE_A)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)