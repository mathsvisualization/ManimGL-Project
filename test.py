from manimlib import *

class MKC(InteractiveScene):
    def construct(self):
        t = Text("Hello Sex")
        vmobject_to_svg(t, "s")
        self.add(t)
