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

        title = TexText("Ultimate Learning Bundle (200GB+)", font_size=36)
        title.next_to(v_line, RIGHT)
        self.add(title)

        content = TexText(
             r"""
            {\Huge \textbf{The Knowledge Vault}}

          
            \vspace{0.5cm}

            {\Large 100GB+ Curated Educational Library}

            \vspace{0.6cm}

            5000+ PDFs $\bullet$ Books $\bullet$ Lecture Notes $\bullet$ Research Papers

            \vspace{0.8cm}

            Whether you're a student, self-learner, programmer,
            researcher, or simply curious about science,
            this collection brings thousands of carefully
            organized educational resources together in one place.

            \vspace{0.8cm}

            \textbf{Inside you'll find:}

            \vspace{0.3cm}

            $\bullet$ Mathematics\\
            $\bullet$ Physics\\
            $\bullet$ Chemistry\\
            $\bullet$ Quantum Mechanics\\
            $\bullet$ Astronomy\\
            $\bullet$ Computer Science

            \vspace{0.8cm}

            \textit{No endless searching. Everything is organized and ready to use.}
            """,)
        self.add(content)