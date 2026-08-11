from manimlib import *

class Test(InteractiveScene):
    def construct(self):
        t = TexText("B")
        t.set_width(FRAME_WIDTH - 1)
        self.play(Write(t))