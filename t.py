from manimlib import *

class Test(InteractiveScene):
    def construct(self):
        eq = TexText("e^{i\\pi} = -1", font_size=56)
        self.play(Write(eq), run_time=3)
        self.wait(2)