from manimlib import *

class Paid(InteractiveScene):
    pgno = "1"
    def construct(self):
        logo = Tex(R"\langle \psi \rangle")
        logo.scale(0.8)
        logo.set_color(PURPLE_A)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)

        v_line = Line(UP, DOWN)
        v_line.set_height(logo.get_height() * 1.5)
        v_line.next_to(logo, RIGHT, buff=MED_SMALL_BUFF)
        v_line.insert_n_curves(10)
        v_line.set_stroke(width=[0.5, 1.5, 1.5, 0.5])
        self.add(v_line)

        h_line = Line(LEFT, RIGHT)
        h_line.set_width(FRAME_WIDTH - 1)
        h_line.to_edge(DOWN, buff=MED_LARGE_BUFF * 0.75 + SMALL_BUFF)
        h_line.insert_n_curves(10)
        h_line.set_stroke(width=[0.5, 2, 2, 0.5])
        self.add(h_line)

        pg = TexText(str(self.pgno))
        cir = Circle(radius=0.1)
        cir.set_stroke(width=1, color=WHITE)
        cir.set_fill("#191919", 1.0)
        pg.move_to(cir)
        pg.set_height(cir.get_height() * 0.5)
        vg = VGroup(cir, pg)
        vg.next_to(h_line, DOWN, buff=SMALL_BUFF)
        self.add(cir, pg)

        title = TexText("Ultimate Learning Bundle (200GB+)", font_size=30)
        title.next_to(v_line, RIGHT)
        self.add(title)

        cont = TexText(R"The Knowledge Vault")
        cont.next_to(title, DOWN, buff=LARGE_BUFF*0.7, aligned_edge=ORIGIN)
        cont_underline = Underline(cont, stroke_width=[0.5, 2, 2, 0.5])
        self.add(cont, cont_underline)