from manimlib import *

class NGA(InteractiveScene):
    def construct(self):
        tex = Tex(R"\int x\, dx = \frac{x^2}{2}", font_size=40)
        tex2 = Tex(R"\int x\, dx = \frac{x^2}{2} - C", font_size=40)

        self.play(Transform(tex, tex2[:-2]), FadeIn(tex2["- C"][0]))
        self.wait()