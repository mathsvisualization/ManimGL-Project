from manimlib import *

class Test(InteractiveScene):
    def construct(self):
        t = TexText("Q")
        t.set_width(FRAME_WIDTH - 1)
        self.add(t)