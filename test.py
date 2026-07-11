from manimlib import *

class MKC(InteractiveScene):
    def construct(self):
        t = Square().set_color(BLACK).set_color([GREEN, RED], opacity=0.5)
        vmobject_to_svg(t, "s.svg")
        self.add(t)
