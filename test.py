from manimlib import *

class MKC(InteractiveScene):
    def construct(self):
        t = Square().set_color(BLACK)
        vmobject_to_svg(t, "s.svg")
        self.add(t)
