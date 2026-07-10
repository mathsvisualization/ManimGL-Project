from manimlib import *

class MKC(InteractiveScene):
    def construct(self):
        t = Text("Hello Sex").set_color(BLACK)
        vmobject_to_svg(t, "s.svg")
        self.add(t)
