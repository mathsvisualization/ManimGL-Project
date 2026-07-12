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
        cont.next_to(title, DOWN, buff=LARGE_BUFF * 0.5, aligned_edge=ORIGIN)
        cont_underline = Underline(cont, stroke_width=[0.5, 2, 2, 0.5])
        self.add(cont, cont_underline)

        cont1 = TexText("200GB+ Curated Educational Library", font_size=30)
        cont1.next_to(cont_underline, DOWN, buff=MED_LARGE_BUFF * 0.5)
        self.add(cont1)

        itm = BulletedList(
            "7000+ PDFs",
            "Books",
            "Lecture Notes",
            "Research Papers",
            "Beginners to Advanced Resources",
            buff=SMALL_BUFF,
            font_size=26
        )
        itm.next_to(cont1, DOWN, buff=MED_LARGE_BUFF * 0.67, aligned_edge=LEFT)
        self.add(itm)

        cont2 = TexText(
            """
            Whether you're a student, self-learner,\\ 
            programmer, researcher, or simply curious\\
            about science, this collection brings\\
            thousands of carefully organized educational\\
            resources together in one place\\
            """, font_size=20, alignment=R"\flushleft"
        )
        cont2.next_to(itm, DOWN, buff=MED_LARGE_BUFF * 0.67, aligned_edge=LEFT)
        self.add(cont2)

        inside = VGroup(
            TexText("Inside you'll find:", font_size=26),
            BulletedList(
                "Mathematics",
                "Physics",
                "Chemistry",
                "Quantum Mechanics",
                "Astronomy",
                "Computer Science",
                R"Artificial Intelligence \& Machine Learning",
                buff=SMALL_BUFF,
                font_size=20
            )
        )
        inside.arrange(DOWN, buff=SMALL_BUFF, aligned_edge=LEFT)
        inside[0].shift(LEFT * 0.5)
        inside.next_to(cont2, DOWN, aligned_edge=LEFT)
        self.add(inside)