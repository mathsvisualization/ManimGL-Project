from manimlib import *

class Paid(InteractiveScene):
    def construct(self):
        logo = Tex(R"\langle \psi \rangle")
        logo.set_color(PURPLE_A)
        self.add(logo)